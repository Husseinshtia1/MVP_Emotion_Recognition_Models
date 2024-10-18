
import requests

def send_alert_to_safety_system(alert_data):
    url = "https://safety-system.example/api/alerts"
    response = requests.post(url, json=alert_data)
    if response.status_code == 200:
        print("Alert sent successfully.")
    else:
        print(f"Failed to send alert: {response.status_code}")
