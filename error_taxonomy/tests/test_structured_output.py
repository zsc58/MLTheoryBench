import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_paper_result_audits as base
import run_paper_dual_review as reviewer
from structured_output import (transport_schema, preservation_errors, repair_invalid_output,
    normalize_bookkeeping, regroup_review_rows, bookkeeping_slots, apply_bookkeeping_patch,
    REPAIR_POLICY_VERSION)
from jsonschema import Draft202012Validator


def clean_result():
    return {"result_id":"theory_001", "audit_status":"assessed",
            "contract":{"quantified_domain":[],"assumptions":[],"conclusion":"C","statement_objects":[]},
            "lead_adjudications":[], "theorem_failure":{"status":"undetermined","statement_object_findings":[],"other_global_counterexamples":[]},
            "findings":{"proof_obligation":[],"inference":[],"calculation":[]},
            "dependencies":[],"result_impact_assessment":None,"open_questions":[]}


class SchemaTests(unittest.TestCase):
    def test_all_request_schemas(self):
        schemas = [*reviewer.schema_bundle(), base.read_json(ROOT/"schemas/paper_impact_output.schema.json"),
                   base.read_json(ROOT/"schemas/propagation_audit.schema.json")]
        for schema in schemas:
            original = copy.deepcopy(schema)
            wire = transport_schema(schema)
            Draft202012Validator.check_schema(wire)
            self.assertEqual(schema, original)
            self.assertNotIn('"oneOf"', json.dumps(wire))
            self.assertNotIn('"uniqueItems"', json.dumps(wire))
    def test_canonical_and_wire_accept_clean_result(self):
        schema = reviewer.schema_bundle()[0]
        for s in (schema, transport_schema(schema)):
            self.assertEqual(list(Draft202012Validator(s).iter_errors(clean_result())), [])
    def test_optional_property_is_rejected(self):
        with self.assertRaises(ValueError):
            transport_schema({"type":"object","properties":{"x":{"type":"string"}},"required":[],"additionalProperties":False})
    def test_overlapping_union_is_not_weakened(self):
        with self.assertRaises(ValueError):
            transport_schema({"oneOf":[{"type":"integer"},{"type":"number"}]})
    def test_unresolved_reference_rejected(self):
        with self.assertRaises(ValueError):
            transport_schema({"$ref":"other.json"})
    def test_initial_and_resume_enforce_schema(self):
        args = SimpleNamespace(codex_bin="codex", model="gpt-6-astra", reasoning_effort="high")
        for cmd in (base.initial_command(args,Path('/workspace'),Path('/output'),Path('/schema')),
                    base.resume_command(args,'session',Path('/output'),Path('/schema'))):
            self.assertEqual(cmd[cmd.index('--output-schema')+1], '/schema')
            self.assertEqual(cmd[-1], '-')
    def test_prompt_matches_indeterminate_driver_rule(self):
        self.assertIn('the driver must also be null', (ROOT/'prompts/result_node_audit_prompt.md').read_text())
        self.assertIn('`primary_driver_result_id` must also be null', (ROOT/'prompts/paper_impact_prompt.md').read_text())


