
import requests

def send_pagerduty_alert(api_key, incident):
    """Send an alert to PagerDuty."""
    url = 'https://api.pagerduty.com/incidents'
    headers = {'Authorization': f'Token token={api_key}', 'Content-Type': 'application/json'}
    response = requests.post(url, json=incident, headers=headers)
    return response.status_code

if __name__ == "__main__":
    api_key = "your_pagerduty_api_key"
    incident = {"title": "Test Incident", "severity": "info"}
    print(send_pagerduty_alert(api_key, incident))
