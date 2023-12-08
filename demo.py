from iiilab import get_resource,YOUTUBE,FACEBOOK,BILIBILI
import json

# youtube video
url_yt="https://www.youtube.com/watch?v=MtOXxlUE2Zg"
res_yt=get_resource(url_yt,YOUTUBE)
print(json.dumps(res_yt,indent=4))

# facebook video
url_fb="https://www.facebook.com/100094681485185/videos/815409647254080"
res_fb=get_resource(url_fb,FACEBOOK)
print(json.dumps(res_fb,indent=4))

# bilibili video
url_bili="https://www.bilibili.com/video/BV1bg4y137R6"
res_bili=get_resource(url_bili,BILIBILI)
print(json.dumps(res_bili,indent=4))
