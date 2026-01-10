# iiiLabCrawler

`A web crawler for the video parsing API of snapany.com/iiilab.com`

[简体中文](README_zh.md)

## Introduction

This repository is a Python web crawler for the video parsing API of [iiilab.com](https://iiilab.com/), a website that
supports parsing and downloading video links from multiple platforms.

Update: The video parsing API for some platforms is now redirected to [snapany.com](https://snapany.com/).
The crawler scripts for the old version can be found in the `old-version-202x`.

SnapAny currently supports downloading videos and images from TikTok/Douyin, YouTube, Bilibili, X/Twitter, Pinterest,
and other platforms.
Some platforms still require the old API, and this repository temporarily integrates parsing support for Facebook,
Instagram, and NetEase Cloud Music.

If you only need to parse and download a small number of media files, you can also use the original websites directly:

- [snapany.com (TikTok/Douyin, YouTube, Bilibili, X/Twitter)](https://snapany.com/)
- [facebook.iiilab.com (Facebook)](https://facebook.iiilab.com/)
- [instagram.iiilab.com (Instagram)](https://instagram.iiilab.com/)
- [yinyue.iiilab.com (NetEase Cloud Music)](https://yinyue.iiilab.com/)

## Preparation

```
git clone https://github.com/1kuzus/iiiLabCrawler.git
pip install requests
```

## Usage

```python
from iiilab import get_resource

res = get_resource(url="https://www.youtube.com/watch?v=...")
```

Set `url` to the resource link to be parsed.

If the request fails, `get_resource` will return `None` and prints the error details. Otherwise, it will return the
parsed JSON response data.

The script automatically determines whether to call the new or old API based on the domain of the provided URL.
If you need to force a specific API, you may pass a second argument to specify the platform.

```python
from iiilab import get_resource, MUSIC163

url = "https://music.163.com/#/song?id=518894020"
res = get_resource(url=url, site=MUSIC163)
```

### Demo

See `demo.py` for an example:

```python
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
```

You will get the output:

```
{
    "text": "Incredible orca hunt🤯 #FrozenPlanet2 #BBCiPlayer #iPlayer ",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://v16.tokcdn.com/a4b5559305c7e737b3958e6c2cc48d1a/631d2500/7142215700784893189_original.mp4",
            "preview_url": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/ed6b06befc12479d8845686ff91d1809_1662926686~tplv-tiktokx-360p.webp?dr=1363&refresh_token=372b800c&x-expires=1768129200&x-signature=M7cuD4kYJv7tzW3juA81JP3e91E%3D&t=bacd0480&ps=d97f9a4f&shp=d05b14bd&shcp=1d1a97fc&idc=maliva&sc=feed_cover&biz_tag=tt_video&s=AWEME_DETAIL"
        },
        {
            "media_type": "audio",
            "resource_url": "https://v16-ies-music.tiktokcdn.com/3a296d023659e028d616967063ed52b4/696b6fdb/video/tos/useast2a/tos-useast2a-v-27dcd7/a8e6e765d48045aa84c13714adb81c50/?a=583965&bti=OUBzOTg7QGo6OjZAL3AjLTAzYCMxNDNg&ch=0&cr=0&dr=0&er=0&lr=default&cd=0%7C0%7C0%7C0&br=250&bt=125&ft=k_ghWID.ZNhWVQl2Gclfu1mNSpM5SbrwuX.7TGbL&mime_type=audio_mpeg&qs=6&rc=ODM6NjUzaDVmZjg0N2hpN0BpM2o3eGg6ZnE2ZjMzNzU8M0AxNWI0NGMyNmAxNWFiMS8xYSNrcmYvcjRfcmNgLS1kMTZzcw%3D%3D&vvpl=1&l=202601101911313F52CFE9CB8F10BB05A6&btag=e00098000&shp=d05b14bd&shcp=-",
            "preview_url": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/65c76bec2af5783edfd123d29c90da99~tplv-tiktokx-cropcenter-q:1080:1080:q70.webp?dr=10796&idc=maliva&ps=87d6e48a&refresh_token=e3ef3d3c&s=AWEME_DETAIL&sc=avatar&shcp=1d1a97fc&shp=d05b14bd&t=223449c4&x-expires=1768129200&x-signature=mCy92D%2FIPhRyhWtTpjoKN%2Fo2c%2BI%3D"
        }
    ],
    "overseas": 1,
    "id": "7142215700784893189"
}
{
    "text": "四年了，风吹过稻田，依然想念您。缅怀袁老！",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://v11.douyinvod.com/abacb963a53d27fd094b795a9c9dc144/69623e00/video/tos/cn/tos-cn-ve-15/osAue2Egtt4faWdG0ZCM2AADMYC8ARx57ifjQf/?a=1128&ch=0&cr=0&dr=0&er=0&cd=0%7C0%7C0%7C0&cv=1&br=1250&bt=1250&cs=0&ds=4&ft=ahhJkQQqUnXfmoZmo0OW_QYaUqiXjy4EkVJEHNuMIbPD-Ipz&mime_type=video_mp4&qs=0&rc=aGk8aGY8ZWhpOmg0MzQ6aEBpamV3NnA5cmx5MzMzNGkzM0BfNTJeYzMuNjYxYS80YWIwYSMuazBnMmQ0amphLS1kLTBzcw%3D%3D&btag=c0000e000a5000&cc=33&cquery=100y&dy_q=1768042428&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=202601101853483493F9DDA6B3FA973FC1&req_cdn_type=",
            "preview_url": "https://p3-pc-sign.douyinpic.com/image-cut-tos-priv/4e48fbbf9b2c40ced0a64c3d186d836e~tplv-dy-resize-origshort-autoq-75:330.jpeg?lk3s=138a59ce&x-expires=2083399200&x-signature=MWg1XP1E8m3ykf%2B%2BwHgaJL2oN10%3D&from=327834062&s=PackSourceEnum_AWEME_DETAIL&se=false&sc=cover&biz_tag=pcweb_cover&l=20260110185348A824162A2DBC4B6C6069",
            "headers": {
                "User-Agent": ""
            }
        }
    ],
    "overseas": 0
}
{
    "text": "The incredible ibex defies gravity and climbs a dam | Forces of Nature with Brian Cox - BBC",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3AkQPcnfxxeLIohyTRTJ1Sl63noNCWTJojvd9OUK5QeYH237Qb2ZrW1y6_US2e1zvV0RZKxjOYo&spc=wH4Qq0a8kQsZ-izNzoN7&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=16332781&ratebypass=yes&dur=232.408&lmt=1725424927317407&mt=1768041895&fvip=3&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4538434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAJh_IG0dKiTxLmH7ShT5ZKjU04KbT_nqQnSNNjKZytmCAiAGrFkceITNwulL8qE9DVgPsrQ92EfRR8OTEpAG1Y1PIA%3D%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
            "preview_url": "https://i.ytimg.com/vi_webp/RG9TMn1FJzc/sddefault.webp",
            "formats": [
                {
                    "quality": 1080,
                    "quality_note": "1080p",
                    "video_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=137&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=56556197&dur=232.360&lmt=1725425356139113&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgdEcEDIe8vamqIvCP4qlMgP85tWAvSzjK4Lu4PCHRM3ACIGKlbJg-SkOAO0j7vlHnXg3tuLRN5gOSwonqPvxCGr2J&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "video_ext": "mp4",
                    "video_size": 56556197,
                    "audio_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=3762111&dur=232.408&lmt=1725424428667227&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhANNfHPVOxVJPLAcAwY_t4kUWRCaiJvEkZaYHWfd3M5O1AiEArNacL7nJuIL5Qg_-3gx2p567WYmrhHImijW83W3c4v4%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "audio_ext": "m4a",
                    "audio_size": 3762111,
                    "separate": 1,
                    "video_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEdSLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAdDB0IFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYTFtMGEJUSkNxHlVJX09JARdORh5ZS0pbSXEBVUNGGwcIDVBIGkZQR0YYWFBPXEoURVRAKFhbVUtbFFlJVERCFVtRSFVAGCgQQ0QfXQMPBAkQRzkGRB1ZUxIIHF0VCRoCSFYcHB4lWERVQUJLDh0JUEwcQVBBQhVSQEsuTBxBU0ZFHF5ASy5MHEFTRkIVWUBLLkwcQV1DTRtTOQxdSR9CBk41Yy83NiQ9cQFVQ0YbHx0JUE0YR1dHRxk3EEldSxsHFRIGTAYWRAgBXR0XFlEfKAAQSEtuHRVWRm4CAVxfOkQABBRRHygWFhgLThFAQTdfDhQMBAtIBxYfUR8oHQkOXB83BwYdCFkmCh0aCEYmBQRfHUBLLgpbBBAQUR8oCBAAHAhGJgEFRU5XOgoQX1FXMBdBDgtcXzpJARdWRm4HCA0xDB1EV0UHRAxYOCcffBA2AAN%2FKiweCTxOMSE6ERUdBBQcMFs3NUcFQSYCKVVMWSMkBSdXAS5NIQwZJCY7JmBYJDokPmYYBzkTADgONiw2HR5SBRhlBT0eXg1YODc9QUokNg4CF1wkEws3ahlXMzEMHURXRRheGwQLDBReSQYDBwhZJhQIDQhGJh4cCFkmFABcHzcIHVEfKAgKSEtuGRNWRm4GExBIS24ECVZGbhkICkhLbh0LGgBOHAsdDwleKBBDRB9dCQoEHhA1NRIgVRMoDj8eZBwkPzt6GgERWk5jMyA6I2guCEwZMBweExhCZy4wLCpKZjwrKkJoH1ITI04aNyQaMWweDg8yPABALiA7GAotDjkgXxkPF0xqGA5JJjpJGy8sQWk0ChsJGFlBN0UlCFghWxA%3D",
                    "audio_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEBVLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAKEB0EFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSlpPH0VUQihYW1VLWx1YBlhBRx9FUUlVJVhEVUFCQQYRRFxOH0FRQUAZWV1PW04fRlIvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZKIg04IzdLPDUlO1U9LykhOE41EiorWV8OLDorbhUMOQJoAD8YNDF6EgFAORgkVDgEPGwGKxIXYVwLMxgwYUE0FCsAWAIBXwkYQlIkLUAZDTEkFEQeMktHelgGTRtNCEchLwEdW1dPAQpdFRcSGV5WBgkeXB83CBYACFkmFAVcHzcIHlEfKAgXSEtuGRZWRm4GE1xfOkACDFZGbhsJXF86XxkWVkZuAgsQGRpaGgERBF43EEldSxsYFhoTECo1GDkBVTkSIRNkAyQ1Ii5cEA1EQ2MsIDA6PGgZUAc9HAETElszaCEwNEdmIysgWzxZQw89QxooJBAoOFgfEywxAF8uKiJMTDwSJy1fBg8dVT5eH1U4N0kELyZYPXIbBxcVWV43TzxcHjBHDg%3D%3D"
                },
                {
                    "quality": 720,
                    "quality_note": "720p",
                    "video_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=136&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=18194126&dur=232.360&lmt=1725425255555336&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhAMjGKkh3IgmlFT_X7Z1zBStHh85g79dvNa7O6GVrDJyyAiEAloxNbRYxeLxVdY9nEYnbaJxjNWDq6ofuiRGjzy36fAI%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "video_ext": "mp4",
                    "video_size": 18194126,
                    "audio_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=3762111&dur=232.408&lmt=1725424428667227&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhANNfHPVOxVJPLAcAwY_t4kUWRCaiJvEkZaYHWfd3M5O1AiEArNacL7nJuIL5Qg_-3gx2p567WYmrhHImijW83W3c4v4%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "audio_ext": "m4a",
                    "audio_size": 3762111,
                    "separate": 1,
                    "video_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEdTLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAdDB0IFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSFVIFEBUQUJxHlVJX09JARdORh5ZS0pbSXEBVUNGGwcIDVBIGkZQR0YYWVBMWEwYR1ZFKFhbVUtbFFlJVERCFVtRSFVAGCgQQ0QfXQMPBAkQRzkGRB1ZUxIIHF0VCRoCSFYcHB4lWERVQUJLDh0JUEwcQVBBQhVSQEsuTBxBU0ZFHF5ASy5MHEFTRkIVWUBLLkwcQV1DTRtTOQxdSR9CBk41Yy83NiQ9cQFVQ0YbHx0JUE0YR1dHRxk3EEldSxsHFRIGTAYWRAgBXR0XFlEfKAAQSEtuHRVWRm4CAVxfOkQABBRRHygWFhgLThFAQTdfDhQMBAtIBxYfUR8oHQkOXB83BwYdCFkmCh0aCEYmBQRfHUBLLgpbBBAQUR8oCBAAHAhGJgEFRU5XOgoQX1FXMBdBDgtcXzpJARdWRm4HCA0xDB1EV0UHRAxYOCcffBA2AAN%2FDCwRLDRHMy4YHB4iAhQBP3krPUQuHBEnKhkxRUxQFEMUDxM3DE5iQiIlBmkhHAAsEGg1CRwMYwk3IBUcYQwzFy0UBSAgAxtMPh0ZOnovFE8CH1gdNzQeVxJWTws4ZFFWNyhYW1VLWxVeBAQBFUAYWBodCghGJh4RWU5XOgARCEYmHhkIWSYUA1wfNwgAUR8oCA9IS24ZExpRHygVFUhLbgYIAFEfKAwXBA1OAwsXFl0YOQxdSR9CCQAdSlYkKQwtVQwoBCZKIg04ITZ6BQEbQxolIjwkLmgxCEYAZFoPDwZPZzEwJjMeIC03NE9oAFIZOhpcJjgEPGwBDgUraEZRMj42GBUtBCB0GQgTCUFqBw5DP24PCjMyTGkrChEQTB9QK1soCEchUQk%3D",
                    "audio_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEBVLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAKEB0EFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSlpPH0VUQihYW1VLWx1YBlhBRx9FUUlVJVhEVUFCQQYRRFxOH0FRQUAZWV1PW04fRlIvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZKIg04IzdLPDUlO1U9LykhOE41EiorWV8OLDorbhUMOQJoAD8YNDF6EgFAORgkVDgEPGwGKxIXYVwLMxgwYUE0FCsAWAIBXwkYQlIkLUAZDTEkFEQeMktHelgGTRtNCEchLwEdW1dPAQpdFRcSGV5WBgkeXB83CBYACFkmFAVcHzcIHlEfKAgXSEtuGRZWRm4GE1xfOkACDFZGbhsJXF86XxkWVkZuAgsQGRpaGgERBF43EEldSxsYFhoTECo1GDkBVTkSIRNkAyQ1Ii5cEA1EQ2MsIDA6PGgZUAc9HAETElszaCEwNEdmIysgWzxZQw89QxooJBAoOFgfEywxAF8uKiJMTDwSJy1fBg8dVT5eH1U4N0kELyZYPXIbBxcVWV43TzxcHjBHDg%3D%3D"
                },
                {
                    "quality": 480,
                    "quality_note": "480p",
                    "video_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=135&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=9944950&dur=232.360&lmt=1725425253993160&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhAMYMCCmoU4tqsrRFPusJ-Nyr-viUQ1sySY-M6c654xmWAiBL1NxkCl6aVukm_KqoUkjMEk5SQQLsDMmgyRReiKjZdQ%3D%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "video_ext": "mp4",
                    "video_size": 9944950,
                    "audio_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=3762111&dur=232.408&lmt=1725424428667227&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhANNfHPVOxVJPLAcAwY_t4kUWRCaiJvEkZaYHWfd3M5O1AiEArNacL7nJuIL5Qg_-3gx2p567WYmrhHImijW83W3c4v4%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "audio_ext": "m4a",
                    "audio_size": 3762111,
                    "separate": 1,
                    "video_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEdQLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAdDB0IFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYQFRNGU1QQyhYW1VLWx1YBlhBRx9FVk9dJVhEVUFCQQYRRFxOH0FRQUEfXlZAVEocQlUvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZ8Ig04ICBgNyYeG3hfEQgeC38yNQYHZ0YrAB9UWx0wIkVeEjYgQDQbF1NGQFUGMjgEO2FFKwsfbgdTGDsMRhk6OAVCPg4TIDxGQTYiJWEYITQAHlQmNxYdZgE%2FHTxcHjBAQDBxHlVJX09BBxUSBkwGFkQOCV5RVzAZSB9ASy4URVFXMBlATlc6ABcIRiYeBwhZJhQbXB83CAUdCFkmCQFcHzcXHgcIWSYQAxBZFxIdEE8bFiUYSR1GUx8HRAxYOD0YeQwdPgN%2FDCwRLDViIxQXHBpcKz4oMHoxIB5BWSJUExsSGz4gJiFqWC4xIyAbMRFEHmNcUjosEGg1EBgCci5ITSYqYkEEOwN5MhcUBx0VMxYYRGYoARYnJhgwOhwWSQoRTD9PfFFWN1ZQ",
                    "audio_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEBVLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAKEB0EFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSlpPH0VUQihYW1VLWx1YBlhBRx9FUUlVJVhEVUFCQQYRRFxOH0FRQUAZWV1PW04fRlIvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZKIg04IzdLPDUlO1U9LykhOE41EiorWV8OLDorbhUMOQJoAD8YNDF6EgFAORgkVDgEPGwGKxIXYVwLMxgwYUE0FCsAWAIBXwkYQlIkLUAZDTEkFEQeMktHelgGTRtNCEchLwEdW1dPAQpdFRcSGV5WBgkeXB83CBYACFkmFAVcHzcIHlEfKAgXSEtuGRZWRm4GE1xfOkACDFZGbhsJXF86XxkWVkZuAgsQGRpaGgERBF43EEldSxsYFhoTECo1GDkBVTkSIRNkAyQ1Ii5cEA1EQ2MsIDA6PGgZUAc9HAETElszaCEwNEdmIysgWzxZQw89QxooJBAoOFgfEywxAF8uKiJMTDwSJy1fBg8dVT5eH1U4N0kELyZYPXIbBxcVWV43TzxcHjBHDg%3D%3D"
                },
                {
                    "quality": 360,
                    "quality_note": "360p",
                    "video_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3AkQPcnfxxeLIohyTRTJ1Sl63noNCWTJojvd9OUK5QeYH237Qb2ZrW1y6_US2e1zvV0RZKxjOYo&spc=wH4Qq0a8kQsZ-izNzoN7&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=16332781&ratebypass=yes&dur=232.408&lmt=1725424927317407&mt=1768041895&fvip=3&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4538434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAJh_IG0dKiTxLmH7ShT5ZKjU04KbT_nqQnSNNjKZytmCAiAGrFkceITNwulL8qE9DVgPsrQ92EfRR8OTEpAG1Y1PIA%3D%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "video_ext": "mp4",
                    "video_size": 16332781,
                    "separate": 0,
                    "video_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEw5BkQdWVMKAgxfFwBODUIeEQwPHHEBVUNGGxkACBgQXxEWABgQEgAKMQwdRFdFDF0IWDwKL0JGBDcnYzpASilcHjA5BkQdWVMaHQoQRjkGRB1ZUxQIDRBFUkVMHV9XTV9ACEYmLwEdW1dPABEQJ0gvAR1bV08AFBBHVFZGbllcJRhJHUZTHhoQGAtUGAFMDFEFG10BUAgVVE4MAhhRHygWF0BNSkEAFxpJXDkMXUkfQggASUweQEsuC0kBOQZEHVlTFBtEQCgQQ0QfXQgPBEQcRTkGRB1ZUwkBRB9EOQZEHVlTCwAKEBUQVkZuChAlGEkdRlMaGkQfBg4DHU8EFk5FFFNdTlhJcQFVQ0YbCRAQUDh0ITYyR2wANCkOF0sMHRY4ZAQNADkreT5UIBgbWAsWIzp6IC8cHlsPXDY4MhglACo8H1hSKA9LdwYyQg0bNDAqXxwcDhMlRH8xLgEHNnQbOQZEHVlTCh0aEAMtRyVcWwRBBiheLkgaDmMRCjdaJVhEVUFCWxsXD1BIcQFVQ0YbGBMJGBoQRTkGRB1ZUxQEFEhJExoQSARASysUXUA5BkQdWVMLHBEQRTkGRB1ZUx4ECxANAAAoWFtVS1saQRELTkUbWFZLWkEcKBBDRB9dFxgZHE8NFRIHXlYcHB4lWERVQUJJHhdEX0ofWlFDTHEeVUlfT0EZEU5FGllQTV9NFEZSQEUaX1VOMQwdRFdFGVlWVE5bQR1AVEtNGDcQSV1LGxITGgQQWDkMXUkfQgMWDF1WUEhYTB9CXUpRHyhQSFhPGEVURlEfKFBIWE8YQl1BUR8oUEhYQR1NU0soWFtVS1saEDUrNyZiIiElGEkdRlMHDF1WUUxeQRlHUS8BHVtXTx4JTAYEHgcQDh0JBAtIUVcwEUROVzoECQhGJhoQCFkmEBkYSlFXMAdCHhcaCFwfNxcWBVgCFxweCkFRVzAMXQhASy4bWB1AQTdeGwZcXzpbBBcFUR8oFg8dDE5RVzAZRAYAXF86XwUNVkZuDAwLSEtuFwkWGghZJgsMDUgWHAMVXhhASy4dWAZAQTdBBhElGEkdRlMAHUpWJDMLKEknFgQmfCINOCcRcj0iQxBmAjEBIRRlQzYbIBgxLhM4SRk%2FBycrQxo0Fz43Yx4uKQ1ZBiY4BDhqBiMYF0giMTcaDEE4XQIxFC8zHj0KXyVcQTFLOTdBIi1oBCQ0RXRaNTAsXB4wQEAwcR5VSV9PQQcVEgZMBhZEDgleUVcwGUgfQEsuFEVRVzAZQE5XOgAXCEYmHgcIWSYUG1wfNwgFHQhZJgkBXB83Fx4HCFkmEAMQWRcSHRBPGxYlGEkdRlMfB0QMWDg9GHkMHT4DfwwsESw1YiMUFxwaXCs%2BKDB6MSAeQVkiVBMbEhs%2BICYhalguMSMgGzERRB5jXFI6LBBoNRAYAnIuSE0mKmJBBDsDeTIXFAcdFTMWGERmKAEWJyYYMDocFkkKEUw%2FT3xRVjdWUA%3D%3D"
                },
                {
                    "quality": 240,
                    "quality_note": "240p",
                    "video_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=133&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=3040395&dur=232.360&lmt=1725425259108255&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIhAI6PFFYvbBgWrhJS6W_8eWuxlkSsRSDRnTi-2-i2PtGtAiASFmFxl7_qzcPpnC7u1JEl1DEOwQWZB6onekbw2t_vKQ%3D%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "video_ext": "mp4",
                    "video_size": 3040395,
                    "audio_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=3762111&dur=232.408&lmt=1725424428667227&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhANNfHPVOxVJPLAcAwY_t4kUWRCaiJvEkZaYHWfd3M5O1AiEArNacL7nJuIL5Qg_-3gx2p567WYmrhHImijW83W3c4v4%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "audio_ext": "m4a",
                    "audio_size": 3762111,
                    "separate": 1,
                    "video_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEdWLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAdDB0IFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSl1NHUdcRihYW1VLWx1YBlhBRx9FVk9dJVhEVUFCQQYRRFxOH0FRQUEfXlxIXUEfQVAvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZ8Ig04JE99MiMqAk8pAi4fEWcnUyQrFQ4yDBUVRicWISdpOQstBFQfWQxBJFksETgEOH4yCDUMQVw6CBcafQQLMENYWi88AUhpMSoEJXoxJ08CF0gfBwRGWTQTMjxcHjBAQDBxHlVJX09BBxUSBkwGFkQOCV5RVzAZSB9ASy4URVFXMBlATlc6ABcIRiYeBwhZJhQbXB83CAUdCFkmCQFcHzcXHgcIWSYQAxBZFxIdEE8bFiUYSR1GUx8HRAxYOD0YeQwdPgN%2FDCwRLDViIxQXHBpcKz4oMHoxIB5BWSJUExsSGz4gJiFqWC4xIyAbMRFEHmNcUjosEGg1EBgCci5ITSYqYkEEOwN5MhcUBx0VMxYYRGYoARYnJhgwOhwWSQoRTD9PfFFWN1ZQ",
                    "audio_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEBVLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAKEB0EFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSlpPH0VUQihYW1VLWx1YBlhBRx9FUUlVJVhEVUFCQQYRRFxOH0FRQUAZWV1PW04fRlIvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZKIg04IzdLPDUlO1U9LykhOE41EiorWV8OLDorbhUMOQJoAD8YNDF6EgFAORgkVDgEPGwGKxIXYVwLMxgwYUE0FCsAWAIBXwkYQlIkLUAZDTEkFEQeMktHelgGTRtNCEchLwEdW1dPAQpdFRcSGV5WBgkeXB83CBYACFkmFAVcHzcIHlEfKAgXSEtuGRZWRm4GE1xfOkACDFZGbhsJXF86XxkWVkZuAgsQGRpaGgERBF43EEldSxsYFhoTECo1GDkBVTkSIRNkAyQ1Ii5cEA1EQ2MsIDA6PGgZUAc9HAETElszaCEwNEdmIysgWzxZQw89QxooJBAoOFgfEywxAF8uKiJMTDwSJy1fBg8dVT5eH1U4N0kELyZYPXIbBxcVWV43TzxcHjBHDg%3D%3D"
                },
                {
                    "quality": 144,
                    "quality_note": "144p",
                    "video_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=160&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=1350792&dur=232.360&lmt=1725425253642860&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhALQgMhYR1Ssm5uLXBOWiIEpkvSav9vRMnxHSikiSOOjsAiEAgcViW7vAAoeVsLn1j1pnb7F5Ecuzvamdqbqsj2X7q1Q%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "video_ext": "mp4",
                    "video_size": 1350792,
                    "audio_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=3762111&dur=232.408&lmt=1725424428667227&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhANNfHPVOxVJPLAcAwY_t4kUWRCaiJvEkZaYHWfd3M5O1AiEArNacL7nJuIL5Qg_-3gx2p567WYmrhHImijW83W3c4v4%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
                    "audio_ext": "m4a",
                    "audio_size": 3762111,
                    "separate": 1,
                    "video_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1UUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEJVLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAdDB0IFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSF5MHUNcQShYW1VLWx1YBlhBRx9FVk9dJVhEVUFCQQYRRFxOH0FRQUEfXlZPWUsVQlUvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZKIg04IShKOQ0qJhw4FhRYDGEsJzwjRCIgCQYPfhUTSgJ%2FJgsBJSpEHwwgO2IBFjgEPGwTBiUdelwTOCwWSCIWPxocAVQJAxsaMlA2F1gRExgAHVwWFAAeHzNSCFwoCEchLwEdW1dPAQpdFRcSGV5WBgkeXB83CBYACFkmFAVcHzcIHlEfKAgXSEtuGRZWRm4GE1xfOkACDFZGbhsJXF86XxkWVkZuAgsQGRpaGgERBF43EEldSxsYFhoTECo1GDkBVTkSIRNkAyQ1Ii5cEA1EQ2MsIDA6PGgZUAc9HAETElszaCEwNEdmIysgWzxZQw89QxooJBAoOFgfEywxAF8uKiJMTDwSJy1fBg8dVT5eH1U4N0kELyZYPXIbBxcVWV43TzxcHjBHDg%3D%3D",
                    "audio_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1UUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEBVLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAKEB0EFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSlpPH0VUQihYW1VLWx1YBlhBRx9FUUlVJVhEVUFCQQYRRFxOH0FRQUAZWV1PW04fRlIvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZKIg04IzdLPDUlO1U9LykhOE41EiorWV8OLDorbhUMOQJoAD8YNDF6EgFAORgkVDgEPGwGKxIXYVwLMxgwYUE0FCsAWAIBXwkYQlIkLUAZDTEkFEQeMktHelgGTRtNCEchLwEdW1dPAQpdFRcSGV5WBgkeXB83CBYACFkmFAVcHzcIHlEfKAgXSEtuGRZWRm4GE1xfOkACDFZGbhsJXF86XxkWVkZuAgsQGRpaGgERBF43EEldSxsYFhoTECo1GDkBVTkSIRNkAyQ1Ii5cEA1EQ2MsIDA6PGgZUAc9HAETElszaCEwNEdmIysgWzxZQw89QxooJBAoOFgfEywxAF8uKiJMTDwSJy1fBg8dVT5eH1U4N0kELyZYPXIbBxcVWV43TzxcHjBHDg%3D%3D"
                }
            ],
            "resource_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1VUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEw5BkQdWVMKAgxfFwBODUIeEQwPHHEBVUNGGxkACBgQXxEWABgQEgAKMQwdRFdFDF0IWDwKL0JGBDcnYzpASilcHjA5BkQdWVMaHQoQRjkGRB1ZUxQIDRBFUkVMHV9XTV9ACEYmLwEdW1dPABEQJ0gvAR1bV08AFBBHVFZGbllcJRhJHUZTHhoQGAtUGAFMDFEFG10BUAgVVE4MAhhRHygWF0BNSkEAFxpJXDkMXUkfQggASUweQEsuC0kBOQZEHVlTFBtEQCgQQ0QfXQgPBEQcRTkGRB1ZUwkBRB9EOQZEHVlTCwAKEBUQVkZuChAlGEkdRlMaGkQfBg4DHU8EFk5FFFNdTlhJcQFVQ0YbCRAQUDh0ITYyR2wANCkOF0sMHRY4ZAQNADkreT5UIBgbWAsWIzp6IC8cHlsPXDY4MhglACo8H1hSKA9LdwYyQg0bNDAqXxwcDhMlRH8xLgEHNnQbOQZEHVlTCh0aEAMtRyVcWwRBBiheLkgaDmMRCjdaJVhEVUFCWxsXD1BIcQFVQ0YbGBMJGBoQRTkGRB1ZUxQEFEhJExoQSARASysUXUA5BkQdWVMLHBEQRTkGRB1ZUx4ECxANAAAoWFtVS1saQRELTkUbWFZLWkEcKBBDRB9dFxgZHE8NFRIHXlYcHB4lWERVQUJJHhdEX0ofWlFDTHEeVUlfT0EZEU5FGllQTV9NFEZSQEUaX1VOMQwdRFdFGVlWVE5bQR1AVEtNGDcQSV1LGxITGgQQWDkMXUkfQgMWDF1WUEhYTB9CXUpRHyhQSFhPGEVURlEfKFBIWE8YQl1BUR8oUEhYQR1NU0soWFtVS1saEDUrNyZiIiElGEkdRlMHDF1WUUxeQRlHUS8BHVtXTx4JTAYEHgcQDh0JBAtIUVcwEUROVzoECQhGJhoQCFkmEBkYSlFXMAdCHhcaCFwfNxcWBVgCFxweCkFRVzAMXQhASy4bWB1AQTdeGwZcXzpbBBcFUR8oFg8dDE5RVzAZRAYAXF86XwUNVkZuDAwLSEtuFwkWGghZJgsMDUgWHAMVXhhASy4dWAZAQTdBBhElGEkdRlMAHUpWJDMLKEknFgQmfCINOCcRcj0iQxBmAjEBIRRlQzYbIBgxLhM4SRk%2FBycrQxo0Fz43Yx4uKQ1ZBiY4BDhqBiMYF0giMTcaDEE4XQIxFC8zHj0KXyVcQTFLOTdBIi1oBCQ0RXRaNTAsXB4wQEAwcR5VSV9PQQcVEgZMBhZEDgleUVcwGUgfQEsuFEVRVzAZQE5XOgAXCEYmHgcIWSYUG1wfNwgFHQhZJgkBXB83Fx4HCFkmEAMQWRcSHRBPGxYlGEkdRlMfB0QMWDg9GHkMHT4DfwwsESw1YiMUFxwaXCs%2BKDB6MSAeQVkiVBMbEhs%2BICYhalguMSMgGzERRB5jXFI6LBBoNRAYAnIuSE0mKmJBBDsDeTIXFAcdFTMWGERmKAEWJyYYMDocFkkKEUw%2FT3xRVjdWUA%3D%3D",
            "subtitles": [
                {
                    "language_name": "English",
                    "language_tag": "English",
                    "urls": [
                        {
                            "url": "https://www.youtube.com/api/timedtext?caps=asr&ei=vS9iaaLbKKTKi9oPyIK48Q0&expire=1768067629&fmt=srt&hl=en&ip=0.0.0.0&ipbits=0&key=yt8&lang=en&opi=112496729&signature=1744D4536C6D0AB98FED868860E599035D550DCC.F0570188A368823307370DDAE2521767A9E62115&sparams=ip%2Cipbits%2Cexpire%2Cv%2Cei%2Ccaps%2Copi%2Cxoaf&v=RG9TMn1FJzc&xoaf=5&xowf=1",
                            "format": "srt"
                        },
                        {
                            "url": "https://www.youtube.com/api/timedtext?caps=asr&ei=vS9iaaLbKKTKi9oPyIK48Q0&expire=1768067629&fmt=vtt&hl=en&ip=0.0.0.0&ipbits=0&key=yt8&lang=en&opi=112496729&signature=1744D4536C6D0AB98FED868860E599035D550DCC.F0570188A368823307370DDAE2521767A9E62115&sparams=ip%2Cipbits%2Cexpire%2Cv%2Cei%2Ccaps%2Copi%2Cxoaf&v=RG9TMn1FJzc&xoaf=5&xowf=1",
                            "format": "vtt"
                        },
                        {
                            "url": "https://www.youtube.com/api/timedtext?caps=asr&ei=vS9iaaLbKKTKi9oPyIK48Q0&expire=1768067629&fmt=ttml&hl=en&ip=0.0.0.0&ipbits=0&key=yt8&lang=en&opi=112496729&signature=1744D4536C6D0AB98FED868860E599035D550DCC.F0570188A368823307370DDAE2521767A9E62115&sparams=ip%2Cipbits%2Cexpire%2Cv%2Cei%2Ccaps%2Copi%2Cxoaf&v=RG9TMn1FJzc&xoaf=5&xowf=1",
                            "format": "ttml"
                        },
                        {
                            "url": "https://www.youtube.com/api/timedtext?caps=asr&ei=vS9iaaLbKKTKi9oPyIK48Q0&expire=1768067629&fmt=json3&hl=en&ip=0.0.0.0&ipbits=0&key=yt8&lang=en&opi=112496729&signature=1744D4536C6D0AB98FED868860E599035D550DCC.F0570188A368823307370DDAE2521767A9E62115&sparams=ip%2Cipbits%2Cexpire%2Cv%2Cei%2Ccaps%2Copi%2Cxoaf&v=RG9TMn1FJzc&xoaf=5&xowf=1",
                            "format": "json3"
                        },
                        {
                            "url": "https://www.youtube.com/api/timedtext?caps=asr&ei=vS9iaaLbKKTKi9oPyIK48Q0&expire=1768067629&fmt=srv1&hl=en&ip=0.0.0.0&ipbits=0&key=yt8&lang=en&opi=112496729&signature=1744D4536C6D0AB98FED868860E599035D550DCC.F0570188A368823307370DDAE2521767A9E62115&sparams=ip%2Cipbits%2Cexpire%2Cv%2Cei%2Ccaps%2Copi%2Cxoaf&v=RG9TMn1FJzc&xoaf=5&xowf=1",
                            "format": "srv1"
                        },
                        {
                            "url": "https://www.youtube.com/api/timedtext?caps=asr&ei=vS9iaaLbKKTKi9oPyIK48Q0&expire=1768067629&fmt=srv2&hl=en&ip=0.0.0.0&ipbits=0&key=yt8&lang=en&opi=112496729&signature=1744D4536C6D0AB98FED868860E599035D550DCC.F0570188A368823307370DDAE2521767A9E62115&sparams=ip%2Cipbits%2Cexpire%2Cv%2Cei%2Ccaps%2Copi%2Cxoaf&v=RG9TMn1FJzc&xoaf=5&xowf=1",
                            "format": "srv2"
                        },
                        {
                            "url": "https://www.youtube.com/api/timedtext?caps=asr&ei=vS9iaaLbKKTKi9oPyIK48Q0&expire=1768067629&fmt=srv3&hl=en&ip=0.0.0.0&ipbits=0&key=yt8&lang=en&opi=112496729&signature=1744D4536C6D0AB98FED868860E599035D550DCC.F0570188A368823307370DDAE2521767A9E62115&sparams=ip%2Cipbits%2Cexpire%2Cv%2Cei%2Ccaps%2Copi%2Cxoaf&v=RG9TMn1FJzc&xoaf=5&xowf=1",
                            "format": "srv3"
                        }
                    ]
                }
            ]
        },
        {
            "media_type": "audio",
            "resource_url": "https://redirector.googlevideo.com/videoplayback?expire=1768064029&ei=vS9iaaLbKKTKi9oPyIK48Q0&ip=176.6.151.223&id=o-AH-1ra1NuwXrE8j74ndWvtROvuZQpSVioKVvtrmy9G6L&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&cps=2&met=1768042429%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-cxgk%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=11&pl=20&rms=au%2Cau&initcwndbps=1988750&bui=AYUSA3DbztcfTVHlDa4Jc6m5vUBrykJZQ1kx4NSYttXWx1a8l6ns92wrkcNCPty1_46dwa9oq0ZlX9cB&spc=wH4Qqz69OQsR&vprv=1&svpuc=1&mime=audio%2Fmp4&rqh=1&gir=yes&clen=3762111&dur=232.408&lmt=1725424428667227&mt=1768041895&fvip=3&keepalive=yes&fexp=51552689%2C51565115%2C51565682%2C51580968&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhANNfHPVOxVJPLAcAwY_t4kUWRCaiJvEkZaYHWfd3M5O1AiEArNacL7nJuIL5Qg_-3gx2p567WYmrhHImijW83W3c4v4%3D&lsparams=cps%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=APaTxxMwRgIhALOWqdh77NGEIWEEm5tI1jvk6JEUUG3KHNY6Et7jN77CAiEAukv_E-4KSO5aHwTYrmjd8Gsk0KCdoJ_5D_obdat5R6Q%3D",
            "preview_url": "https://i.ytimg.com/vi_webp/RG9TMn1FJzc/sddefault.webp",
            "resource_proxy_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkVMHV9WTF1IHk1UUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREIVW1NNXUsUKBBDRB9dABBQD35NDBIVYQkuMjkyRE0KIw1kIFFBPElxAVVDRhsCFURcThtaU11FGFpLS19KcQFVQ0YbAgFEAlRsPEhCBkxaKwwaIV8xXRlDGQUBLhsNfzsTBi58GzYvBBZmIhMHBkASXD5bNXEBVUNGGwIRGApEHEBVLwEdW1dPHhZYBgYWSVQEEA0YG0goEENEH10XHBwMRAYAAAdBVhwcHiVYRFVBQlUbBkQoHnsbVxIwfiU0XF49CEchLwEdW1dPDgleSVcvAR1bV08AHFlJVERCFVtRS1lLFFFXMChYW1VLWxRFSTZeKFhbVUtbFEBJVkJRHyhXQDEMHURXRRlDVhYXQAxVFR1HAkIbD0wcAQAXHRQfCFkmCgNUGRNQFhBDD1IlGEkdRlMeBxAKEFxfOl8QEC8BHVtXTwAPEBk5BkQdWVMUGxAQRVQvAR1bV08dFRBGVS8BHVtXTx8UXkkEBlEfKAQMMQwdRFdFHUMCERoaF0kWFQBJHFJdQVpMHSgQQ0QfXQcMBERsLTAgNR4vBwMZGksgMzsYaQpRMw5PQEETJjZfEg4zNygcHx1HOn4yEQ01LlVFBEsYGwUWQF8OXx8GPTd9HxxIMk0bEBISTUIaVSMBIRQXJy8BHVtXTx4JTkkSO0B8Gh9PVDZ8BzcvAR1bV08bCV8CWEIoWFtVS1sKWwQQEEkcNxBJXUsbGQweERAKEB0EFghGIx4EGTcQSV1LGwYUG0kcNxBJXUsbEwwBSVQOFiUYSR1GUxAYSAVYSlpPH0VUQihYW1VLWx1YBlhBRx9FUUlVJVhEVUFCQQYRRFxOH0FRQUAZWV1PW04fRlIvAR1bV08ADRBFUkVMHV9UQVRMcQFVQ0YbDRMQHUQeKBBDRB9dDhwICUwYDAUREBIACjEMHURXRRJIExVEWEgYQVdFTBROVzpYSBhCUEJFGE5XOlhIGEJQRUwfTlc6WEgYTFVKQhU3EEldSxsXWDI6aTkqMCklWERVQUJZExVEWUweRlFAQHEeVUlfT14EBAEVQBhYHBUJRAYAVkZuDgxcXzpEBEBBN0QPQEsuEFkVAlZGbhgKDB8aSFFXMAZIGhAQHxxeBwlWRm4TFRpIS24WEBpRHygWCQ5cHzcTAwZbTlc6Hg9dAQZWRm4GDBQIXB83FwIcCFkmHgQLCEYmEBhIBUBLLh1YBkBBN0EGESUYSR1GUwAdSlYkMwsoSScWBCZKIg04IzdLPDUlO1U9LykhOE41EiorWV8OLDorbhUMOQJoAD8YNDF6EgFAORgkVDgEPGwGKxIXYVwLMxgwYUE0FCsAWAIBXwkYQlIkLUAZDTEkFEQeMktHelgGTRtNCEchLwEdW1dPAQpdFRcSGV5WBgkeXB83CBYACFkmFAVcHzcIHlEfKAgXSEtuGRZWRm4GE1xfOkACDFZGbhsJXF86XxkWVkZuAgsQGRpaGgERBF43EEldSxsYFhoTECo1GDkBVTkSIRNkAyQ1Ii5cEA1EQ2MsIDA6PGgZUAc9HAETElszaCEwNEdmIysgWzxZQw89QxooJBAoOFgfEywxAF8uKiJMTDwSJy1fBg8dVT5eH1U4N0kELyZYPXIbBxcVWV43TzxcHjBHDg%3D%3D"
        }
    ],
    "overseas": 1
}
{
    "text": "刘德华全新献唱！人民日报杭州亚运会助威曲《登场》",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://cn-gddg-ct-01-12.bilivideo.com/upgcxcode/29/51/1272295129/1272295129-1-192.mp4?e=ig8euxZM2rNcNbRMhwdVhwdlhWKVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&mid=0&nbs=1&deadline=1768050701&gen=playurlv3&og=cos&oi=1782024106&trid=0000aac8ff1064594b30b8f4abe54c69511h&platform=html5&os=bcache&upsig=8da7020b8112991f60cfe3bced39b563&uparams=e,uipk,mid,nbs,deadline,gen,og,oi,trid,platform,os&cdnid=61312&bvc=vod&nettype=0&bw=1123066&build=0&dl=0&f=h_0_0&agrr=0&buvid=&orderid=0,1",
            "preview_url": "http://i2.hdslb.com/bfs/archive/735eb6e0c7b3d80f77f6efb184821305b94e906d.jpg"
        }
    ],
    "overseas": 0
}
{
    "text": "Angry car https://t.co/GbkwIDEGEX",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://video.twimg.com/ext_tw_video/1924691978786373636/pu/vid/avc1/720x1278/pHT_GN4OO64wZYP6.mp4?tag=12",
            "preview_url": "https://pbs.twimg.com/ext_tw_video_thumb/1924691978786373636/pu/img/-P0J21FzJQl1C4qK.jpg"
        }
    ],
    "overseas": 1,
    "id": "1924692026383335840",
    "created_at": "Tue May 20 05:01:52 +0000 2025",
    "stats": {
        "comment_count": 6,
        "like_count": 3308,
        "play_count": null,
        "share_count": 319
    },
    "user": {
        "username": "TheCatsX",
        "image_url": "https://pbs.twimg.com/profile_images/2007846404929245184/sAN8YnzL_normal.png",
        "id": "868354704",
        "nickname": "The Cats 𝕏",
        "biography": "Your Daily Dose of Cats",
        "post_count": 11530,
        "following_count": 10,
        "followers_count": 231056,
        "created_at": "Mon Oct 08 17:25:41 +0000 2012",
        "banner_url": "https://pbs.twimg.com/profile_banners/868354704/1693697154",
        "verified": true
    }
}
{
    "text": "Florence, 1501. Going head-to-head, Michelangelo and Leonardo – two very different men - will use all their creativity to push each other to extraordinary new heights, and create some of the most brilliant art the world has ever seen.\n\n📺 Renaissance: The Blood and the Beauty - the epic new three-part drama-documentary series, starring Charles Dance as Michelangelo - is on #iplayer now. And new episodes are on #bbctwo, Mondays at 21:00. | BBC Arts",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://video-hou1-1.xx.fbcdn.net/o1/v/t2/f2/m366/AQNRNKBhH0JriXcYEHK3Bg_c9a-_yiVpEFq585vUgQZjF2T0lGZ1EKBzQ23jEQSRnsQI8vZW4wL-Wt9nzuFlNqka_N2aT0FSJ8hRMQd6J5DRpg.mp4?_nc_cat=101&_nc_sid=5e9851&_nc_ht=video-hou1-1.xx.fbcdn.net&_nc_ohc=4Tk8tQNU1ykQ7kNvwE54Mis&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5GQUNFQk9PSy4uQzMuNzE2LmRhc2hfaDI2NC1iYXNpYy1nZW4yXzcyMHAiLCJ4cHZfYXNzZXRfaWQiOjU2Mzg0MDQxMzAyOTA2NiwiYXNzZXRfYWdlX2RheXMiOjM5MywidmlfdXNlY2FzZV9pZCI6MTAxMjIsImR1cmF0aW9uX3MiOjE0MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=909cddc8b79cb5c1&_nc_vs=HBksFQIYRWZiX2VwaGVtZXJhbC80MjREOEIyQzZDNTE2MDk2ODY5Mjc2QTk0RjE4OTY4Rl9tdF8xX3ZpZGVvX2Rhc2hpbml0Lm1wNBUAAsgBEgAVAhg1ZmJfcGVybWFuZW50LzE3NTE5OTcxNTIyNDQzNDZfODM1NzA3MDgxNTY4MjkxOTQyNi5tcDQVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAmlMu6uOqzgAIVAigCQzMsF0BhgAAAAAAAGBlkYXNoX2gyNjQtYmFzaWMtZ2VuMl83MjBwEQB1AmWUngEA&_nc_gid=-lCI2G55stjtknzu1D1UsQ&_nc_zt=28&oh=00_Afqff75j_XYokWJ-_9AB0nk3DPWo_DrRM_WxlDX2vnt0JQ&oe=6967FD4B&bitrate=744868&tag=dash_h264-basic-gen2_720p&dl=1",
            "preview_url": "https://scontent-hou1-1.xx.fbcdn.net/v/t15.5256-10/470038362_1086079176330287_5496252946760869303_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=596eb7&_nc_ohc=uIOmKphOVAkQ7kNvwGmZosl&_nc_oc=AdmkkvLfnsFOXYqHDoVrmX-jkQvzCCJ0adPzCIe9gi5KzWxGWZE2RRt3xpoHVk2c5Ws&_nc_zt=23&_nc_ht=scontent-hou1-1.xx&_nc_gid=zlbSJcx-RBtbQJWLdtoniQ&oh=00_AfpTCCqV_QXfk6Bo5hfSrajPa-HS9JDgfw0OdA47IivkQQ&oe=6967F251"
        }
    ],
    "overseas": 1
}
{
    "text": "hydrodynamica's Post",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://instagram.fiev22-2.fna.fbcdn.net/o1/v/t2/f2/m82/AQN5Zfeqq2fZi-FBOJNEGyu-dzWvA9-htQ4ZVuFu2wyqK5p9ZJSMbhQ-rgL4AYTmkDi-239JqNW45FftSH_axnlkuIuu69SflxE1Ud0.mp4?_nc_cat=102&_nc_oc=Adm16ZC24kkjxaBmPcdf_ZyDh8otvkQdnutHMQwhyCHa5W3xzt9C7gT03UQjVR_L3G8&_nc_sid=5e9851&_nc_ht=instagram.fiev22-2.fna.fbcdn.net&_nc_ohc=XYRQMLyJ1NgQ7kNvwFYfFwK&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uQ0xJUFMuQzMuMTA4MC5kYXNoX2Jhc2VsaW5lXzFfdjEiLCJ4cHZfYXNzZXRfaWQiOjcwMzkwNjI5MTI4MjE1NTEsImFzc2V0X2FnZV9kYXlzIjo3ODQsInZpX3VzZWNhc2VfaWQiOjEwMDk5LCJkdXJhdGlvbl9zIjo1NSwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&_nc_gid=5Ya6nRy_lQQhJ3pLJwaX8w&_nc_zt=28&vs=fdca3573d650538b&_nc_vs=HBkcFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC80QTRFOTk1Q0ZFMTkzOTM5OTk0RkRDQUM2Nzk2NDhCMl92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm3qTDx7H_gBkVAigCQzMsF0BLjEm6XjU_GBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX-B2XmnQEA&oh=00_Afq1pZuLU9ZDCjkUCRbL-wTipg955PCkz2AIkQ7ANDuF-w&oe=696394A7",
            "preview_url": "https://instagram.fiev22-1.fna.fbcdn.net/v/t51.2885-15/502124948_23875896725378239_7892676189851508448_n.jpg?stp=dst-jpg_e15_tt6&_nc_ht=instagram.fiev22-1.fna.fbcdn.net&_nc_cat=107&_nc_oc=Q6cZ2QHjVWuM_I9o3gadX7dyA-5KqIIOYGf8Wlj1TALSdgwNLioD1Qjwz8asUrma1WFowSI&_nc_ohc=ijVs4VBjC-oQ7kNvwFrPAy1&_nc_gid=5Ya6nRy_lQQhJ3pLJwaX8w&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfrtOKsEU89wxjG2HVMHSZGGdSte4II88VwNLkAO9hfAjA&oe=69679BF1&_nc_sid=d885a2"
        }
    ],
    "overseas": 1
}
{
    "text": "Attention",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "http://vodkgeyttp8.vod.126.net/cloudmusic/MCEgMjJgIGIwYDAzIDAlYA==/mv/5499051/f4f358c7f0ac3555caa6f1a9c404359f.mp4?wsSecret=b6fc22c7dbf434eee261ff92cdd31308&wsTime=1768043509",
            "preview_url": "http://p1.music.126.net/dBbwDNVKp9DizHd_qo4aiQ==/18534467511312557.jpg",
            "formats": [
                {
                    "quality": 1080,
                    "quality_note": "1080p",
                    "video_url": "http://vodkgeyttp8.vod.126.net/cloudmusic/MCEgMjJgIGIwYDAzIDAlYA==/mv/5499051/f4f358c7f0ac3555caa6f1a9c404359f.mp4?wsSecret=b6fc22c7dbf434eee261ff92cdd31308&wsTime=1768043509",
                    "video_ext": "mp4",
                    "separate": 0
                },
                {
                    "quality": 720,
                    "quality_note": "720p",
                    "video_url": "http://vodkgeyttp8.vod.126.net/cloudmusic/MCEgMjJgIGIwYDAzIDAlYA==/mv/5499051/c7af71d0c8482557ac0541ab2c38ec40.mp4?wsSecret=ffdc15bfbd1a283d3c0320656f72d6bb&wsTime=1768043509",
                    "video_ext": "mp4",
                    "separate": 0
                },
                {
                    "quality": 480,
                    "quality_note": "480p",
                    "video_url": "http://vodkgeyttp8.vod.126.net/cloudmusic/MCEgMjJgIGIwYDAzIDAlYA==/mv/5499051/14acae4553af257d638fc1ba38c6af4d.mp4?wsSecret=385d4570e7fa9024e6d69b52a35b0967&wsTime=1768043509",
                    "video_ext": "mp4",
                    "separate": 0
                },
                {
                    "quality": 240,
                    "quality_note": "240p",
                    "video_url": "http://vodkgeyttp8.vod.126.net/cloudmusic/MCEgMjJgIGIwYDAzIDAlYA==/mv/5499051/b26180b7dcf61c32498c51609230a132.mp4?wsSecret=d7b7a66d50bf0a36f6d710af369c2f44&wsTime=1768043509",
                    "video_ext": "mp4",
                    "separate": 0
                }
            ],
            "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36"
            }
        }
    ],
    "overseas": 0,
    "id": "5499051",
    "stats": {
        "comment_count": 8255,
        "like_count": 162491,
        "play_count": null,
        "share_count": null,
        "view_count": 12813224
    }
}
{
    "text": "Are You Lost",
    "medias": [
        {
            "media_type": "audio",
            "resource_url": "http://m7.music.126.net/20260110193650/8ca1c62b4ffd53de0f9bc2413c424323/ymusic/obj/w5zDlMODwrDDiGjCn8Ky/3700897762/c5c0/999d/090f/9aaa114880919c9ce6a6e28aa2c9e3dc.mp3?vuutv=GoAIzPM+t9RjLZ0nrjFi0xjhW68QzK3oIgFPittRJzZuwr+zfPvAexRr5GdGoKAb1N6nMvsnLMzghOL9lKMbftp7Q01En75P+J+Ue8QgKps=",
            "preview_url": "http://p2.music.126.net/B0hvMNWSoxW5jMc9kgS5xA==/109951165076735700.jpg",
            "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-us,en;q=0.5",
                "Sec-Fetch-Mode": "navigate",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4556.0 Safari/537.36"
            }
        }
    ],
    "overseas": 0,
    "id": "518894020",
    "created_at": "1509984000",
    "stats": {
        "comment_count": 0,
        "like_count": 0,
        "play_count": null,
        "share_count": null,
        "view_count": 0
    }
}
```
