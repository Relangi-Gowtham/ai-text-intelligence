
# AI Text Intelligence

A modular Python text analysis application that processes
user-provided text, returns structured JSON results, and
persists analysis records using JSON Lines (JSONL).

The project is progressively evolving into an LLM-powered
text intelligence API.

## Current Features

- Word and character counting
- Uppercase and lowercase conversion
- Case-insensitive unique word counting
- Runtime input validation
- Exception handling
- Continuous command-line interaction
- Formatted JSON output
- Persistent analysis storage using JSONL
- Automated unit tests

## Technology Stack

- Python 3.12
- Python Standard Library (json)
- Conda
- Git and GitHub

## Architecture

The application follows a modular architecture with
separation of concerns.

- main.py: Application entry point, user interaction,
  output formatting, and exception handling.
- app/analyzer.py: Input validation and text analysis.
- app/storage.py: JSONL serialization and persistent storage.
- tests/test_analyzer.py: Automated unit tests.

## Project Structure

```text
ai-text-intelligence/
├── app/
│   ├── __init__.py
│   ├── analyzer.py
│   └── storage.py
├── tests/
│   ├── __init__.py
│   └── test_analyzer.py
├── main.py
├── README.md
└── .gitignore
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Relangi-Gowtham/ai-text-intelligence.git
cd ai-text-intelligence
```

### 2. Create a Python environment

```bash
conda create -n ai-text-intelligence python=3.12
conda activate ai-text-intelligence
```

No external Python packages are currently required.

### 3. Run the application

```bash
python main.py
```

Enter text to analyze. Type `exit` to terminate
the application.

## Example

Input:

```text
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

## Data Storage

Successful analysis results are appended to
`analysis_results.jsonl`.

Each line contains an independent JSON object.
Existing records are preserved across application sessions.

Analysis records contain original user-provided text and
are stored locally. The generated file is excluded from
version control.

## Testing

Run the automated analyzer tests:

```bash
python -m tests.test_analyzer
```

The current test suite includes seven unit tests:

- Word count
- Character count
- Unique word count
- Uppercase conversion
- Lowercase conversion
- Empty input validation
- Invalid data type validation

## Current Limitations

- Text analysis is rule-based.
- Word counting is based on whitespace.
- Punctuation is not normalized.
- Storage is local and file-based.
- Storage and CLI behavior are not yet covered by
  automated tests.
- LLM integration is not yet implemented.

## Roadmap

- [x] Basic Python text analysis
- [x] Modular application architecture
- [x] Input validation and exception handling
- [x] JSON serialization
- [x] Persistent JSONL storage
- [x] Basic automated unit testing
- [ ] REST API using FastAPI
- [ ] Request validation using Pydantic
- [ ] LLM integration
- [ ] Summarization and sentiment analysis
- [ ] Keyword extraction and classification
- [ ] Interactive user interface
- [ ] Docker and cloud deployment

## Project Status

Under active development.
