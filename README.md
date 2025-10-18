# Phishing URL Checker

This project is a Python-based tool that checks URLs in real-time to determine whether they are phishing or legitimate using the Google Safe Browsing API.

## Features

- **Real-time phishing detection**: Enter a URL, and the program checks if it's flagged as phishing or legitimate by the Google Safe Browsing API.
- **Caching**: URLs that have already been checked are cached to improve performance for subsequent checks.
- **Input Validation**: Automatically ensures URLs are in a valid format before checking.
- **Logging**: Keeps track of all activities (requests, errors, etc.) via logging for easier debugging and monitoring.
- **Retry Logic**: Retries API requests in case of network issues.

## Requirements

- **Python 3.x**: Make sure Python 3 is installed.
- **Google Safe Browsing API key**: You will need a Google Safe Browsing API key to use this tool.
- **Dependencies**: All necessary dependencies are listed in `requirements.txt`.

## Setup

### 1. Clone the repository

```bash
[git clone https://github.com/yourusername/phish-detector.git](https://github.com/Abhishek-390/Real-Time-Phishing-Detector.git)
cd phish-detector
```
### 2. Install dependencies

Install all the necessary dependencies using pip:
```bash
pip install -r requirements.txt
```
### 3. Get Google Safe Browsing API Key

You’ll need to obtain a Google Safe Browsing API key. Here’s how to get it:

1. Go to the Google Cloud Console
2. Create a new project or select an existing one.
3. Enable the Google Safe Browsing API.
4. Create an API key for the project.

### 4. Set up environment variables

Create a .env file in the project directory and add your Google Safe Browsing API key:
```plaintext
GOOGLE_SAFE_BROWSING_API_KEY=your_api_key_here
```
### 5. Run the script

Once everything is set up, run the script:
```bash
python phishing_detector.py
```
You will be prompted to enter a URL to check. The script will return whether the URL is flagged as phishing or legitimate by Google Safe Browsing.
##Usage

The script checks if a URL is flagged as phishing by querying the Google Safe Browsing API. It will print out whether the URL is Phishing or Legitimate based on the result from the API.
