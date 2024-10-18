
def detect_voice_deception(audio_features):
    """Simple rule-based voice deception detection."""
    if audio_features.get("pitch_variation") > 0.7:
        return "Deception detected"
    return "No deception detected"

if __name__ == "__main__":
    sample_audio = {"pitch_variation": 0.8}
    print(detect_voice_deception(sample_audio))
