#!/usr/bin/env python3
"""Validate public downloads and exact finite witnesses; does NOT run Lean or a judge."""
from __future__ import annotations
import hashlib
import json
import zipfile
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / 'research/source_pilot_20260908'

CASES = [
    ('A01','ai4slt','01_basic_inequality.md','LeastSquares.basic_inequality','reference_and_controlled_variants','exact_contract'),
    ('A02','ai4slt','02_two_sided_tail.md','subGaussian_tail_bound','reference_and_controlled_variants','fixed_increment_form'),
    ('A03','ai4slt','03_local_mgf_domain.md','bernstein_one_sided_of_cgf_bound','reference_and_controlled_variants','source_contract'),
    ('R01','rlmeval','01_identical_distributions.md','ProbabilityTheory.bayesBinaryRisk_self','reference_and_controlled_variants','finite_probability_specialization'),
    ('R02','rlmeval','02_data_processing.md','ProbabilityTheory.bayesBinaryRisk_le_bayesBinaryRisk_comp','reference_and_controlled_variants','finite_probability_specialization'),
    ('R03','rlmeval','03_reference_quarantine.md','ProbabilityTheory.statInfo_eq_abs_add_lintegral_abs','reference_quarantine','unfinished_lean_reference'),
    ('M01','arxiv_math_grading','01_convex_hull_gap.md','2302.08300v1:Lemma6.1','revision_pair_review','local_normalization_required'),
    ('M02','arxiv_math_grading','02_weighted_cycle_contract.md','2502.10890v1:Lemma20','revision_pair_review','revised_contract_is_narrower'),
    ('M03','arxiv_math_grading','03_withdrawal_is_not_repair.md','2501.13445v2:Theorem5','version_admission_exclusion','withdrawn_without_corrected_proof'),
]

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    records=[]
    for meta in sorted(SNAPSHOT.rglob('*.provenance.json')):
        d=json.loads(meta.read_text());p=meta.with_name(meta.name.removesuffix('.provenance.json'))
        assert p.is_file() and sha(p)==d['sha256'],p
        records.append({'path':str(p.relative_to(ROOT)),'sha256':d['sha256'],'bytes':p.stat().st_size})
    full=json.loads((SNAPSHOT/'arxiv_math_grading/raw/full_rows.json').read_text())
    rows=[r['row'] for r in full['rows']]
    assert len(rows)==full['num_rows_total']==100
    assert all(not r['truncated_cells'] for r in full['rows'])
    assert len({r['arxiv_id'] for r in rows})==100
    old=[json.loads(l) for l in (SNAPSHOT/'arxiv_math_grading/raw/arxiv_grading_bench.jsonl').read_text().splitlines()]
    assert len(old)==35
    assert {r['arxiv_id'] for r in old}=={r['arxiv_id'] for r in rows if r['benchmark_version']==1}
    a=json.loads((SNAPSHOT/'ai4slt/raw/novel_test_first1.json').read_text())
    assert len(a['rows'])==1 and not a['rows'][0]['truncated_cells']
    assert a['num_rows_total']==173
    # Full task assumptions for the scalar least-squares counterexample.
    sigma=F(1);w=F(1);fstar=F(0);fhat=F(2);candidate_class=[F(0),F(2)]
    y=fstar+sigma*w;delta=fhat-fstar
    assert sigma>0 and fstar in candidate_class and fhat in candidate_class
    assert all((y-fhat)**2<=(y-f)**2 for f in candidate_class)
    assert delta**2<=2*sigma*w*delta and not delta**2<=sigma*w*delta
    assert (y-fhat)*delta!=0
    # Finite probability checks; sub-Gaussian admission additionally uses the
    # analytic Hoeffding bound explained in A02, not this arithmetic check.
    atoms=[(F(1),F(2,3)),(F(-2),F(1,3))];u=F(3,2)
    assert sum(p for _,p in atoms)==1 and sum(y*p for y,p in atoms)==0
    pplus=sum(p for y,p in atoms if y>=u);pabs=sum(p for y,p in atoms if abs(y)>=u)
    assert pplus==0 and pabs==F(1,3)
    # Local MGF parameter violation and exact exponent ordering in A03.
    t=F(2);C=v=b=F(1);l=t/(2*C*v);cap=1/(2*C*b)
    assert l==1 and l>cap
    assert F(6)<F(25,4) # exp(-6) > exp(-25/4), by strict monotonicity.
    # Identical data with equal priors: all randomized constant decisions fail half the time.
    for q in [F(0),F(1,4),F(1,2),F(1)]: assert q/2+(1-q)/2==F(1,2)
    # Two distinguishable atoms vs. the common discard kernel, under equal priors.
    raw_best=min((q0+1-q1)/2 for q0 in [F(0),F(1)] for q1 in [F(0),F(1)])
    discarded_best=min((q+1-q)/2 for q in [F(0),F(1)])
    assert raw_best==0 and discarded_best==F(1,2)
    assert (1-F(1,2))**2==F(1,4)<F(1,2)
    index=[]
    for cid,source,file,target,kind,relation in CASES:
        p=ROOT/'cases'/source/file;assert p.is_file()
        index.append({'case_id':cid,'source':source,'card_path':str(p.relative_to(ROOT)),
            'card_sha256':sha(p),'target':target,'case_kind':kind,'contract_relation':relation,
            'ground_truth_admitted':False,'lean_locally_verified':False,
            'judge_run':False,'independent_human_score_adjudication':False})
    result={'scope':'public_source_feasibility_pilot_not_a_judge_accuracy_experiment',
        'source_assets':records,'case_cards':index,
        'counts':{'ai4slt_hf_rows_downloaded':1,'ai4slt_hf_test_split_rows':173,
          'arxiv_legacy_rows':len(old),'arxiv_current_rows':len(rows),
          'arxiv_benchmark_versions':dict(Counter(r['benchmark_version'] for r in rows)),
          'rlmeval_original_model_failures_obtained':0,'cards':len(index),
          'by_card_kind':dict(Counter(c['case_kind'] for c in index)),
          'lean_locally_verified':0,'formal_gold_admitted':0,'judge_calls':0},
        'checks':{'download_hashes':'passed','arxiv_35_vs_100_reconciliation':'passed',
          'finite_rational_witness_arithmetic':'passed',
          'witness_scope':'Arithmetic checks do not certify analytic hypotheses or original Lean dependencies.'},
        'commits':{
          'ai4slt_source':zipfile.ZipFile(SNAPSHOT/'ai4slt/raw/source.zip').comment.decode(),
          'rlmeval_harness':zipfile.ZipFile(SNAPSHOT/'rlmeval/raw/source_main.zip').comment.decode(),
          'testing_lower_bounds':zipfile.ZipFile(SNAPSHOT/'rlmeval/raw/testing_lower_bounds.zip').comment.decode()}}
    out=SNAPSHOT/'pilot_index.json';out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'index':str(out),'counts':result['counts'],'checks':result['checks']},ensure_ascii=False))

if __name__=='__main__':main()
