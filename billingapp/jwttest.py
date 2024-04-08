import requests

# Define the URL
url = 'http://localhost:8000/api/token/'

# Define the payload (username and password)
data = {
    'username': 'Aradhya',
    'password': 'Alfa06094'
}

# Send a POST request to obtain the token
response = requests.post(url, json=data)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the token from the response JSON
    token_data = response.json()
    access_token = token_data['access']
    refresh_token = token_data['refresh']
    
    print("Access Token:", access_token)
    print("Refresh Token:", refresh_token)
else:
    print("Failed to obtain token. Status code:", response.status_code)
