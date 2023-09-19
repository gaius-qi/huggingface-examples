from huggingface_hub import snapshot_download
snapshot_download(endpoint="http://huggingface.co", repo_id="gaius-qi/dragonfly", proxies={'http': 'http://127.0.0.1:65001'})
