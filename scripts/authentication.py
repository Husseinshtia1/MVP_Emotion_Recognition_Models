
def authenticate_user(username, password):
    """Authenticate user with given credentials."""
    return username == "admin" and password == "password123"

if __name__ == "__main__":
    print(authenticate_user("admin", "password123"))  # Should return True
