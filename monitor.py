import requests
target_url="https://www.google.com"

print("Monitoring the target:", target_url)

try:
    response= requests.get(target_url)
    if response.status_code == 200:
        print("Target is up and running.")
    else:
        print("Target is down. Status code:", response.status_code)
except Exception as e:
    print("An error occurred while trying to reach the target:", str(e))