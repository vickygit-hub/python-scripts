import requests
import time

url = "https://www.google.com"

try: 
	start = time.time()
	response = requests.get(url, timeout=5)
	end = time.time()
	elapsed = round((end - start) * 1000, 2)

	print("👍 internet is working")
	print(f"Status Code: {response.status_code}")
	print(f"Response Time: {elapsed} ms")

except requests.ConnectionError:
	print("😫🤞😶‍🌫️ no internet connection")
