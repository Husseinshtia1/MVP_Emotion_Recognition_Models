
from flask import Flask, jsonify, request

app = Flask(__name__)

notebooks = {}

@app.route('/notebooks', methods=['GET'])
def list_notebooks():
    """List all shared notebooks."""
    return jsonify(notebooks)

@app.route('/notebooks', methods=['POST'])
def create_notebook():
    """Create a new shared notebook."""
    data = request.get_json()
    notebook_id = len(notebooks) + 1
    notebooks[notebook_id] = data
    return jsonify({'id': notebook_id, 'message': 'Notebook created successfully.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5007)
