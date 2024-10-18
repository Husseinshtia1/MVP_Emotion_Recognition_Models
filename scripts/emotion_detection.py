
def detect_emotion(text):
    """Detect emotion from text input."""
    emotions = {
        "happy": ["joy", "excited", "cheerful"],
        "sad": ["down", "blue", "miserable"],
        "angry": ["mad", "furious", "irritated"]
    }
    for emotion, keywords in emotions.items():
        if any(keyword in text.lower() for keyword in keywords):
            return emotion
    return "neutral"

if __name__ == "__main__":
    sample_text = "I feel so joyful today!"
    print(f"Detected emotion: {detect_emotion(sample_text)}")
