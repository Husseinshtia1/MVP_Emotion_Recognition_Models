
def detect_advanced_deception(text_input):
    """Simulate NLP-based advanced deception detection."""
    keywords = ["lie", "false", "untruth"]
    if any(keyword in text_input.lower() for keyword in keywords):
        return "Advanced deception detected"
    return "No deception detected"

if __name__ == "__main__":
    print(detect_advanced_deception("This is a lie."))
