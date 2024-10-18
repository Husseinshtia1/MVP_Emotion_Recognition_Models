
import librosa
import numpy as np

def analyze_audio_emotion(audio_file):
    """Extract features from audio and classify emotion."""
    y, sr = librosa.load(audio_file)
    mfcc = np.mean(librosa.feature.mfcc(y=y, sr=sr).T, axis=0)
    return "happy" if np.mean(mfcc) > 0 else "neutral"

if __name__ == "__main__":
    print(analyze_audio_emotion('sample_audio.wav'))
