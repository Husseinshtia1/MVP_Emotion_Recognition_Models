
import requests

def send_alert_to_security(platform_url, alert_data):
    response = requests.post(platform_url, json=alert_data)
    if response.status_code == 200:
        print("Alert sent successfully.")
    else:
        print(f"Failed to send alert. Status: {response.status_code}")
