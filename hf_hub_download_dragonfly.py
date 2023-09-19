from huggingface_hub import hf_hub_download
hf_hub_download(endpoint="http://huggingface.co", repo_id="gaius-qi/dragonfly", filename="README.md", proxies={'http': 'http://127.0.0.1:65001'})
