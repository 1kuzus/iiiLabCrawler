from iiilab import get_resource
import json

urls = [
    # tiktok/douyin video
    "https://www.tiktok.com/@bbc/video/7142215700784893189",
    "https://www.douyin.com/user/MS4wLjABAAAA8U_l6rBzmy7bcy6xOJel4v0RzoR_wfAubGPeJimN__4?from_tab_name=main&modal_id=7506930749623373071",

    # youtube video
    "https://www.youtube.com/watch?v=RG9TMn1FJzc",

    # bilibili video
    "https://www.bilibili.com/video/BV1az4y1L7dL",

    # X/twitter video
    "https://x.com/TheCatsX/status/1924692026383335840",

    # facebook video
    "https://www.facebook.com/BBCArtsOnline/videos/florence-1501-michelangelo-and-leonardo-go-head-to-head-renaissance-the-blood-an/572612065554780/",

    # instagram video
    "https://www.instagram.com/reel/CzwrRR1SN-0",

    # 163 music
    "https://music.163.com/#/mv?id=5499051",
    "https://music.163.com/#/song?id=518894020",
]

for url in urls:
    res = get_resource(url)
    print(json.dumps(res, indent=4, ensure_ascii=False))
