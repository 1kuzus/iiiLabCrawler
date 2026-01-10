from urllib.parse import urlparse
from hashlib import md5
import requests
import time

FACEBOOK = "facebook"
INSTAGRAM = "instagram"
MUSIC163 = "yinyue"

key_old_api = "2HT8gjE3xL"
key_new_api = "6HTugjCXxR"


def get_resource_old_api(url, site):
    url_api = "https://service.iiilab.com/iiilab/extract"
    key = key_old_api
    timestamp = str(int(time.time() * 1000))
    sign = md5((url + site + timestamp + key).encode()).hexdigest()
    headers = {
        "G-Timestamp": timestamp,
        "G-Footer": sign,
    }
    data = {"url": url, "site": site}
    return requests.post(url_api, headers=headers, json=data)


def get_resource_new_api(url):
    url_api = "https://api.snapany.com/v1/extract"
    key = key_new_api
    timestamp = str(int(time.time() * 1000))
    accept_language = "en"
    sign = md5((url + accept_language + timestamp + key).encode()).hexdigest()
    headers = {
        "Accept-Language": accept_language,
        "G-Timestamp": timestamp,
        "G-Footer": sign,
    }
    data = {"link": url}
    return requests.post(url_api, headers=headers, json=data)


def get_resource(url, site=None):
    if site is not None:
        resp = get_resource_old_api(url, site)
    else:
        hostname = urlparse(url).hostname
        if "facebook.com" in hostname:
            resp = get_resource_old_api(url, FACEBOOK)
        elif "instagram.com" in hostname:
            resp = get_resource_old_api(url, INSTAGRAM)
        elif "music.163.com" in hostname:
            resp = get_resource_old_api(url, MUSIC163)
        else:
            resp = get_resource_new_api(url)

    if not resp.ok:
        print(f"[*] The request was unsuccessful.")
        print(f"    resp.status_code: {resp.status_code}")
        print(f"    resp.text: {resp.text}")
        return None
    else:
        return resp.json()
