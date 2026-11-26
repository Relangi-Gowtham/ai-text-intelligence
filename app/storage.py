import json

def save_analysis(analysis: dict, filename: str) -> None:
    """Save an analysis result to a JSONL file."""
    with open(filename, "a", encoding="utf-8") as file:
       file.write(json.dumps(analysis) + "\n") 
