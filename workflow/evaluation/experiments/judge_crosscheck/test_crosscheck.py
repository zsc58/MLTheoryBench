import unittest
from run_crosscheck import metrics, parse_json, stratified_sample, reduced_output_budget


class CrosscheckTests(unittest.TestCase):
    def test_stratification_is_reproducible(self):
        eligible = {f'PRC{i}': [f'paper_{i}_{j:03}' for j in range(20 if i < 4 else 6)] for i in range(5)}
        a = stratified_sample(eligible)
        b = stratified_sample({key: list(reversed(val)) for key, val in eligible.items()})
        self.assertEqual(a, b)
        self.assertEqual([len(a[f'PRC{i}']) for i in range(5)], [10, 10, 10, 10, 6])
        self.assertEqual(len({p for ids in a.values() for p in ids}), 46)

    def test_no_replacement_when_stratum_too_small(self):
        with self.assertRaises(ValueError):
            stratified_sample({f'PRC{i}': ['only_one'] for i in range(5)})

    def test_json_unwrap_only(self):
        self.assertEqual(parse_json('```json\n{"score":0}\n```'), {'score': 0})
        with self.assertRaises(ValueError):
            parse_json('')
        with self.assertRaises(ValueError):
            parse_json('[]')

    def test_zero_scores_are_retained(self):
        m = metrics([(0, 0), (10, 8), (8, 5)])
        self.assertEqual(m['n'], 3)
        self.assertEqual(m['gpt_judge_mean'], 6)
        self.assertEqual(m['new_ge8_rate'], 1/3)
        self.assertAlmostEqual(m['mean_delta'], -5/3)

    def test_context_budget_uses_reported_input_without_truncation(self):
        message = ('provider returned HTTP 400: accepts at most 262144 combined input and output tokens. '
                   'your request has 149343 input tokens and asks for 131072 output tokens')
        self.assertEqual(reduced_output_budget(message, 131072), 111777)
        self.assertIsNone(reduced_output_budget('HTTP 429 rate limit', 131072))
        self.assertIsNone(reduced_output_budget(message.replace('149343', '261000'), 131072))
        self.assertIsNone(reduced_output_budget(message, 48000))


if __name__ == '__main__':
    unittest.main()