class PreservationTests(unittest.TestCase):
    def setUp(self):
        self.before = clean_result()
        self.before['findings']['inference']=[{'finding_id':'theory_001::F1','error_statement':'E',
             'mathematical_reason':'M','repair_assessment':{'repair_difficulty_level':2,'selected_honest_repair':'R','level_rationale':'L'}}]
        self.before['result_impact_assessment']={'result_impact_level':None,'revised_result_summary':'S','impact_explanation':'I','primary_driver_finding_id':'theory_001::F1'}
    def test_null_driver_fix_allowed(self):
        after=copy.deepcopy(self.before);after['result_impact_assessment']['primary_driver_finding_id']=None
        self.assertEqual(preservation_errors(self.before,after),[])
    def test_regrading_blocked(self):
        after=copy.deepcopy(self.before);after['result_impact_assessment']['result_impact_level']=1
        self.assertTrue(preservation_errors(self.before,after))
    def test_removing_finding_blocked(self):
        after=copy.deepcopy(self.before);after['findings']['inference']=[]
        self.assertTrue(preservation_errors(self.before,after))
    def test_mathematical_reason_change_blocked(self):
        after=copy.deepcopy(self.before);after['findings']['inference'][0]['mathematical_reason']='different'
        self.assertTrue(preservation_errors(self.before,after))
    def test_repair_change_blocked(self):
        after=copy.deepcopy(self.before);after['findings']['inference'][0]['repair_assessment']['repair_difficulty_level']=1
        self.assertTrue(preservation_errors(self.before,after))
    def test_misplaced_group_can_move_without_math_change(self):
        after=copy.deepcopy(self.before);after['findings']['calculation']=after['findings'].pop('inference');after['findings']['inference']=[]
        self.assertEqual(preservation_errors(self.before,after),[])
    def test_reviewer_wrapper_guarded(self):
        after=copy.deepcopy(self.before);after['findings']['inference']=[]
        self.assertTrue(preservation_errors({'result_audit':self.before},{'result_audit':after}))
    def test_contract_change_blocked(self):
        after=copy.deepcopy(self.before);after['contract']['assumptions']=['new']
        self.assertTrue(preservation_errors(self.before,after))
    def test_missing_empty_failure_array_can_be_filled(self):
        old=copy.deepcopy(self.before);del old['theorem_failure']['other_global_counterexamples']
        self.assertEqual(preservation_errors(old,self.before),[])
    def test_reviewer_decision_change_blocked(self):
        old={'result_audit':self.before,'proposal_reviews':[{'candidate_ids':['A/F1'],'verdict':'retained','explanation':'E'}]}
        new=copy.deepcopy(old);new['proposal_reviews'][0]['verdict']='rejected'
        self.assertTrue(preservation_errors(old,new))
    def test_malformed_review_correction_does_not_crash_guard(self):
        old={'result_audit':self.before,'proposal_reviews':[]};new=copy.deepcopy(old);new['proposal_reviews']=None
        self.assertTrue(preservation_errors(old,new))
    def test_propagation_level_change_blocked(self):
        old={'downstream_assessments':[{'downstream_result_id':'T2','propagation_status':'proof_support_lost','propagated_result_impact_assessment':{'result_impact_level':3}}]}
        new=copy.deepcopy(old);new['downstream_assessments'][0]['propagated_result_impact_assessment']['result_impact_level']=1
        self.assertTrue(preservation_errors(old,new))


class ReviewMappingPreservationTests(unittest.TestCase):
    def setUp(self):
        self.group = {"candidate_ids": ["A/F1", "B/F1"], "verdict": "retained",
                      "final_ids": ["T::F1"], "explanation": "One root, merged.", "locations": []}
        self.duplicate = {"candidate_ids": ["B/F1"], "verdict": "retained",
                          "final_ids": ["T::F1"], "explanation": "Already grouped above.", "locations": []}
        self.old = {"result_audit": clean_result(),
                    "proposal_reviews": [copy.deepcopy(self.group), copy.deepcopy(self.duplicate)]}
        self.new = copy.deepcopy(self.old)
        self.new['proposal_reviews'].pop()

    def test_redundant_subset_row_can_be_removed(self):
        self.assertEqual(preservation_errors(self.old, self.new), [])

    def test_exact_duplicate_row_can_be_removed(self):
        self.old['proposal_reviews'][1] = copy.deepcopy(self.group)
        self.assertEqual(preservation_errors(self.old, self.new), [])

    def test_candidate_order_is_bookkeeping(self):
        self.new = copy.deepcopy(self.old)
        self.new['proposal_reviews'][0]['candidate_ids'].reverse()
        self.assertEqual(preservation_errors(self.old, self.new), [])

    def test_unique_candidate_cannot_be_removed(self):
        self.old['proposal_reviews'][1]['candidate_ids'] = ['B/F2']
        self.assertTrue(preservation_errors(self.old, self.new))

    def test_conflicting_verdict_cannot_be_deleted(self):
        self.old['proposal_reviews'][1]['verdict'] = 'rejected'
        self.old['proposal_reviews'][1]['final_ids'] = []
        self.assertTrue(preservation_errors(self.old, self.new))

    def test_distinct_target_cannot_be_deleted(self):
        self.old['proposal_reviews'][1]['final_ids'] = ['T::F2']
        self.assertTrue(preservation_errors(self.old, self.new))

    def test_cannot_retarget_to_make_row_redundant(self):
        self.old['proposal_reviews'][0]['final_ids'] = ['T::F2']
        self.assertTrue(preservation_errors(self.old, self.new))

    def test_surviving_explanation_stays_verbatim(self):
        self.new['proposal_reviews'][0]['explanation'] = 'A new argument.'
        self.assertTrue(preservation_errors(self.old, self.new))

    def test_dedup_exception_requires_unchanged_result_audit(self):
        self.new['result_audit']['open_questions'] = ['Changed interpretation.']
        self.assertTrue(preservation_errors(self.old, self.new))

    def test_no_new_grouping_in_dedup_exception(self):
        self.new['proposal_reviews'][0]['candidate_ids'] = ['A/F1']
        self.assertTrue(preservation_errors(self.old, self.new))

    def test_final_id_fix_keeps_existing_rationale(self):
        self.new = copy.deepcopy(self.old)
        self.new['proposal_reviews'][0]['final_ids'].append('T::F2')
        self.assertEqual(preservation_errors(self.old, self.new), [])

    def test_empty_review_lists_remain_valid(self):
        self.old['proposal_reviews'] = []
        self.new['proposal_reviews'] = []
        self.assertEqual(preservation_errors(self.old, self.new), [])


