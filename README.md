# GPT-Genius: AI-Driven Python Code Generator and Analyzer

GPT-Genius is a versatile Python script that harnesses the power of GPT (Generative Pre-trained Transformer) technology to both generate Python code and analyze existing code for improvements. This comprehensive tool offers code generation, code analysis, and an interactive code editor, all powered by advanced AI capabilities.

## Project Introduction and Purpose

The purpose of this project is to provide developers with a tool that can generate Python code snippets for various programming tasks, analyze existing Python code files for potential improvements, and provide an interactive code editor for writing, editing, and testing Python code. All these functionalities are made possible by integrating OpenAI's GPT API.

## Installation Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage Guide with Examples

To use GPT-Genius, you need to instantiate the `GPTGenius` class with your OpenAI API key:

```python
from gpt_genius import GPTGenius

gpt_genius = GPTGenius("your-api-key")
```

### Code Generation

To generate Python code, use the `generate_code` method:

```python
prompt = "Write a function to calculate the factorial of a number"
code = gpt_genius.generate_code(prompt)
print(code)
```

### Code Analysis

To analyze Python code, use the `analyze_code` method:

```python
code = "def hello_world():\n    print('Hello, world!')"
analysis = gpt_genius.analyze_code(code)
print(analysis)
```

### Interactive Code Editor

To use the interactive code editor, use the `interactive_editor` method:

```python
gpt_genius.interactive_editor()
```

## Code Generation Features and Options

The `generate_code` method uses the OpenAI GPT API to generate Python code based on the provided prompt. The generated code is returned as a string.

## Code Analysis and Enhancement Capabilities

The `analyze_code` method uses the OpenAI GPT API to analyze the provided Python code. The analysis results are returned as a string.

## Interactive Code Editing

The `interactive_editor` method provides an interactive code editor where you can write, edit, and test Python code. The editor uses the `analyze_code` method to analyze the code you enter.

## How GPT-Genius Works

GPT-Genius uses the OpenAI GPT API to generate and analyze Python code. The API key for the OpenAI API is provided when creating an instance of the `GPTGenius` class.

## Acknowledgments and Credits

This project uses the OpenAI GPT API.

## Contribution Guidelines

If you want to contribute to this project, please submit a pull request.

## License Information

See the [LICENSE](LICENSE) file for license rights and limitations.
