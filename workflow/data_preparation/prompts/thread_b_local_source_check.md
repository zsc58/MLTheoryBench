# Thread B Local Source Check

## Mission

Adjudicate one downstream objection by comparing the current source-audit records with the exact original statement and proof excerpts supplied by the runner. This is a correction turn in the existing Thread B session, not a new paper-wide source audit.

## Procedure

1. Check the objection against the current affected material records.
2. If those records are inaccurate or incomplete, use only the supplied excerpts to correct their recovered content, proof reconstruction, dependencies, statuses, findings, repairs, and precise source locations.
3. If the records are accurate and the objection is mathematically unfounded, preserve the source audit and return `objection_rejected`.
4. If the excerpts confirm a substantive source-level statement defect or theorem-critical proof gap, update the affected records to `major_issue` or `major_gap` and return `paper_issue_confirmed`.
5. Otherwise return `source_record_corrected` and a complete corrected source-audit object.

Do not silently strengthen assumptions, weaken conclusions, change material IDs or roles, change the frozen chain ranking, or inspect any part of the paper outside the supplied excerpts. Preserve the order and complete content of every unaffected material record exactly. If you assign `minor_issue` or `minor_error`, supply the corresponding complete repair object. Return only the JSON object required by the response schema.
