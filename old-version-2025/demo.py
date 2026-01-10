from iiilab import get_resource, TIKTOK, YOUTUBE, FACEBOOK, BILIBILI, INSTAGRAM, TWITTER
import json

# tiktok/douyin video
url_tiktok = "https://www.douyin.com/user/MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4?from_tab_name=main&modal_id=7506930749623373071"
res_tiktok = get_resource(url_tiktok, TIKTOK)
print(json.dumps(res_tiktok, indent=4))

# youtube video
url_youtube = "https://www.youtube.com/watch?v=RG9TMn1FJzc"
res_youtube = get_resource(url_youtube, YOUTUBE)
print(json.dumps(res_youtube, indent=4))

# bilibili video
url_bili = "https://www.bilibili.com/video/BV1az4y1L7dL"
res_bili = get_resource(url_bili, BILIBILI)
print(json.dumps(res_bili, indent=4))

# facebook video
url_facebook = "https://www.facebook.com/BBCArtsOnline/videos/florence-1501-michelangelo-and-leonardo-go-head-to-head-renaissance-the-blood-an/572612065554780/"
res_facebook = get_resource(url_facebook, FACEBOOK)
print(json.dumps(res_facebook, indent=4))

# instagram video
url_instagram = "https://www.instagram.com/reel/CzwrRR1SN-0"
res_instagram = get_resource(url_instagram, INSTAGRAM)
print(json.dumps(res_instagram, indent=4))

# X/twitter video
url_twitter = "https://x.com/TheCatsX/status/1924692026383335840"
res_twitter = get_resource(url_twitter, TWITTER)
print(json.dumps(res_twitter, indent=4))
