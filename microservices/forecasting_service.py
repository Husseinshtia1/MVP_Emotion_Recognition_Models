
from flask import Flask, jsonify, request
from prophet import Prophet
import pandas as pd

app = Flask(__name__)

@app.route('/forecast', methods=['POST'])
def forecast():
    """Generate a forecast from time-series data."""
    data = request.get_json()
    df = pd.DataFrame(data)
    df.columns = ['ds', 'y']

    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)

    return jsonify(forecast[['ds', 'yhat']].to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
