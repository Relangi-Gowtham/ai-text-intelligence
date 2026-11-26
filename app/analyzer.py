def analyze_text(text: str) -> dict:
    """Analyze input text and return basic text statistics."""
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    if not text.strip():
        raise ValueError("Input text cannot be empty.")
    
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