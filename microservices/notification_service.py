
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/notify', methods=['POST'])
def notify():
    return jsonify({"message": "Notification sent!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
