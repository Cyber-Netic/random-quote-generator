import requests

def get_random_quote():
    # API endpoint for random quotes
    API_URL = "https://api.quotable.io/random"

    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        print(f"Here’s a random quote for you:\n\n\"{data['content']}\" — {data['author']}")
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the quote:", e)

if __name__ == "__main__":
    print("Welcome to the Random Quote Generator!")
    get_random_quote()
