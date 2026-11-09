import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from test_structured_output import ROOT, clean_result


class RunnerIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.fake=self.root/'fake_codex';shutil.copy2(ROOT/'tests/fake_codex.py',self.fake);self.fake.chmod(0o700)
        self.source=self.root/'source.md';self.source.write_text('Synthetic offline integration fixture. C follows immediately.\n')
        self.audit=self.root/'audit.json'
        self.audit.write_text(json.dumps({'material_records':[
            {'item_id':f'theory_00{i}','role':'theory_candidate','statement_status':'major_issue','proof_status':'major_gap','depends_on':[],
             'source_spans':[f'Theorem {i}'], 'proof_source_locations':[f'Proof of Theorem {i}']}
            for i in (1,2)]}))
        self.results=[]
        for i in (1,2):
            x=clean_result();x['result_id']=f'theory_00{i}';self.results.append(x)
        self.summary={'paper_impact_assessment':None,'paper_open_questions':[]}
    def invoke(self,script,extra,values,name):
        responses=self.root/f'{name}_responses.json';responses.write_text(json.dumps(values))
        state=self.root/f'{name}_state'
        env={**os.environ,'TAXONOMY_TEST_RESPONSES':str(responses),'TAXONOMY_TEST_STATE':str(state),'PYTHONDONTWRITEBYTECODE':'1'}
        runs=self.root/name
        cmd=[sys.executable,'-B',str(ROOT/'scripts'/script),'--runs-root',str(runs),
             '--codex-bin',str(self.fake),'--model','gpt-6-astra','--max-output-repairs','2',*extra]
        result=subprocess.run(cmd,env=env,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stdout+result.stderr)
        run=next(runs.iterdir());manifest=json.loads((run/'manifest.json').read_text())
        self.assertEqual(manifest['status'],'completed')
        self.assertEqual(manifest['usage'],{'input_tokens':400,'output_tokens':40})
        self.assertEqual(len(manifest['turns']),3)
        self.assertEqual(state.read_text(),'4')
        return run,manifest
    def audited(self):
        return self.invoke('run_paper_result_audits.py',
            ['--paper-id','paper_2026_001','--theory-topic','synthetic_test','--source-file',str(self.source),'--turn3-audit',str(self.audit)],
            ['{bad',self.results[0],self.results[1],self.summary],'audit_runs')
    def test_audit_repairs_then_continues_node_and_summary(self):
        run,m=self.audited()
        self.assertEqual(len(m['turns'][0]['output_attempts']),2)
        self.assertEqual((run/'outputs/001_theory_001.json').read_text(),'{bad')
        self.assertEqual(json.loads((run/'paper_audit.json').read_text())['result_audits'],self.results)
        self.assertEqual(m['turns'][0]['usage']['input_tokens'],200)
    def test_reviewer_repairs_then_continues_summary(self):
        audited,_=self.audited();inputs=self.root/'review_inputs';inputs.mkdir()
        for arm in ('a','b'):shutil.copy2(audited/'paper_audit.json',inputs/f'audit_{arm}.json')
        shutil.copy2(self.audit,inputs/'turn3_source_audit.json')
        wrappers=[{'result_audit':r,'proposal_reviews':[]} for r in self.results]
        broken=copy.deepcopy(wrappers[1]);del broken['result_audit']['findings']['calculation']
        run,m=self.invoke('run_paper_dual_review.py',['--inputs',str(inputs),'--source-file',str(self.source)],
            [wrappers[0],broken,wrappers[1],self.summary],'review_runs')
        self.assertEqual(len(m['turns'][1]['output_attempts']),2)
        self.assertEqual(json.loads((run/'paper_audit.json').read_text())['result_audits'],self.results)


if __name__=='__main__':unittest.main()
