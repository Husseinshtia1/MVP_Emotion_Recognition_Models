
import speech_recognition as sr
from transformers import pipeline

recognizer = sr.Recognizer()
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_conversation(audio_file_path):
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio)
    sentiment = sentiment_analyzer(text)[0]
    return {"transcription": text, "sentiment": sentiment}
