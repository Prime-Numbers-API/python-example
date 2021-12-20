import requests

apiKey = "YOUR_API_KEY"
base_url = "http://api.prime-numbers.io"
number = "60309232769"
minimum_combined_prime_gap = "200"
include_explanations = "true"
include_prime_types_list = "true"
language = "english"
full_url = base_url + "/get-isolated-random-prime.php?key=" + apiKey + "&include_explanations=" + include_explanations + "&include_prime_types_list=" + include_prime_types_list + "&language=" + language + "&minimum_combined_prime_gap=" + minimum_combined_prime_gap

response = requests.get(full_url)

print("response status code: " + str(response.status_code))
print("response: " + str(response.json()))
