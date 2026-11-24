def analyze_text(text: str) -> dict:
    """Analyze input text and return basic text statistics."""
    words = text.split()
    lower_text = text.lower()
    result = {
        "original_text": text,
        "word_count": len(words),
        "character_count": len(text),
        "uppercase_text": text.upper(),
        "lowercase_text": lower_text,
        "unique_word_count": len(set(lower_text.split()))
    }
    return result

if __name__ == "__main__":
    print("Welcome to AI Text Intelligence")
    user_text = input("Enter text to analyze: ")
    analysis = analyze_text(user_text)

    print(analysis)