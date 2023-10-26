import requests
from huggingface_hub import configure_http_backend
from huggingface_hub import hf_hub_download
from requests.adapters import HTTPAdapter

class MyAdapter(HTTPAdapter):
    def get_connection(self, url, proxies=None):
        if url.startswith('https://'):
            url = url.replace('https://', 'http://', 1)
        return super().get_connection(url, proxies)

# Create a factory function that returns a Session with configured proxies
def backend_factory() -> requests.Session:
    session = requests.Session()
    # session.mount('http://', MyAdapter())
    session.mount('https://', MyAdapter())
    return session

# Set it as the default session factory
configure_http_backend(backend_factory=backend_factory)

hf_hub_download(endpoint='http://huggingface.co', repo_id="timm/mobilenetv3_large_100.ra_in1k", filename="model.safetensors", proxies={'http': 'http://127.0.0.1:65001'})
