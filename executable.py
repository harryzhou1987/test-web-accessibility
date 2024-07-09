"""Test the website accessibility for the list of the urls provided"""

import sys
import os
import requests
from datetime import datetime

# Collect Inputs
urls_string = sys.argv[1]
error_threshold = int(sys.argv[2])
urls = urls_string.split("\n")

# Dictionaries to store results
success = []
redirects = []
errors = []

# Function to categorize URL response
def check_url(url):
    try:
        response = requests.get(url)
        status_code = response.status_code
        if 200 <= status_code < 300:
            success.append(url)
        elif 300 <= status_code < 400:
            redirects.append(url)
        elif 400 <= status_code < 600:
            errors.append(url)
    except requests.exceptions.RequestException as e:
        errors.append(url)
        print(f"Request failed for {url}: {e}")

# Check each URL
for url in urls:
    check_url(url)

# Print results
print(f"Test Report - {datetime.now().date()}")
print(f"Success:{len(success)}, Redirects:{len(redirects)}, Errors:{len(errors)}")
print(f"\nSuccess:")
for url in success:
    print(f" - {url}")

print(f"\nRedirects:")
for url in redirects:
    print(f" - {url}")

print(f"\nErrors:")
for url in errors:
    print(f" - {url}")

# Check if the number of errors exceeds the threshold
if len(errors) > error_threshold:
    print(f"Number of errors ({len(errors)}) exceeded the threshold ({error_threshold}).")
    exit(1)

# Print Out Date as Output
now_str = datetime.now().isoformat()
os.system(f'echo "END_TIME={now_str}" >> $GITHUB_OUTPUT')
