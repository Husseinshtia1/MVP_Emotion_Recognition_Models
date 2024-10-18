
def store_secret(secret_name, secret_value):
    """Simulate storing a secret in a vault."""
    print(f"Storing {secret_name} in the vault.")
    return True

if __name__ == "__main__":
    store_secret("api_key", "12345")
