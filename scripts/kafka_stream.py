
from kafka import KafkaConsumer

def process_video_stream():
    consumer = KafkaConsumer('video-stream', bootstrap_servers=['localhost:9092'])
    for message in consumer:
        print(f'Processing frame from video stream: {message.value}')
