
def detect_anomalies(data):
    """Simple anomaly detection based on thresholding."""
    threshold = 100
    anomalies = [x for x in data if x > threshold]
    return anomalies

if __name__ == "__main__":
    sample_data = [50, 120, 30, 200, 80]
    print(detect_anomalies(sample_data))
