import requests
from requests.adapters import HTTPAdapter

class MyAdapter(HTTPAdapter):
    def request_url(self, request, proxies):
        if request.url.startswith('https://'):
            url = request.url.replace('https://', 'http://', 1)
            print("Request URL: " + url)
        return request.url

s = requests.Session()
s.mount('https://', MyAdapter())
r = s.request(method="GET", url="https://baidu.com")
print("Status Code: " + str(r.status_code))
print("Response Content: " + r.text)
