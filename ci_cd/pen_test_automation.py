
import requests

def run_pen_test(url):
    """Basic penetration test for common vulnerabilities."""
    response = requests.get(url)
    if "X-Content-Type-Options" not in response.headers:
        print(f"Security Header Missing: X-Content-Type-Options at {url}")
    else:
        print(f"{url} passed basic security checks.")

if __name__ == "__main__":
    run_pen_test("http://example.com")
