import requests

URL = "https://uselessfacts.jsph.pl/api/v2/facts/random"

def get_facts():
    response = requests.get(URL, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data["text"]

if __name__ == "__main__":
    try:
        for _ in range(3):
            print(get_facts())
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")