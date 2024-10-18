
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('index.html')

@app.route('/analytics')
def analytics():
    """Return a sample analytics report."""
    sample_report = {"summary": "Analytics Dashboard", "data": {"happy": 70, "sad": 20, "angry": 10}}
    return jsonify(sample_report)

@app.route('/alerts', methods=['POST'])
def send_alert():
    """Receive alert data and send an alert."""
    alert_data = request.json
    print(f"Alert Received: {alert_data}")
    return jsonify({"status": "Alert Sent", "data": alert_data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
