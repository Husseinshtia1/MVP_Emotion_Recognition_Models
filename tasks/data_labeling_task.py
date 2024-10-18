
import json

def label_data(data):
    """Automatically label data with predefined rules."""
    labeled_data = [{"text": item, "label": "positive" if "good" in item else "negative"} for item in data]
    return labeled_data

if __name__ == "__main__":
    sample_data = ["This is good", "I dislike this"]
    print(json.dumps(label_data(sample_data), indent=2))
