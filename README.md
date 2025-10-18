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
git clone https://github.com/yourusername/phish-detector.git
cd phish-detector
### 2. Install dependencies

Install all the necessary dependencies using pip:
