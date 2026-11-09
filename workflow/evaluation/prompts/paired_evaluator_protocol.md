# Paired Reference Evaluation Protocol

Apply the supplied single-answer reference-scoring instructions independently to every anonymized solver proof and its matching validity report.

- Use the same shared public task, ground-truth proof, rubric, and provenance for every answer.
- Never transfer proof content, findings, or earned credit from one answer to another.
- Do not rank the answers or adjust scores to create separation between models.
- Use the exact single-answer evaluation fields and enum values for every answer.
- Preserve each supplied anonymous `answer_id` exactly. Model identities are intentionally hidden.

Return one envelope containing one independent evaluation for every supplied answer. Do not add comparative prose.
