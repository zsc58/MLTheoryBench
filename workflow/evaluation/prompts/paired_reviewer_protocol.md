# Paired Validity Review Protocol

Apply the supplied single-answer validity-review instructions independently to every anonymized solver proof.

- Judge each answer only against the shared public task. Never use one answer to complete, repair, or reinterpret another answer.
- Do not rank the answers or adjust one judgment to create separation between models.
- Use the exact single-answer report fields and enum values for every answer.
- Preserve the supplied anonymous `answer_id` exactly. Model identities are intentionally hidden.
- If an answer gives a concrete reason that the target itself may be invalid, apply the original `target_suspected_invalid` standard. Ordinary proof errors remain `incomplete_major_gap` and do not challenge the task.

Return one envelope containing one independent report for every supplied answer. Do not add comparative prose.
