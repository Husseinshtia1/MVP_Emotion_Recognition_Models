
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def analyze_emotion():
    data = request.json.get('text', '')
    # Example: Mock emotion analysis logic
    emotion = "happy" if "good" in data.lower() else "neutral"
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
