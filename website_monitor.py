import requests
import time

websites = [
    "https://google.com",
    "https://github.com",
    "https://thiswebsitedoesnotexist12345.com"
]

def check_website(url):

    try:
        start = time.time()

        response = requests.get(url, timeout=5)

        end = time.time()

        response_time = round(end - start, 2)

        if response.status_code == 200:
            print(f"✅ {url} is ONLINE ({response_time}s)")
        else:
            print(f"⚠️ {url} returned status {response.status_code}")

    except requests.exceptions.RequestException:
        print(f"❌ {url} is OFFLINE or unreachable")


print("\nChecking websites...\n")

for site in websites:
    check_website(site)

print("\nDone.\n")
