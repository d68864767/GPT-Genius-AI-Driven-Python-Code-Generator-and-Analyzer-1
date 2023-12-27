```python
import unittest
from gpt_genius import GPTGenius

class TestGPTGenius(unittest.TestCase):
    def setUp(self):
        self.gpt_genius = GPTGenius("your-api-key")

    def test_generate_code(self):
        prompt = "Write a function to calculate the factorial of a number"
        code = self.gpt_genius.generate_code(prompt)
        self.assertIsNotNone(code)
        self.assertTrue("factorial" in code)

    def test_analyze_code(self):
        code = "def hello_world():\n    print('Hello, world!')"
        analysis = self.gpt_genius.analyze_code(code)
        self.assertEqual(analysis, "This code looks good!")

    def test_interactive_editor(self):
        # This test is a bit tricky as it involves user input and output.
        # You might need to use mocking to simulate user input and output.
        # For now, we'll just check that the method exists and is callable.
        self.assertTrue(callable(self.gpt_genius.interactive_editor))

if __name__ == "__main__":
    unittest.main()
```
