import json
import requests

def getlei():
    url = ""
    headers = {
        "User-Agent" : ""
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return
    return json.loads(resp.text)["country"]

if __name__ == '__main__':
    getlei()