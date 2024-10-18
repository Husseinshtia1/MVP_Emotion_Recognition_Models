
import pandas as pd

def preprocess_data(data):
    """Basic preprocessing: remove NaNs and normalize data."""
    data = data.dropna()
    return (data - data.mean()) / data.std()

if __name__ == "__main__":
    df = pd.DataFrame({'scores': [1, 2, None, 4, 5]})
    print(preprocess_data(df))