class RepairLoopTests(unittest.TestCase):
    def simulate(self, generated, initial=None, session_return='sid', timeout=False, validate_errors=None):
        tmp = tempfile.TemporaryDirectory();self.addCleanup(tmp.cleanup);root=Path(tmp.name)
        original=root/'001.json';original.write_text('{bad' if initial is None else json.dumps(initial))
        original_bytes=original.read_bytes(); calls=[]; checkpoints=[]
        def run(**kw):
            calls.append(kw)
            if timeout:raise subprocess.TimeoutExpired('fake',10)
            out=Path(kw['command'][kw['command'].index('--output-last-message')+1])
            value=generated[min(len(calls)-1,len(generated)-1)]
            out.write_text(json.dumps(value))
            return subprocess.CompletedProcess(kw['command'],0,stdout='events',stderr='')
        runtime=SimpleNamespace(utc_now=lambda:'2026-10-07T12:00:00Z',run_codex=run,resume_command=base.resume_command,
                                extract_event_metadata=lambda _:({'input_tokens':100+len(calls)*10,'output_tokens':10+len(calls)},session_return))
        def validate(path):
            return json.loads(path.read_text()),list(validate_errors or [])
        args=SimpleNamespace(codex_bin='codex',model='gpt-6-astra',reasoning_effort='high',timeout_seconds=10,max_output_repairs=2)
        turn={'usage':{'input_tokens':100,'output_tokens':10}}
        value,errors,path=repair_invalid_output(runtime=runtime,args=args,output_path=original,output=initial,
            errors=['original failed'],turn=turn,schema={'type':'object'},wire_schema_path=root/'schema.json',
            session_id='sid',environment={},workspace=root,validate=validate,checkpoint=lambda:checkpoints.append(copy.deepcopy(turn)))
        self.assertEqual(original.read_bytes(),original_bytes)
        self.assertTrue(checkpoints)
        return value,errors,path,turn,calls
    def test_success_keeps_raw_and_latest_cumulative_usage(self):
        value,errors,path,turn,calls=self.simulate([clean_result()])
        self.assertEqual(errors,[]);self.assertEqual(len(calls),1)
        self.assertIn('.repair_01.json',str(path));self.assertEqual(len(turn['output_attempts']),2)
        self.assertEqual(turn['usage']['input_tokens'],110)
        self.assertEqual(turn['repair_policy_version'], REPAIR_POLICY_VERSION)
    def test_two_attempt_cap(self):
        _,errors,_,turn,calls=self.simulate([clean_result()],validate_errors=['still invalid'])
        self.assertEqual(len(calls),2);self.assertTrue(errors);self.assertEqual(len(turn['output_attempts']),3)
        self.assertEqual(turn['usage']['input_tokens'],120)
    def test_session_mismatch_fails_closed(self):
        _,errors,_,turn,calls=self.simulate([clean_result()],session_return='another')
        self.assertEqual(len(calls),1);self.assertIn('persistent session',errors[0])
        self.assertEqual(turn['usage']['input_tokens'],100)
        self.assertEqual(turn['unmerged_correction_usage'][0]['usage']['input_tokens'],110)
    def test_timeout_keeps_original_usage(self):
        _,errors,_,turn,calls=self.simulate([clean_result()],timeout=True)
        self.assertEqual(len(calls),1);self.assertIn('timed out',errors[0]);self.assertEqual(turn['usage']['input_tokens'],100)
    def test_scientific_change_cannot_pass_validator_alone(self):
        old=clean_result();new=clean_result();new['audit_status']='rejected_missing_proof_source'
        _,errors,_,_,calls=self.simulate([new],initial=old)
        self.assertEqual(len(calls),2);self.assertIn('format repair changed audit_status',errors)


