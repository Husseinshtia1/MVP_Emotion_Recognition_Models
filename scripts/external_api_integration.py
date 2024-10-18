
import requests

def get_data_from_api(api_url):
    """Fetch data from an external API."""
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data"}

if __name__ == "__main__":
    print(get_data_from_api("https://api.publicapis.org/entries"))
