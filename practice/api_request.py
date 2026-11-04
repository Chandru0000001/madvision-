import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users/1"

# Send API request
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# Convert response into JSON
data = response.json()

# Display response
print("Name:", data["name"])
print("Email:", data["email"])