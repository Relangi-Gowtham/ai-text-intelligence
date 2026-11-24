
# AI Text Intelligence

A Python-based text analysis application that processes
user-provided text and returns structured text statistics.

This project is being developed progressively into an
AI-powered text intelligence API.

## Current Features

- Word count
- Character count
- Uppercase conversion
- Lowercase conversion
- Case-insensitive unique word count
- Structured dictionary output

## Technology Stack

- Python 3.12
- Conda
- Git and GitHub
- Visual Studio Code

## Getting Started

### 1. Create a Python environment

```bash
conda create -n ai-text-intelligence python=3.12
```

### 2. Activate the environment

```bash
conda activate ai-text-intelligence
```

### 3. Run the application

```bash
python main.py
```

No external Python packages are currently required.

## Example

Input:

```
AI is powerful and AI is useful
```

Output:

```json
{
    "original_text": "AI is powerful and AI is useful",
    "word_count": 7,
    "character_count": 31,
    "uppercase_text": "AI IS POWERFUL AND AI IS USEFUL",
    "lowercase_text": "ai is powerful and ai is useful",
    "unique_word_count": 5
}
```

The current program returns a Python dictionary.
The example above uses JSON formatting for readability.

## Project Structure

```
ai-text-intelligence/
├── main.py
├── README.md
└── .gitignore
```

## Current Limitations

- Text analysis is rule-based.
- Word counting is based on whitespace.
- Punctuation is not normalized.
- LLM integration is not yet implemented.

## Future Enhancements

- REST API using FastAPI
- Input validation using Pydantic
- LLM-powered text summarization
- Sentiment analysis
- Keyword extraction
- Text classification
- Automated testing
- Interactive user interface
- Application deployment

## Project Status

Under active development.
