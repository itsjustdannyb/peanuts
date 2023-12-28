import requests

api_url = "https://peanuts-api-production.up.railway.app/peanuter2000"

entry = input("prompt: ")

payload = {'prompt':entry}
# headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.post(api_url, params=payload)

if response.status_code == 200:
    print(response.status_code)
    response = response.json()['prayer']
    print(response)

else:
    error_message = f"Error: {response.status_code} - {response.text}"
    print(error_message)