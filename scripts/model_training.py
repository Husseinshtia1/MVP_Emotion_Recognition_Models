
from sklearn.linear_model import LogisticRegression

def train_model(X, y):
    """Train a logistic regression model."""
    model = LogisticRegression()
    model.fit(X, y)
    return model

if __name__ == "__main__":
    from sklearn.datasets import load_iris
    iris = load_iris()
    model = train_model(iris.data, iris.target)
    print(f"Model trained: {model}")
