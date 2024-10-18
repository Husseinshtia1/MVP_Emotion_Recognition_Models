
def behavioral_alerts(behavior_data):
    # Detect abnormal behavior patterns
    if behavior_data.get('aggression', 0) > 0.7:
        print("Alert: Aggressive behavior detected!")
    if behavior_data.get('stress', 0) > 0.8:
        print("Alert: High stress levels detected!")
