import requests
r = requests.request(method="GET", url="http://huggingface.co")
print("Status Code: " + str(r.status_code))
