
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/governance', methods=['GET'])
def governance():
    return jsonify({"message": "Governance policy applied."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)
