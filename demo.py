from iiilab import get_source,YOUTUBE,FACEBOOK,BILIBILI
import json

# youtube video
url_yt="https://www.youtube.com/watch?v=MtOXxlUE2Zg"
src_yt=get_source(url_yt,YOUTUBE)
print(json.dumps(src_yt,indent=4))

# facebook video
url_fb="https://www.facebook.com/100094681485185/videos/815409647254080"
src_fb=get_source(url_fb,FACEBOOK)
print(json.dumps(src_fb,indent=4))

# bilibili video
url_bili="https://www.bilibili.com/video/BV1bg4y137R6"
src_bili=get_source(url_bili,BILIBILI)
print(json.dumps(src_bili,indent=4))
