import requests

# A dictionary of platforms and their username URLs
SOCIAL_MEDIA_URLS = {
    "Twitter": "https://twitter.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Facebook": "https://www.facebook.com/{}",
    "GitHub": "https://github.com/{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Reddit": "https://www.reddit.com/user/{}",
}

def check_username(platform, username):
    url = SOCIAL_MEDIA_URLS[platform].format(username)
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"[+] {platform}: Username '{username}' exists at {url}"
        elif response.status_code == 404:
            return f"[-] {platform}: Username '{username}' is available."
        else:
            return f"[!] {platform}: Unexpected response for '{username}' (status code: {response.status_code})."
    except requests.RequestException as e:
        return f"[!] {platform}: Error checking username '{username}' ({e})."

def search_username(username):
    print(f"Searching for username '{username}' across platforms...\n")
    results = []
    for platform in SOCIAL_MEDIA_URLS:
        result = check_username(platform, username)
        results.append(result)
        print(result)
    return results

# Example Usage
if __name__ == "__main__":
    # Prompt the user for input with a default value
    username = input("Enter the username to search (default: 'shilpasayura'): ") or "shilpasayura"
    # Output the result for testing
    print(f"Searching for username: {username}")

    search_username(username)
