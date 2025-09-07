import requests

try: 
	requests.get("https://www.google.com", timeout=5)
	print(" 😁👍 internet is working")
except requests.ConnectionError:
	print("😫🤞😶‍🌫️ no internet connection")
