
def fuse_modalities(text_data, audio_data):
    """Combine text and audio features for joint emotion analysis."""
    return {"fused_score": (len(text_data) + sum(audio_data)) / 2}

if __name__ == "__main__":
    print(fuse_modalities("happy", [0.5, 0.6, 0.7]))
