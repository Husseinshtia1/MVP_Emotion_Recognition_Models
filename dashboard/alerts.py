
def send_alert(alert_data):
    """Send an alert based on the provided data."""
    print(f"Alert sent: {alert_data}")

if __name__ == "__main__":
    send_alert({"type": "warning", "message": "High CPU usage detected."})
