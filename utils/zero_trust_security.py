
def enforce_zero_trust(user_role):
    """Simulate zero trust security enforcement based on role."""
    if user_role not in ["admin", "analyst"]:
        return "Access Denied"
    return "Access Granted"

if __name__ == "__main__":
    print(enforce_zero_trust("admin"))
