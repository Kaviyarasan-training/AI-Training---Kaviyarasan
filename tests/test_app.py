import unittest

from app import build_prompt


class PromptBuilderTests(unittest.TestCase):
    def test_zero_shot_prompt_contains_email(self):
        email = "Hi team, please share the update."
        prompt = build_prompt(email, strategy="zero-shot")
        self.assertIn(email, prompt)
        self.assertIn("Reply:", prompt)

    def test_few_shot_prompt_contains_examples(self):
        email = "Could you send the report by Friday?"
        prompt = build_prompt(email, strategy="few-shot")
        self.assertIn("Example 1", prompt)
        self.assertIn("Example 2", prompt)
        self.assertIn(email, prompt)


if __name__ == "__main__":
    unittest.main()
