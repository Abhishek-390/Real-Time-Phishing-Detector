import requests
import json
import re
import os
import logging
from dotenv import load_dotenv
import time

# Load environment variables from the .env file
load_dotenv()

# Cache file path
CACHE_FILE = "url_cache.json"

# -----------------------
# Caching Functions
# -----------------------
def load_cache():
    """Load cache from a JSON file."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            return json.load(file)
    return {}

def save_cache(cache):
    """Save cache to a JSON file."""
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file)

# -----------------------
# Google Safe Browsing Check with Timeout, Retry, and Caching
# -----------------------
def check_google_safe_browsing(url: str, api_key: str) -> bool:
    """Check if the URL is flagged by Google Safe Browsing API."""
    cache = load_cache()

    # If the URL is in the cache, return the cached result
    if url in cache:
        logging.info(f"Cache hit for {url}")
        return cache[url]
    
    logging.info(f"Checking URL: {url}")
    endpoint = f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={api_key}"
    body = {
        "client": {"clientId": "your-app-name", "clientVersion": "1.0"},
        "threatInfo": {
            "threatTypes": ["MALWARE", "SOCIAL_ENGINEERING", "POTENTIALLY_HARMFUL_APPLICATION"],
            "platformTypes": ["ANY_PLATFORM"],
            "threatEntryTypes": ["URL"],
            "threatEntries": [{"url": url}]
        }
    }

    try:
        response = requests.post(endpoint, json=body, timeout=10)
        if response.status_code == 200:
            data = response.json()
            is_flagged = "matches" in data
            cache[url] = is_flagged
            save_cache(cache)
            logging.info(f"API result for {url}: {is_flagged}")
            return is_flagged
        else:
            logging.error(f"Error checking URL {url}: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Error with Safe Browsing API request for URL {url}: {e}")
        return False

def check_google_safe_browsing_with_retry(url: str, api_key: str, retries=3):
    """Retry checking Google Safe Browsing if the request fails."""
    for _ in range(retries):
        result = check_google_safe_browsing(url, api_key)
        if result is not None:
            return result
        logging.warning("Retrying...")
        time.sleep(2)  # Wait before retrying
    return False

# -----------------------
# Real-Time URL Checker
# -----------------------
def real_time_check(api_key):
    logging.info("\n🔍 Real-time Phishing URL Checker")
    while True:
        url = input("\nEnter a URL to check (or type 'exit' to quit): ").strip()

        if url.lower() == "exit":
            logging.info("Exiting real-time checker.")
            break

        # Clean and validate the URL
        if not re.match(r'https?://', url):
            url = 'http://' + url  # Add http:// if missing

        # Validate URL format
        if not re.match(r'https?://[A-Za-z0-9.-]+(?:\.[a-zA-Z]{2,})+', url):
            print(f"Invalid URL format: {url}. Please enter a valid URL.")
            continue

        # Check URL with Google Safe Browsing API
        is_flagged = check_google_safe_browsing_with_retry(url, api_key)
        verdict = "🚨 Phishing" if is_flagged else "✅ Legitimate"
        print(f"\nResult: {verdict} (Flagged by Google Safe Browsing: {is_flagged})")

# -----------------------
# Main function to start real-time checking
# -----------------------
if __name__ == "__main__":
    # Fetch API Key from environment variables
    api_key = os.getenv('GOOGLE_SAFE_BROWSING_API_KEY')

    if not api_key:
        logging.error("Error: API Key is missing. Please provide a valid API key from Google Safe Browsing.")
        exit(1)  # Stop the program if the API key is missing
    else:
        # Set up logging configuration
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Start real-time URL check
        real_time_check(api_key)
