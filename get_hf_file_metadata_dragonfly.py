import requests
from huggingface_hub import get_hf_file_metadata

http_url = "http://huggingface.co/gaius-qi/dragonfly/resolve/main/README.md"
https_url = "http://huggingface.co/gaius-qi/dragonfly/resolve/main/README.md"
proxies = {"https": "http://127.0.0.1:65001", "http": "http://127.0.0.1:65001"}

get_hf_file_metadata(http_url, proxies=proxies)
get_hf_file_metadata(https_url, proxies=proxies)
requests.head(http_url, proxies=proxies)
requests.head(https_url, proxies=proxies)