class BookkeepingTests(unittest.TestCase):
    def test_duplicate_ids_can_be_disambiguated_without_merging_claims(self):
        old=clean_result();old['findings']['inference']=[{'finding_id':'F','assessed_after_repairing':[],'error_statement':'E1'}, {'finding_id':'F','assessed_after_repairing':[],'error_statement':'E2'}]
        self.assertEqual(preservation_errors(old,old),[])
        new=copy.deepcopy(old);new['findings']['inference'][1]['finding_id']='F2'
        self.assertEqual(preservation_errors(old,new),[])
        self.assertIn('/findings/inference/1/finding_id',bookkeeping_slots(old))
        self.assertNotIn('/findings/inference/1/finding_id',bookkeeping_slots(new))
        new['findings']['inference'][1]['error_statement']='changed'
        self.assertTrue(preservation_errors(old,new))

    def test_unique_id_cannot_be_renamed(self):
        old=clean_result();old['findings']['inference']=[{'finding_id':'F','assessed_after_repairing':[],'error_statement':'E'}]
        new=copy.deepcopy(old);new['findings']['inference'][0]['finding_id']='G'
        self.assertTrue(preservation_errors(old,new))

    def test_upstream_order_reference_removed_only_when_dependency_preserved(self):
        old=clean_result();old['findings']['inference']=[{'finding_id':'F','assessed_after_repairing':['U','X']}]
        old['dependencies']=[{'upstream_finding_ids':['U']}]
        new,actions=normalize_bookkeeping(old)
        self.assertEqual(new['findings']['inference'][0]['assessed_after_repairing'],['X'])
        self.assertEqual(new['dependencies'],old['dependencies']);self.assertTrue(actions)
        self.assertEqual(old['findings']['inference'][0]['assessed_after_repairing'],['U','X'])
        self.assertEqual(preservation_errors(old,new),[])

    def test_local_cycles_not_arbitrarily_broken(self):
        old=clean_result();old['findings']['inference']=[{'finding_id':'F','assessed_after_repairing':['G']}, {'finding_id':'G','assessed_after_repairing':['F']}]
        new,actions=normalize_bookkeeping(old)
        self.assertEqual(new,old);self.assertEqual(actions,[])

    def test_statement_object_order_field_has_same_policy_as_other_findings(self):
        old=clean_result();old['theorem_failure']['statement_object_findings']=[{'finding_id':'F','assessed_after_repairing':['U'],'error_statement':'E','witness':{'reason':'R'}}]
        new=copy.deepcopy(old);new['theorem_failure']['statement_object_findings'][0]['assessed_after_repairing']=[]
        self.assertEqual(preservation_errors(old,new),[])
        new['theorem_failure']['statement_object_findings'][0]['witness']['reason']='changed'
        self.assertTrue(preservation_errors(old,new))

    def test_connected_bundled_review_groups_keep_all_claims(self):
        rows=[{'candidate_ids':[c],'final_ids':fs,'verdict':'retained','explanation':c+' rationale','locations':[]}
              for c,fs in [('A1',['F1']),('A2',['F2']),('B1',['F1','F2'])]]
        old={'result_audit':clean_result(),'proposal_reviews':rows}
        new=regroup_review_rows(old)
        self.assertEqual(len(new['proposal_reviews']),1)
        self.assertEqual(set(new['proposal_reviews'][0]['candidate_ids']),{'A1','A2','B1'})
        self.assertEqual(set(new['proposal_reviews'][0]['final_ids']),{'F1','F2'})
        for row in rows:self.assertIn(row['explanation'],new['proposal_reviews'][0]['explanation'])
        self.assertEqual(new['result_audit'],old['result_audit'])
        self.assertEqual(preservation_errors(old,new),[])
        new['proposal_reviews'][0]['explanation']+=' new science'
        self.assertTrue(preservation_errors(old,new))

    def test_conflicting_candidate_decision_not_normalized(self):
        rows=[{'candidate_ids':[c],'final_ids':fs,'verdict':v,'explanation':'R','locations':[]}
              for c,fs,v in [('A1',['F1'],'retained'),('B1',['F1'],'retained'),('A1',[],'rejected')]]
        old={'result_audit':clean_result(),'proposal_reviews':rows}
        self.assertEqual(regroup_review_rows(old),old)

    def test_only_allowed_patch_fields_can_change(self):
        old=clean_result();old['findings']['inference']=[{'finding_id':'F','assessed_after_repairing':['F'],'error_statement':'E'}]
        slots=bookkeeping_slots(old)
        path='/findings/inference/0/assessed_after_repairing'
        new=apply_bookkeeping_patch(old,{'edits':[{'path':path,'value_json':'[]'}],'unresolved_reason':''},slots)
        self.assertEqual(new['findings']['inference'][0]['error_statement'],'E')
        self.assertEqual(old['findings']['inference'][0]['assessed_after_repairing'],['F'])
        for forbidden in ('/findings/inference/0/error_statement','/findings/inference','/result_impact_assessment'):
            with self.assertRaises(ValueError):
                apply_bookkeeping_patch(old,{'edits':[{'path':forbidden,'value_json':'null'}],'unresolved_reason':''},slots)
        with self.assertRaises(ValueError):
            apply_bookkeeping_patch(old,{'edits':[{'path':path,'value_json':'[]'}]*2,'unresolved_reason':''},slots)


if __name__ == '__main__':unittest.main()
