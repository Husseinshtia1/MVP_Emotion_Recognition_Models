
import numpy as np
import pandas as pd

def generate_synthetic_data(samples=1000, features=5):
    """
    Generates a synthetic dataset with emotion labels.
    """
    data = np.random.rand(samples, features)
    labels = np.random.choice(['happy', 'sad', 'angry', 'neutral'], size=samples)
    df = pd.DataFrame(data, columns=[f'feature_{{i}}' for i in range(features)])
    df['label'] = labels
    return df

if __name__ == "__main__":
    synthetic_df = generate_synthetic_data()
    print(synthetic_df.head())
