
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load your pre-trained model (placeholder replaced with actual code)
model = tf.keras.models.load_model('models/emotion_model.h5')

@app.route('/predict', methods=['POST'])
def predict_emotion():
    try:
        data = request.json['data']
        prediction = model.predict(np.array([data]))
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
