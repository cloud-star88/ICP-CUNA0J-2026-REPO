import requests

API_URL = "https://randomuser.me/api/"

def fetch_user():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()

        data = response.json()
        user = data["results"][0]

        first_name = user["name"]["first"]
        last_name = user["name"]["last"]
        email = user["email"]
        country = user["location"]["country"]

        print("User fetched successfully:")
        print(f"Name: {first_name} {last_name}")
        print(f"Email: {email}")
        print(f"Country: {country}")

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.ConnectionError:
        print("Error: Network problem. Check your internet connection.")
    except requests.exceptions.HTTPError:
        print("Error: Invalid response from the API.")
    except Exception as e:
        print("Unexpected error:", e)

fetch_user()
