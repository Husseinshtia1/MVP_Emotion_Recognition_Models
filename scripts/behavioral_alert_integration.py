
def linked_alerts(deepfake_detected, behavior_data):
    if deepfake_detected and behavior_data.get("aggression", 0) > 0.7:
        print("Critical Alert: Deepfake detected with aggressive behavior!")
