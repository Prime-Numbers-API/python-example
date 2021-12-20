import requests

apiKey = "YOUR_API_KEY"
base_url = "http://api.prime-numbers.io"
number = "60309232769"
start = "69"
end = "200"
include_explanations = "true"
include_prime_types_list = "true"
language = "english"
full_url = base_url + "/get-all-primes-between-two-numbers.php?key=" + apiKey + "&include_explanations=" + include_explanations + "&include_prime_types_list=" + include_prime_types_list + "&language=" + language + "&start=" + start + "&end=" + end

response = requests.get(full_url)

print("response status code: " + str(response.status_code))
print("response: " + str(response.json()))
