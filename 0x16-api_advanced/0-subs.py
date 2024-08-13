import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    Returns 0 if an invalid subreddit is given.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; mybot/0.1)"}

    try:
        # Send the request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            # Return 0 if the status code is not 200
            return 0
    except requests.RequestException as e:
        # Handle any request exceptions (e.g., network issues)
        print(f"An error occurred: {e}")
        return 0

# Example usage:
if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    print(f"Number of subscribers: {number_of_subscribers(subreddit)}")

