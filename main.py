import json

from app.analyzer import analyze_text
from app.storage import save_analysis

EXIT_COMMAND = "exit"
OUTPUT_FILE = "analysis_results.jsonl"
JSON_INDENT = 4

def main() -> None:
    """Run the text intelligence application."""

    print("Welcome to AI Text Intelligence")
    print("Type 'exit' to quit")
    while True:
        user_text = input("Enter text to analyze: ")

        if user_text.strip().lower() == EXIT_COMMAND:
            print("Thank You for using AI Text Intelligence!")
            break
        try:
            analysis = analyze_text(user_text)
            analysis_json = json.dumps(analysis, indent=JSON_INDENT)
            save_analysis(analysis, OUTPUT_FILE)
            print(analysis_json)
        except (ValueError, TypeError) as error:
            print(f"Error: {error}")
        except OSError as error:
            print(f"Storage error: {error}")    


if __name__ == "__main__":
    main()