from app.analyzer import analyze_text

def test_word_count() -> None:
    """Verify that word counting works correctly."""
    result = analyze_text("Hello AI")
    assert result["word_count"] == 2
    print("Word count test passed.")

def test_character_count() -> None:
    """Verify that character counting works correctly."""
    result = analyze_text("Python")
    assert result["character_count"] == 6
    print("Character count test passed.")

def test_unique_word_count() -> None:
    """Verify that unique word count works correctly."""
    result = analyze_text("AI ai AI")
    assert result["unique_word_count"] == 1
    print("Unique word count test passed.")

def test_uppercase() -> None:
    """Verify that text converted to uppercase correctly."""
    result = analyze_text("hello")
    assert result["uppercase_text"] == "HELLO"
    print("Uppercase test passed.")

def test_lowercase() -> None:
    """Verify that text converted to lowercase correctly."""
    result = analyze_text("HELLO")
    assert result["lowercase_text"] == "hello"
    print("Lowercase test passed.")

def test_empty_input() -> None:
    """Verify that empty input raises ValueError."""
    try:
        analyze_text("")
    except ValueError:
        print("Empty input test passed.")
    else:
        raise AssertionError("Expected ValueError")

def test_invalid_type() -> None:
    """Verify that invalid input raises TypeError."""
    try:
        analyze_text(123)
    except TypeError:
        print("Invalid type test passed.")
    else:
        raise AssertionError("Expected TypeError")
    
if __name__ == "__main__":
    test_word_count()
    test_character_count()
    test_unique_word_count()
    test_uppercase()
    test_lowercase()
    test_empty_input()
    test_invalid_type()
    print("\nAll 7 tests passed!")