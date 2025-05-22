import requests
import execjs
import json

# 2-tuple:
#   ('hostPrefix' parameter of the function 'getAcceptPatch' in tool.js, subdomain of iiiLab.com)
# In most cases they are the same.
YOUTUBE=("youtube","youtube")
FACEBOOK=("facebook","facebook")
BILIBILI=("bilibili","bili")

def get_resource(url,SITE):
    with open("tool.js", "r") as f:
        jscode=f.read()
    tool_js=execjs.compile(jscode)
    enc_link=tool_js.eval(f"getEncLink('{url}')")
    accept_patch=tool_js.eval(f"getAcceptPatch('{SITE[0]}','{url}')")
    with requests.Session() as session:
        session.get(f"https://{SITE[0]}.iiilab.com/")
        resp=session.post(
            url=f"https://{SITE[1]}.iiilab.com/media",
            cookies={"lab0626":"1"},
            json={"link":enc_link},
            headers={"Accept-Patch":accept_patch}
        )
    if not resp.ok:
        print("The request was unsuccessful. Please check your network connection and try again.")
        return None
    else:
        try:
            dec_data=tool_js.eval(f"getDecData('{resp.json()['data']}')")
            dec_data=json.loads(dec_data)
        except Exception:
            print("An error occurred while parsing the returned data. Please check the request parameters or the response.")
            print("response message:",resp.json()["msg"])
            return None
        else:
            return dec_data
