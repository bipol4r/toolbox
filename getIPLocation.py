import json
import requests
import traceback

def getCountry(ip):
    url = "https://ip.leiue.com/?ip={}&chk=0&id=0".format(ip)
    # fake-useragent
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers)
    except Exception:
        print(traceback.format_exc())
    if resp.status_code != 200:
        return 0
    return json.loads(resp.text)["country"]


if __name__ == '__main__':
    print(getCountry('8.8.8.8'))