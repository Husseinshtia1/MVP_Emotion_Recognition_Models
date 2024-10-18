
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/healthcare', methods=['GET'])
def healthcare_dashboard():
    return render_template('healthcare_dashboard.html', title="Healthcare Insights")

@app.route('/security', methods=['GET'])
def security_dashboard():
    return render_template('security_dashboard.html', title="Security Insights")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
