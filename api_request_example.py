import requests

response = requests.get("https://dog.ceo/api/breeds/image/random")

print("response status code: " + str(response.status_code))
print("response: " + str(response.json()))
