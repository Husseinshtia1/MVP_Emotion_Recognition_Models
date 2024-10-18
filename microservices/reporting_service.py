
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/report', methods=['GET'])
def generate_report():
    return jsonify({"report": "Monthly report generated."})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004)
