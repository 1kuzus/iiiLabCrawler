import requests
import time
from hashlib import md5

# (is_using_new_api, s1)
TIKTOK = (True, "en")
YOUTUBE = (True, "en")
BILIBILI = (True, "zh")
FACEBOOK = (False, "facebook")
INSTAGRAM = (False, "instagram")
TWITTER = (False, "twitter")

# new API:
# s1 = "en" / "zh" / "ja" / "es" (Accept-Language)
# key = "6HTugjCXxR"
# url_api = "https://api.snapany.com/v1/extract"

# old API:
# s1 = "facebook" / "instagram" / ... (subdomain)
# key = "2HT8gjE3xL"
# url_api = "https://{s1}.iiilab.com/api/extract"
key_new_api = "6HTugjCXxR"
key_old_api = "2HT8gjE3xL"


def get_resource(url, SITE):
    is_using_new_api, s1 = SITE
    timestamp = str(int(time.time() * 1000))
    key = key_new_api if is_using_new_api else key_old_api
    sign = md5((url + s1 + timestamp + key).encode()).hexdigest()
    headers = {
        "G-Timestamp": timestamp,
        "G-Footer": sign,
    }
    data = {
        "link": url,
    }

    if is_using_new_api:
        url_api = "https://api.snapany.com/v1/extract"
        headers["Accept-Language"] = s1
    else:
        url_api = f"https://{s1}.iiilab.com/api/extract"
        data["site"] = s1

    resp = requests.post(url_api, headers=headers, json=data)

    if not resp.ok:
        print(f"[*] The request was unsuccessful.")
        print(f"[*] resp.status_code: {resp.status_code}")
        print(f"[*] resp.text: {resp.text}")
        return None
    else:
        return resp.json()
