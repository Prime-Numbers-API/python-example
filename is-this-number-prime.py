import requests

apiKey = "123"
base_url = "http://api.prime-numbers.io"
number = "60309232769"
include_explanations = "true"
include_prime_types_list = "true"
language = "english"
full_url = base_url + "/is-this-number-prime.php?key=" + apiKey + "&number=" + number + "&include_explanations=" + include_explanations + "&include_prime_types_list=" + include_prime_types_list + "&language=" + language

response = requests.get(full_url)

print("response status code: " + str(response.status_code))
print("response: " + str(response.json()))
