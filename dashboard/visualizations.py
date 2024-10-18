
import matplotlib.pyplot as plt

def plot_emotion_distribution(emotion_data):
    """Plot a pie chart of emotion distribution."""
    labels = emotion_data.keys()
    sizes = emotion_data.values()

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Emotion Distribution')
    plt.show()

if __name__ == "__main__":
    sample_data = {"happy": 50, "sad": 20, "angry": 15, "neutral": 15}
    plot_emotion_distribution(sample_data)
