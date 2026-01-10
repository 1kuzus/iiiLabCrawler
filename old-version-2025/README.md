# iiiLabCrawler

`A web crawler for the video parsing API of iiilab.com`

[简体中文](README_zh.md)

## Introduction

This repository is a Python web crawler for the video parsing API of [iiilab.com](https://iiilab.com/), a website that
supports parsing and downloading video links from multiple platforms.

Update: The video parsing API for some platforms is now redirected to [snapany.com](https://snapany.com/). The old
version of the API used front-end parameter encryption, while the new version uses front-end signature verification.
The crawler scripts for the old version can be found in the `old-version-2024`.

Currently, the script supports only TikTok/Douyin, YouTube, Bilibili, Facebook, Instagram, and X/Twitter platforms. If
you only need to parse and download a single video, you can simply use the original website:

- [snapany.com (TikTok/Douyin, YouTube, Bilibili)](https://snapany.com/)
- [facebook.iiilab.com (Facebook)](https://facebook.iiilab.com/)
- [instagram.iiilab.com (Instagram)](https://instagram.iiilab.com/)
- [twitter.iiilab.com (X/Twitter)](https://twitter.iiilab.com/)

## Preparation

```
git clone https://github.com/1kuzus/iiiLabCrawler.git
pip install requests
```

## Usage

```python
from iiilab import get_resource, YOUTUBE

url = "https://www.youtube.com/watch?v=..."
res = get_resource(url=url, SITE=YOUTUBE)
```

Set `url` to the resource link, and set `SITE` to the constant for the corresponding site, which can be imported
directly from `iiilab.py`.

If the request fails, `get_resource` will return `None` and prints the error details. Otherwise, it parses and returns
the response as JSON.

If you want to add support for more platforms, simply refer to `iiilab.py` and add the corresponding `SITE` constant
(provided that the original website supports parsing for those platforms).

## Demo

See `demo.py` for an example:

```python
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

```

You will get the output:

```
{
    "text": "\u56db\u5e74\u4e86\uff0c\u98ce\u5439\u8fc7\u7a3b\u7530\uff0c\u4f9d\u7136\u60f3\u5ff5\u60a8\u3002\u7f05\u6000\u8881\u8001\uff01",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://v9-default.365yg.com/9d4f3f550765d0fe31b532c9ad3b3bd5/682f3d65/video/tos/cn/tos-cn-ve-15/osAue2Egtt4faWdG0ZCM2AADMYC8ARx57ifjQf/?a=2011&ch=0&cr=0&dr=0&er=0&lr=unwatermarked&net=5&cd=0%7C0%7C0%7C0&cv=1&br=1250&bt=1250&cs=0&ds=4&ft=k7Fz7VVywIiRZm8Zmo~pK7pswApZvN3UvrKsyUc2do0g3cI&mime_type=video_mp4&qs=0&rc=aGk8aGY8ZWhpOmg0MzQ6aEBpamV3NnA5cmx5MzMzNGkzM0BfNTJeYzMuNjYxYS80YWIwYSMuazBnMmQ0amphLS1kLTBzcw%3D%3D&btag=c0000e00020000&dy_q=1747922721&feature_id=46a7bb47b4fd1280f3d3825bf2b29388&l=2025052222052113BFD814FC4F4DFEFE94",
            "preview_url": "https://p11-sign.douyinpic.com/tos-cn-p-0015/osG2atIZeOYtubM6DxaRe9AQGeAZLCBW3E4gfQ~tplv-dy-360p.webp?lk3s=138a59ce&x-expires=1749132000&x-signature=OwtKgpjK6NsleljE0m%2FcwJuJ0W8%3D&from=327834062&s=PackSourceEnum_FEED&se=false&sc=origin_cover&biz_tag=aweme_video&l=202505222205196F06DFB7D8ADAD115103"
        }
    ]
}
{
    "text": "The incredible ibex defies gravity and climbs a dam | Forces of Nature with Brian Cox - BBC",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://redirector.googlevideo.com/videoplayback?expire=1747937849&ei=2RUvaK7tEL_-i9oPt_PLwQc&ip=176.1.151.103&id=o-AAXb0pQe7BgHZB9W1lYpeOGX3K9pEqLsVI4UmvP0MfiK&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1747916249%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=1&pl=17&rms=au%2Cau&initcwndbps=1613750&bui=AecWEAa10E7m8x72t_Y7gSy-qki7E6fBG04Kb5iXvwjMnvzsOEo3AwD43Alzf6N3vu2kFKImbsbNmzBm&spc=wk1kZo2uEhDv87em2RvMqfmYNsH-Y8MREUKKdeCKGOB4dWyV6nTG7-0&vprv=1&svpuc=1&mime=video%2Fmp4&ns=yUQRgsCqgQdrNlmm5dTyhKcQ&rqh=1&gir=yes&clen=16332781&ratebypass=yes&dur=232.408&lmt=1725424927317407&mt=1747915746&fvip=3&fexp=51331020%2C51466697&c=MWEB&sefc=1&txp=4538434&n=h2rx3xxSVVMaVQ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAKExozzC3OFuILatThiZtNN1ldLsklAayFlgLgWdNePuAiAwSDm0-kfqKNvBJv8EHXTdggRzH3LeuR5JQJU37aPL5A%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRAIgAUvb1W-jBbcQJFfy62DtF5sXE8Apk8ySz9aiEKVXm58CICZwe1LfrRqgHsD_GpFfYqPNjbBroq6UK8HrLYuagS5N&pot=MnRwLRiQ9UeN6HARYvwv3wC0CbUeWxa2wG90GlTIPthvJlF862hho6oaTLeJg8TVSiXPNvsPk0Ge_2MDQrgeIMZR0g-WtsftrFI2N4biWdt94zCeRA7CpR9epc9kyPACP3b6OuJsrmvX0O2OBOjKiThLNC8ttg==",
            "preview_url": "https://i.ytimg.com/vi/RG9TMn1FJzc/hq720.jpg?sqp=-oaymwEcCK4FEIIDSEbyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCmpuMp57ew0t_Rs82jRo4O-4kQXw",
            "formats": [
                {
                    "quality": 1080,
                    "video_url": "https://rr1---sn-uxax4vopj5qx-q0n6.googlevideo.com/videoplayback?expire=1747937849&ei=2RUvaK7tEL_-i9oPt_PLwQc&ip=176.1.151.103&id=o-AAXb0pQe7BgHZB9W1lYpeOGX3K9pEqLsVI4UmvP0MfiK&itag=137&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399%2C597%2C598&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1747916249%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=1&pl=17&rms=au%2Cau&initcwndbps=1613750&bui=AecWEAbC5kNWvTTdIlNwEdZ_aTp7NPKnxd7qAtdvOLbwrpBc5LZZWIcsS3Zd-Euwkms_QPLlqBsjnEsI&spc=wk1kZo2tEhDv87em2RvMqfmYNsH-Y8MREUKKdeCKGOB4dWyV6kTD&vprv=1&svpuc=1&mime=video%2Fmp4&ns=Y96ef233er1HQHSjuVoJctEQ&rqh=1&gir=yes&clen=56556197&dur=232.360&lmt=1725425356139113&mt=1747915746&fvip=3&keepalive=yes&fexp=51331020%2C51466697&c=MWEB&sefc=1&txp=4532434&n=fhhBs-EYZS518Q&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIgXqCl0l1DmC2YGPslynXdbzotWDbuGgAwNjrFt0SpwV0CIQDcxtyQoZUsYWMHr3DOrWQTaQOkOv1jaHczoSfujgrPhw%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRAIgAUvb1W-jBbcQJFfy62DtF5sXE8Apk8ySz9aiEKVXm58CICZwe1LfrRqgHsD_GpFfYqPNjbBroq6UK8HrLYuagS5N&pot=MnRwLRiQ9UeN6HARYvwv3wC0CbUeWxa2wG90GlTIPthvJlF862hho6oaTLeJg8TVSiXPNvsPk0Ge_2MDQrgeIMZR0g-WtsftrFI2N4biWdt94zCeRA7CpR9epc9kyPACP3b6OuJsrmvX0O2OBOjKiThLNC8ttg==",
                    "video_ext": "mp4",
                    "video_size": 56556197,
                    "separate": 1,
                    "quality_note": "1080p",
                    "alternate_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkdDFFlXTl9KHUZXUVgPHhcVT0MPHBEHBF5RSlYfCxxZSF4HQ0YQAQwBGQIKAx4YGh1UHElDQksUG0IMCRwbEEkRCl0XQgZKDwQdSBsVHxVUCQQaBkZIDBUaBkhWVE5ZThRHUktAFDcQSV1LGxEMTkZ%2FPhMYJk5ZMSksWURSCikZJn04EiIXcR5VSV9PRARYQkMbRVRXXEwcWlRDR3EeVUlfT0QQWBxZbCo9G10JfBFSMRNlMSdAOkhBLRUWO2ozVjJUCWgFKQAiZF8wFBspHTkDGj9xHlVJX09EAAQUSRxYUiUYSR1GUxIdWQoCClBIHkdAQTccWFFcXzocR1BWRm5aVk9IS25FVkRRHyhUT11cHzdXR0YIWSZLWUoIRiZBQBlOVzpfTRpRVzBGGVNASy5LGkxAQTceUlFcXzoeTVBWRm5YXE9IS25HXERRHyhWQFVcHzdWSk0IWSZMVE4IRiZGTRU3EEldSxsHCgYGTg5YAAIMWQEHFihYW1VLWwtIBRAaBkgYFhVQAEgHOQZEHVlTAR0aEDECJRsfCiEqIygIRyFWR2k3EEldSxsZAAdJHFxRTlRIG0ZRSlEfKDkMXUkfQggbSX5GOQxdSR9CCB5JHlpASy5LFCgQQ0QfXQgXUApDWRALFVVfExYdExgFHV4FHQVTXF86XhpIRxMYDgEXCU5xAVVDRhsGFkQMDAhGJgEQWDcQSV1LGxkTThlxHlVJX09AAgxORXEeVUlfT10YWEJDcR5VSV9PXxkWThVYTlc6DAxxAVVDRhsCCxAZGloaAREEXlZUT1xKGkFVLwEdW1dPDwxESSQWF3ouJBsuTEY6MgUgeQ8sFSMOaBA%2FLBV5G1I3PTJDDAFEBWwfAQ8iNU8DFwM2Tl4pIzcuZBcWIEd3D0g8GA5GGRYsJX0nCQgvCkcaIAA9cR5VSV9PXgQGTgNGWg4jAktZMQ03AhVcABRfK1s5FBUZdCUWMUAgFTk3NiFmIAEcLjJqOydHEHoSM08GLWkoEENEH10TCR8PEEU5BkQdWVMKGwlYF1hCKFhbVUtbFEQZAE4CRA8AFkhLaxkVRyhYW1VLWxdeSTxKQkgNV0peHF9FLSI8fgEQLwIzTgAgIihYW1VLWwtcHFhCKFhbVUtbHkQGWAoRXjcQSV1LGxcJFhoQXlNMWE8cTVIvAR1bV08JDF9JV0BGA1hTSTEMHURXRRhAH1hIWksYQFdGRxhdVEpUSBxHOQZEHVlTFBlEHENRRE0cXlJNWyVYRFVBQksdDAlQSnEBVUNGGwAAHB0YQR0TFklUDhYlGEkdRlMVEVUbWExcSh5FVUFECFkmTFxNG0JTSkNxHlVJX09OSSgkMW83EEldSxsHABUXEFo5DF1JH0IRCwQQX1BKX00eQDkGRB1ZUxdQH0UcJwBZaDI%2FKlhIFSU5BkQdWVMKHRhfFQgASUgTFRAfHAhGJhYdCFkmEB1cHzcMF1EfKAQQGRhKB0BBN14EEAsOHAhGJgERXB4MCwgKXhhAQTdVGwZcXzpPAQxWRm4YFRpIS24CFQECCFkmChsJWBdAQTdAAggcSEtuGhZWRm4ZFBFIS24TDAFRHygGFQgXCEYmFwFfTlc6ARRZKBBDRB9dFhAKRGw%2BAyIQfhgSKzwwSiwUMBgdB1Q9ADofLSIjB0ESCyEJG1cbESQwTx4iHiwOYx4XNQAdOBUOO0luPTQ3F1UfHCgCI3gHPCQ5ZRlWPSILeiUxEiViACoPXBNMPAYJG34NEBMKC30cElZHaU5WPTEMHURXRRheGwQLDBReSQgWAAhZJhQFXB83CB5RHygIF0hLbhkWVkZuBhNcXzpAAgxWRm4bCVxfOl8ZFlZGbgILEBkaWhoBEQReNxBJXUsbGBYaExAqJgwFNHhEEiE1ZAwkLBsbHCNIGTZPCDQzKx9UQlc3AGteFiEoQWwEDksNfhFcGAQ8ZiI9HkEVKCw6Nw5IRSkVBn8aAjEePXIzFTUSdBo1NwcbbwYKAkJ4IF0xHzV0AQQUJxglOQxdSR9CFRwAECYLKxo1fx00SiFIJVMxLCt0AhIFR1ooVToPLEgjHRJGWixcSSoVeT01BxxbIQk%2FVU8fHA0cQkIKMTUIM0pMMSUnRDM1NxsKfR9VNBFyWSg9PAtKESw%2BLn9bAlQ6DV4SEQEyZFkrTQ8QehARSkBXKAArLE5uBDdKEV0IXBIUKWw3NUAWGyQQMx4LQAI9QzsfJCc2BzJEIA0%2FOm5TEQ0KRBBWGA%3D%3D"
                },
                {
                    "quality": 720,
                    "video_url": "https://rr1---sn-uxax4vopj5qx-q0n6.googlevideo.com/videoplayback?expire=1747937849&ei=2RUvaK7tEL_-i9oPt_PLwQc&ip=176.1.151.103&id=o-AAXb0pQe7BgHZB9W1lYpeOGX3K9pEqLsVI4UmvP0MfiK&itag=136&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399%2C597%2C598&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1747916249%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=1&pl=17&rms=au%2Cau&initcwndbps=1613750&bui=AecWEAbC5kNWvTTdIlNwEdZ_aTp7NPKnxd7qAtdvOLbwrpBc5LZZWIcsS3Zd-Euwkms_QPLlqBsjnEsI&spc=wk1kZo2tEhDv87em2RvMqfmYNsH-Y8MREUKKdeCKGOB4dWyV6kTD&vprv=1&svpuc=1&mime=video%2Fmp4&ns=Y96ef233er1HQHSjuVoJctEQ&rqh=1&gir=yes&clen=18194126&dur=232.360&lmt=1725425255555336&mt=1747915746&fvip=3&keepalive=yes&fexp=51331020%2C51466697&c=MWEB&sefc=1&txp=4532434&n=fhhBs-EYZS518Q&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRgIhAPEGcGYsA2VFeThfXyM9j4LYDDicAz376ViFFEO18OgVAiEAs4xYxMCDxXqH_2zpIcyqUI35OeqjjW7JeFWJ1bjnQFc%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRAIgAUvb1W-jBbcQJFfy62DtF5sXE8Apk8ySz9aiEKVXm58CICZwe1LfrRqgHsD_GpFfYqPNjbBroq6UK8HrLYuagS5N&pot=MnRwLRiQ9UeN6HARYvwv3wC0CbUeWxa2wG90GlTIPthvJlF862hho6oaTLeJg8TVSiXPNvsPk0Ge_2MDQrgeIMZR0g-WtsftrFI2N4biWdt94zCeRA7CpR9epc9kyPACP3b6OuJsrmvX0O2OBOjKiThLNC8ttg==",
                    "video_ext": "mp4",
                    "video_size": 18194126,
                    "separate": 1,
                    "quality_note": "720p",
                    "alternate_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkdDFFlXTl9KHUZWUVgPHhcVT0MPHBEHBF5RSlYfCxxZSF4HQ0YQAQwBGQIKAx4YGh1UHElDQksUG0IMCRwbEEkRCl0XQgZKDwQdSBsVHxVUCQQaBkZIDBUaBkhWVE5ZThRHUktAFDcQSV1LGxEMTkZ%2FPhMYJk5ZMSksWURSCikZJn04EiIXcR5VSV9PRARYQkMbRVRXXEwcWlRDR3EeVUlfT0QQWBxZbCo9G10JfBFSMRNlMSdAOkhBLRUWO2ozVjJUCWgFKQAiZF8wFBspHTkDGj9xHlVJX09EAAQUSRxYUyUYSR1GUxIdWQoCClBIHkdAQTccWFFcXzocR1BWRm5aVk9IS25FVkRRHyhUT11cHzdXR0YIWSZLWUoIRiZBQBlOVzpfTRpRVzBGGVNASy5LGkxAQTceUlFcXzoeTVBWRm5YXE9IS25HXERRHyhWQFVcHzdWSk0IWSZMVE4IRiZGTRU3EEldSxsHCgYGTg5YAAIMWQEHFihYW1VLWwtIBRAaBkgYFhVQAEgHOQZEHVlTAR0aEDECJRsfCiEqIygIRyFWR2k3EEldSxsZAAdJHFxRTlRIG0ZRSlEfKDkMXUkfQggbSX5GOQxdSR9CCB5JHlpASy5LFCgQQ0QfXQgXUApDWRALFVVfExYdExgFHV4FHQVTXF86XhpIRxMYDgEXCU5xAVVDRhsGFkQMDAhGJgEQWDcQSV1LGxkTThlxHlVJX09AAgxORXEeVUlfT10YWEJDcR5VSV9PXxkWThVYTlc6DAxxAVVDRhsCCxAZGloaAREEXlZUT1xKGkFVLwEdW1dPDwxESSQWF3ouJBsuTEY6MgUgeQ8sFSMOaBA%2FLBV5G1I3PTJDDAFEBWwfAQ8iNU8DFwM2Tl4pIzcuZBcWIEd3D0g8GA5GGRYsJX0nCQgvCkcaIAA9cR5VSV9PXgQGTgNGWg4jAktZMQ03AhVcABRfK1s5FBUZdCUWMUAgFTk3NiFmIAEcLjJqOydHEHoSM08GLWkoEENEH10TCR8PEEU5BkQdWVMKGwlYF1hCKFhbVUtbFEQZAE4CRA8AFkhLaxkVRyhYW1VLWxdeSTxKQkgNV0peHF9FLSI8fgEQLwIzTgAgIihYW1VLWwtcHFhCKFhbVUtbHkQGWAoRXjcQSV1LGxcJFhoQWl1IVE0cRlMvAR1bV08JDF9JV0BGA1hTSTEMHURXRRhAH1hIWksYQFdGRhheUExYSh5COQZEHVlTFBlEHENRRE0cXlJNWyVYRFVBQksdDAlQSnEBVUNGGwAAHB0YQR0TFklUDhYlGEkdRlMVEVUbWExcSh5FVUFECFkmTFxNG0JTSkNxHlVJX09OSSgkMW83EEldSxsHABUXEFo5DF1JH0IRCwQQX1BKX00eQDkGRB1ZUxdQH0UcJwBZaDI%2FKlhIFSU5BkQdWVMKHRhfFQgASUgTFRAfHAhGJhYdCFkmEB1cHzcMF1EfKAQQGRhKB0BBN14EEAsOHAhGJgERXB4MCwgKXhhAQTdVGwZcXzpPAQxWRm4YFRpIS24CFQECCFkmChsJWBdAQTdAAggcSEtuGhZWRm4ZFBFIS24TDAFRHygGFQgXCEYmFwFfTlc6ARRZKBBDRB9dFhAKRGw%2BAyIQfhgSKwowRTU1NjNOLDwKLEt7MgAnHEszHDRUExk4PDcwRAgkA15OGyIMNTJoJFRBIh57NQw2NV5fHSAVNG4wHSsFZTRXAx0wTg0UJj0eXiocHBNHI1I5EWs8L0gPE0MlIxBRHi85DF1JH0IJAARMGQQUHkRAERFWRm4GDVxfOkAZQEE3QAVASy4UXlFXMBlbTlc6AA9EUVcwBEFOVzofFF5RVzAdQwIRGhoXSRYVAChYW1VLWxVeHQJONW4eDTQ4SVomJDoTbD4TG1wuAB4nERd8ISMfFE8fMBE1QV4zIEEsCUZMHCAOFAoMPCYvdRlQSzdkKD8OCEhhEhchBUojFj0yPl0yAyoFfSUPGy8LQgVTJj8VIxc1NAxMEzZGOnEeVUlfT10bEU45QzkSNT8QfE0wFjobIyQrNA9aAlYENx0oBywILlUVVwQzFFsiFTkwfQANBT5BLV1PXxFFG1McFXknADMKQXkiNhosfSUTCj0SHTMALEZgLzQLChxkOT8hREpGMg0eH1kGIzpGY18HEDodWU1RCTdIOSROLgl%2FTQADFxQAHCksOn1HB0U7WCEWCwAPdUQqQTtvJA8yBC1FOCswTFkfAkRQW1A%3D"
                },
                {
                    "quality": 480,
                    "video_url": "https://rr1---sn-uxax4vopj5qx-q0n6.googlevideo.com/videoplayback?expire=1747937849&ei=2RUvaK7tEL_-i9oPt_PLwQc&ip=176.1.151.103&id=o-AAXb0pQe7BgHZB9W1lYpeOGX3K9pEqLsVI4UmvP0MfiK&itag=135&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399%2C597%2C598&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1747916249%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=1&pl=17&rms=au%2Cau&initcwndbps=1613750&bui=AecWEAbC5kNWvTTdIlNwEdZ_aTp7NPKnxd7qAtdvOLbwrpBc5LZZWIcsS3Zd-Euwkms_QPLlqBsjnEsI&spc=wk1kZo2tEhDv87em2RvMqfmYNsH-Y8MREUKKdeCKGOB4dWyV6kTD&vprv=1&svpuc=1&mime=video%2Fmp4&ns=Y96ef233er1HQHSjuVoJctEQ&rqh=1&gir=yes&clen=9944950&dur=232.360&lmt=1725425253993160&mt=1747915746&fvip=3&keepalive=yes&fexp=51331020%2C51466697&c=MWEB&sefc=1&txp=4532434&n=fhhBs-EYZS518Q&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIgYr0BuT08YCr1iTCG598R1nPiasrP4nE9ZAm219bLGw8CIQDdUHHsmQoHxWeS9cPxPqsbToX3cKO789J6s5ue84saMQ%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRAIgAUvb1W-jBbcQJFfy62DtF5sXE8Apk8ySz9aiEKVXm58CICZwe1LfrRqgHsD_GpFfYqPNjbBroq6UK8HrLYuagS5N&pot=MnRwLRiQ9UeN6HARYvwv3wC0CbUeWxa2wG90GlTIPthvJlF862hho6oaTLeJg8TVSiXPNvsPk0Ge_2MDQrgeIMZR0g-WtsftrFI2N4biWdt94zCeRA7CpR9epc9kyPACP3b6OuJsrmvX0O2OBOjKiThLNC8ttg==",
                    "video_ext": "mp4",
                    "video_size": 9944950,
                    "separate": 1,
                    "quality_note": "480p",
                    "alternate_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkdDFFlXTl9KHUZWUVgPHhcVT0MPHBEHBF5RSlYfCxxZSF4HQ0YQAQwBGQIKAx4YGh1UHElDQksUG0IMCRwbEEkRCl0XQgZKDwQdSBsVHxVUCQQaBkZIDBUaBkhWVE5ZThRHUktAFDcQSV1LGxEMTkZ%2FPhMYJk5ZMSksWURSCikZJn04EiIXcR5VSV9PRARYQkMbRVRXXEwcWlRDR3EeVUlfT0QQWBxZbCo9G10JfBFSMRNlMSdAOkhBLRUWO2ozVjJUCWgFKQAiZF8wFBspHTkDGj9xHlVJX09EAAQUSRxYUCUYSR1GUxIdWQoCClBIHkdAQTccWFFcXzocR1BWRm5aVk9IS25FVkRRHyhUT11cHzdXR0YIWSZLWUoIRiZBQBlOVzpfTRpRVzBGGVNASy5LGkxAQTceUlFcXzoeTVBWRm5YXE9IS25HXERRHyhWQFVcHzdWSk0IWSZMVE4IRiZGTRU3EEldSxsHCgYGTg5YAAIMWQEHFihYW1VLWwtIBRAaBkgYFhVQAEgHOQZEHVlTAR0aEDECJRsfCiEqIygIRyFWR2k3EEldSxsZAAdJHFxRTlRIG0ZRSlEfKDkMXUkfQggbSX5GOQxdSR9CCB5JHlpASy5LFCgQQ0QfXQgXUApDWRALFVVfExYdExgFHV4FHQVTXF86XhpIRxMYDgEXCU5xAVVDRhsGFkQMDAhGJgEQWDcQSV1LGxkTThlxHlVJX09AAgxORXEeVUlfT10YWEJDcR5VSV9PXxkWThVYTlc6DAxxAVVDRhsCCxAZGloaAREEXlZUT1xKGkFVLwEdW1dPDwxESSQWF3ouJBsuTEY6MgUgeQ8sFSMOaBA%2FLBV5G1I3PTJDDAFEBWwfAQ8iNU8DFwM2Tl4pIzcuZBcWIEd3D0g8GA5GGRYsJX0nCQgvCkcaIAA9cR5VSV9PXgQGTgNGWg4jAktZMQ03AhVcABRfK1s5FBUZdCUWMUAgFTk3NiFmIAEcLjJqOydHEHoSM08GLWkoEENEH10TCR8PEEU5BkQdWVMKGwlYF1hCKFhbVUtbFEQZAE4CRA8AFkhLaxkVRyhYW1VLWxdeSTxKQkgNV0peHF9FLSI8fgEQLwIzTgAgIihYW1VLWwtcHFhCKFhbVUtbHkQGWAoRXjcQSV1LGxcJFhoQUlxNWUAYRDkGRB1ZUx0YCxBGVkFaHl1VJRhJHUZTHxlZVlROX0wZRlBBQR5SXEpcTx0oEENEH10IDVBIGkBSSkUYXFFPMQwdRFdFElsCFUReJVhEVUFCRg4ACQwVRAIATg1IGDkMXUkfQgMWDF1WUEheShxEV0NRHyhQSFlPG0JcRChYW1VLWxoQOTI2NnEeVUlfT14RAxBJHDcQSV1LGwAdA0kZXlZLWUoZKBBDRB9dC0QLEUU2Fl4xdDE2TFxBfCgQQ0QfXRYJDAtMGRZOEVUbDAsIXB83ABpRHygMCUhLbh0BVkZuCgwNDB5eUVcwB0IeFxoIXB83FxYFWAIXHB4KQVFXMAxdCEBLLhtYHUBBN14bBlxfOlsEFwVRHygWDx0MTlFXMBlEBgBcXzpDB0BBN18aDVxfOkodF1ZGbggJHANcHzcBBgYIWSYVAA1xAVVDRhsYDB5QOGcSNBcnXhw3KCQedAZVMQF5W10gLgscHTEwMxhSXStcF30dBAAGfV8LPFQjbBlXQk1PJyIOVTpkJSEXIWUjFhQ8FmUMMhYnFAg1AT0IXhYxHCweCC42WkEUPlMAQVgOXU0eGGAlQEAwCFghJRhJHUZTHwddChcYAAoQGQAHUR8oCBFIS24ZCFZGbgYLXF86QAdAQTdAHUBLLhRbHUBBN10HQEsuC0AHQEE3RAUMDQ4OQxAHAwdxHlVJX09BBwwUSWwoEBEgLB0DNzI9SiowDw9IelkPMRZOOi8%2FCwAbRiEHMhgYPTxVOF0fXQonV1IEECgyeywIRkxuIiYjGhwcOAMBJlwMLQopJmoEIxUtXDsrEw87XxsURSFmUy0LISBYFQIgQWM3EEldSxsECgdJYAU3DiErRCVcJhFjXS04PyBbAxNAA25bJhs4HHoMBEEDalJVPgEtZCQRGwJnByNBW0tFHApFG0w%2FKRwnHhUgMyAddTsrDx4pRkQiFisfJiEoHx5IPSgpJh0MSC4ZCksAFzU9HyVRGwQuSQBcRw5uDjc4WjpdJlwWBE5SDgA9OG4kVhFCYh4vCh8UWyxVPEZiKSoTJhB5HCk9NxUfER5QRA8J"
                },
                {
                    "quality": 360,
                    "video_url": "https://redirector.googlevideo.com/videoplayback?expire=1747937849&ei=2RUvaK7tEL_-i9oPt_PLwQc&ip=176.1.151.103&id=o-AAXb0pQe7BgHZB9W1lYpeOGX3K9pEqLsVI4UmvP0MfiK&itag=18&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1747916249%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=1&pl=17&rms=au%2Cau&initcwndbps=1613750&bui=AecWEAa10E7m8x72t_Y7gSy-qki7E6fBG04Kb5iXvwjMnvzsOEo3AwD43Alzf6N3vu2kFKImbsbNmzBm&spc=wk1kZo2uEhDv87em2RvMqfmYNsH-Y8MREUKKdeCKGOB4dWyV6nTG7-0&vprv=1&svpuc=1&mime=video%2Fmp4&ns=yUQRgsCqgQdrNlmm5dTyhKcQ&rqh=1&gir=yes&clen=16332781&ratebypass=yes&dur=232.408&lmt=1725424927317407&mt=1747915746&fvip=3&fexp=51331020%2C51466697&c=MWEB&sefc=1&txp=4538434&n=h2rx3xxSVVMaVQ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIhAKExozzC3OFuILatThiZtNN1ldLsklAayFlgLgWdNePuAiAwSDm0-kfqKNvBJv8EHXTdggRzH3LeuR5JQJU37aPL5A%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRAIgAUvb1W-jBbcQJFfy62DtF5sXE8Apk8ySz9aiEKVXm58CICZwe1LfrRqgHsD_GpFfYqPNjbBroq6UK8HrLYuagS5N&pot=MnRwLRiQ9UeN6HARYvwv3wC0CbUeWxa2wG90GlTIPthvJlF862hho6oaTLeJg8TVSiXPNvsPk0Ge_2MDQrgeIMZR0g-WtsftrFI2N4biWdt94zCeRA7CpR9epc9kyPACP3b6OuJsrmvX0O2OBOjKiThLNC8ttg==",
                    "video_ext": "mp4",
                    "video_size": 16332781,
                    "separate": 0,
                    "quality_note": "360p",
                    "alternate_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkdDFFlXTl9KHUZWUVgPHhcVT0MPHBEHBF5RSlYfHEkdFxYXWQQXVwoWQhMJFgJEDwAWQxpCGUoFHUkOCgkBGFQWBBAfEg4dCQQLSElUREAaUlZOVU0UKBBDRB9dABBQS38hExI%2FGh8gNTJURE0KIwByOykOPBpxAVVDRhsCFURcThtaVF1FGFpLSF1KcQFVQ0YbAgFEAlRsNT0RRF06AE4vHmUuJ0ojHAc8CQg2aixWOE1dLhQ1Hi9kQDAeAn1bKB8EMnEBVUNGGwIRGApEHEw5BkQdWVMKAgxfFwBODUIeEQwPHHEBVUNGGxkACBgQXxEWABgQEgAKMQwdRFdFDF0IWDwKL0JGBDcnYzpASilcHjA5BkQdWVMUCA0QRVJHQxRaU0tZQAhGJi8BHVtXTwARECdILwEdW1dPABQQR1RWRm5ZXCUYSR1GUx4aEBgLVBgBTAxRBRtdAVAIFVRcRAtFUR8oFhdATUpBABcaSVw5DF1JH0IIAElMHkBLLgtJATkGRB1ZUxQbREAoEENEH10IDwREHCgQQ0QfXRUVUEgaKBBDRB9dFxQeREwBQEE3TB45DF1JH0IMHR1ZCBIXCRtdB1hCQhxYUkxdJVhEVUFCTx4MRCwcTiMgMhUcWyBOAEFVQ1cHK3RcAioUVFwfDEQxGw0nPl1NZhZQGixbHA80Aw9XByo2Gx4qEj1ZSmwYHxVCY1gTDF8Saz8sHhZeCSsUFztAKBBDRB9dFgkORFofVBguQlkQPAU9W0xSFhkfORM0HB9ALSsAPAAyXTQ%2FPHg%2FLhcRbiAiNi9NSSMcJUJDPyJOQElxAVVDRhsdFQsbRBwoEENEH10WDx0MTklULwEdW1dPABBAEVgFHUkOClxfP0AEUS8BHVtXTwMKEA0wIiZKGCYICihJBisfGUBeAS0UEWYXNC8BHVtXTx8IRUlULwEdW1dPChBfSRwWB3EeVUlfT04YAB1JHF1WSl9OFUU5BkQdWVMLDA1IFhwDFV4YWAAICnEBVUNGGw8QC1BLHkZLR0QVNxBJXUsbGAgHSRxcV0xZSxlNV0RHHFxRSVolWERVQUJAH1hIWk0aTVRGQxldOQxdSR9CAwUdXVZWJRhJHUZTFRFVG1hMXEoeRVVBRAhZJkxcTRtCU0pDcR5VSV9PTkkoJDFvNxBJXUsbBwAVFxBaOQxdSR9CEQsEEF9QSlVNHkA5BkQdWVMXUBEfBh1ADFU4My8gGHslOQZEHVlTCh0YXxUIAElIExUQHxwIRiYWHQhZJhAdXB83DBdRHygMDQweCEYmABtYGQYcSEtuBgACAUQZAAoeFQhGJgsETk5XOg8MRFFXMAddCEBLLg9dBhNWRm4YEwkYGghGJh4dQA5ASy4XXlFXMAZcA0BLLh5EBkBBN04HABdIS24GBAcRTxIVGB4KCEYmFwFfTlc6ARRZKBBDRB9dFhAKRGw%2BAyIQfhgSKzwwRTUuNgxCER86XjZrASw%2FFVk%2FDRA3DWM6VB8QYRgOFSwYVDIJFDhKPAE3CClYNQwyA34vCElAEksFLj0CbyETQSgxdSABFBN%2FES1KIRxYJlA5JWc%2BVk4MKWFBJFZHaU5WPTEMHURXRRheGwQLDBReSQgWAAhZJhQFXB83CB5RHygIF0hLbhkWVkZuBhNcXzpAAgxWRm4bCVxfOl8ZFlZGbgILEBkaWhoBEQReNxBJXUsbGBYaExAqJgwFNHhEEiE1ZAwkLBsbHCNIGTZPCDQzKx9UQlc3AGteFiEoQWwEDksNfhFcGAQ8ZiI9HkEVKCw6Nw5IRSkVBn8aAjEePXIzFTUSdBo1NwcbbwYKAkJ4IF0xHzV0AQQUJxglOQxdSR9CFRwAECYLKxo1fx00SiFIJVMxLCt0AhIFR1ooVToPLEgjHRJGWixcSSoVeT01BxxbIQk%2FVU8fHA0cQkIKMTUIM0pMMSUnRDM1NxsKfR9VNBFyWSg9PAtKESw%2BLn9bAlQ6DV4SEQEyZFkrTQ8QehARSkBXKAArLE5uBDdKEV0IXBIUKWw3NUAWGyQQMx4LQAI9QzsfJCc2BzJEIA0%2FOm5TEQ0KRBBWGA%3D%3D"
                },
                {
                    "quality": 240,
                    "video_url": "https://rr1---sn-uxax4vopj5qx-q0n6.googlevideo.com/videoplayback?expire=1747937849&ei=2RUvaK7tEL_-i9oPt_PLwQc&ip=176.1.151.103&id=o-AAXb0pQe7BgHZB9W1lYpeOGX3K9pEqLsVI4UmvP0MfiK&itag=133&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399%2C597%2C598&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1747916249%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=1&pl=17&rms=au%2Cau&initcwndbps=1613750&bui=AecWEAbC5kNWvTTdIlNwEdZ_aTp7NPKnxd7qAtdvOLbwrpBc5LZZWIcsS3Zd-Euwkms_QPLlqBsjnEsI&spc=wk1kZo2tEhDv87em2RvMqfmYNsH-Y8MREUKKdeCKGOB4dWyV6kTD&vprv=1&svpuc=1&mime=video%2Fmp4&ns=Y96ef233er1HQHSjuVoJctEQ&rqh=1&gir=yes&clen=3040395&dur=232.360&lmt=1725425259108255&mt=1747915746&fvip=3&keepalive=yes&fexp=51331020%2C51466697&c=MWEB&sefc=1&txp=4532434&n=fhhBs-EYZS518Q&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRAIgKuYbrwtXolBGiLehWyuMJbErvmDmRS_IYAvU5JwZ45gCICkjA84z9bxy7qqb1oG4y4bk-Jf9N2y2Soglbl02sLrV&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRAIgAUvb1W-jBbcQJFfy62DtF5sXE8Apk8ySz9aiEKVXm58CICZwe1LfrRqgHsD_GpFfYqPNjbBroq6UK8HrLYuagS5N&pot=MnRwLRiQ9UeN6HARYvwv3wC0CbUeWxa2wG90GlTIPthvJlF862hho6oaTLeJg8TVSiXPNvsPk0Ge_2MDQrgeIMZR0g-WtsftrFI2N4biWdt94zCeRA7CpR9epc9kyPACP3b6OuJsrmvX0O2OBOjKiThLNC8ttg==",
                    "video_ext": "mp4",
                    "video_size": 3040395,
                    "separate": 1,
                    "quality_note": "240p",
                    "alternate_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkdDFFlXTl9KHUZWUVgPHhcVT0MPHBEHBF5RSlYfCxxZSF4HQ0YQAQwBGQIKAx4YGh1UHElDQksUG0IMCRwbEEkRCl0XQgZKDwQdSBsVHxVUCQQaBkZIDBUaBkhWVE5ZThRHUktAFDcQSV1LGxEMTkZ%2FPhMYJk5ZMSksWURSCikZJn04EiIXcR5VSV9PRARYQkMbRVRXXEwcWlRDR3EeVUlfT0QQWBxZbCo9G10JfBFSMRNlMSdAOkhBLRUWO2ozVjJUCWgFKQAiZF8wFBspHTkDGj9xHlVJX09EAAQUSRxYViUYSR1GUxIdWQoCClBIHkdAQTccWFFcXzocR1BWRm5aVk9IS25FVkRRHyhUT11cHzdXR0YIWSZLWUoIRiZBQBlOVzpfTRpRVzBGGVNASy5LGkxAQTceUlFcXzoeTVBWRm5YXE9IS25HXERRHyhWQFVcHzdWSk0IWSZMVE4IRiZGTRU3EEldSxsHCgYGTg5YAAIMWQEHFihYW1VLWwtIBRAaBkgYFhVQAEgHOQZEHVlTAR0aEDECJRsfCiEqIygIRyFWR2k3EEldSxsZAAdJHFxRTlRIG0ZRSlEfKDkMXUkfQggbSX5GOQxdSR9CCB5JHlpASy5LFCgQQ0QfXQgXUApDWRALFVVfExYdExgFHV4FHQVTXF86XhpIRxMYDgEXCU5xAVVDRhsGFkQMDAhGJgEQWDcQSV1LGxkTThlxHlVJX09AAgxORXEeVUlfT10YWEJDcR5VSV9PXxkWThVYTlc6DAxxAVVDRhsCCxAZGloaAREEXlZUT1xKGkFVLwEdW1dPDwxESSQWF3ouJBsuTEY6MgUgeQ8sFSMOaBA%2FLBV5G1I3PTJDDAFEBWwfAQ8iNU8DFwM2Tl4pIzcuZBcWIEd3D0g8GA5GGRYsJX0nCQgvCkcaIAA9cR5VSV9PXgQGTgNGWg4jAktZMQ03AhVcABRfK1s5FBUZdCUWMUAgFTk3NiFmIAEcLjJqOydHEHoSM08GLWkoEENEH10TCR8PEEU5BkQdWVMKGwlYF1hCKFhbVUtbFEQZAE4CRA8AFkhLaxkVRyhYW1VLWxdeSTxKQkgNV0peHF9FLSI8fgEQLwIzTgAgIihYW1VLWwtcHFhCKFhbVUtbHkQGWAoRXjcQSV1LGxcJFhoQWFVNXUoUQTkGRB1ZUx0YCxBGVkFaHl1VJRhJHUZTHxlZVlROX0wZRlBBQRRaVUFfTBgoEENEH10IDVBIGkBSSkUYXFFPMQwdRFdFElsCFUReJVhEVUFCRg4ACQwVRAIATg1IGDkMXUkfQgMWDF1WUEheShxEV0NRHyhQSFlPG0JcRChYW1VLWxoQOTI2NnEeVUlfT14RAxBJHDcQSV1LGwAdA0kZXlZLWUoZKBBDRB9dC0QLEUU2Fl4xdDE2TFxBfCgQQ0QfXRYJDAtMGRZOEVUbDAsIXB83ABpRHygMCUhLbh0BVkZuCgwNDB5eUVcwB0IeFxoIXB83FxYFWAIXHB4KQVFXMAxdCEBLLhtYHUBBN14bBlxfOlsEFwVRHygWDx0MTlFXMBlEBgBcXzpDB0BBN18aDVxfOkodF1ZGbggJHANcHzcBBgYIWSYVAA1xAVVDRhsYDB5QOGcSNBcnXhw3OCQeZgE8EQZaHz0WATtqHSkWHHoSEDQnG2gGEx4wQDk2JiQgbAIwRj5aMVFMCjpkNw4ZNRVfH0APAVRDFAIWHAQiTRRNTx9IORIUJVcAXypCEwkRGB1ZFjUfL3EBVUNGGwcWCQwLTBkWThlIH0BLLhRFUVcwGUBOVzoAFwhGJh4HCFkmFBtcHzcIBR0IWSYJAVwfNxceBwhZJhADEFkXEh0QTxsWJRhJHUZTHwdEDFg4LgxFOTBDA38qLB4sLFsWVCRZRykHGjwzaxIcRUZpHyNMHiFoTCQDHxUSNgNUGEQxLiUsQF5dOiQ6dwMAQjhLGTcICjFeMDo0BGsNPAg9N0cWJwEbXF0wMlUxXzg8BhVKOFA3MQwdRFdFBEIfWDQDK1o4NxolFD4AN1sxbCY8BQNbWBI6XTpPIQAkDExZEj5USWoYMTokWQMTMwE%2FFUJXGxxCXQoYOTVIPgJLIHs4DCE9N1sHNRhEag46SyA9fAYCFj1gMTdJClR6ABYVAF8tLEsjTU8dMhcAFF8fOggrbEMmAyYUDhUaVBJUJCQwJB4JUzYYM14GCAUsHSRXNi82Rz8MJxxhJSZBGQ1KSVhRCQ%3D%3D"
                },
                {
                    "quality": 144,
                    "video_url": "https://rr1---sn-uxax4vopj5qx-q0n6.googlevideo.com/videoplayback?expire=1747937849&ei=2RUvaK7tEL_-i9oPt_PLwQc&ip=176.1.151.103&id=o-AAXb0pQe7BgHZB9W1lYpeOGX3K9pEqLsVI4UmvP0MfiK&itag=160&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399%2C597%2C598&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1747916249%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=1&pl=17&rms=au%2Cau&initcwndbps=1613750&bui=AecWEAbC5kNWvTTdIlNwEdZ_aTp7NPKnxd7qAtdvOLbwrpBc5LZZWIcsS3Zd-Euwkms_QPLlqBsjnEsI&spc=wk1kZo2tEhDv87em2RvMqfmYNsH-Y8MREUKKdeCKGOB4dWyV6kTD&vprv=1&svpuc=1&mime=video%2Fmp4&ns=Y96ef233er1HQHSjuVoJctEQ&rqh=1&gir=yes&clen=1350792&dur=232.360&lmt=1725425253642860&mt=1747915746&fvip=3&keepalive=yes&fexp=51331020%2C51466697&c=MWEB&sefc=1&txp=4532434&n=fhhBs-EYZS518Q&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIgOc1sx2n3WQw_9qlxwAmb9SttlK09u92jWKF6eDql9hoCIQC2YMM2yJ0P7vaH9S_9VW6VWP3wBDjvrIsEhmPvpRpHTg%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRAIgAUvb1W-jBbcQJFfy62DtF5sXE8Apk8ySz9aiEKVXm58CICZwe1LfrRqgHsD_GpFfYqPNjbBroq6UK8HrLYuagS5N&pot=MnRwLRiQ9UeN6HARYvwv3wC0CbUeWxa2wG90GlTIPthvJlF862hho6oaTLeJg8TVSiXPNvsPk0Ge_2MDQrgeIMZR0g-WtsftrFI2N4biWdt94zCeRA7CpR9epc9kyPACP3b6OuJsrmvX0O2OBOjKiThLNC8ttg==",
                    "video_ext": "mp4",
                    "video_size": 1350792,
                    "separate": 1,
                    "quality_note": "144p",
                    "alternate_url": "https://stream.aipark.top/download?payload=FltZHQgWB1kKCAlPQw9FUkdDFFlXTl9KHUZWUVgPHhcVT0MPHBEHBF5RSlYfCxxZSF4HQ0YQAQwBGQIKAx4YGh1UHElDQksUG0IMCRwbEEkRCl0XQgZKDwQdSBsVHxVUCQQaBkZIDBUaBkhWVE5ZThRHUktAFDcQSV1LGxEMTkZ%2FPhMYJk5ZMSksWURSCikZJn04EiIXcR5VSV9PRARYQkMbRVRXXEwcWlRDR3EeVUlfT0QQWBxZbCo9G10JfBFSMRNlMSdAOkhBLRUWO2ozVjJUCWgFKQAiZF8wFBspHTkDGj9xHlVJX09EAAQUSRxdVSUYSR1GUxIdWQoCClBIHkdAQTccWFFcXzocR1BWRm5aVk9IS25FVkRRHyhUT11cHzdXR0YIWSZLWUoIRiZBQBlOVzpfTRpRVzBGGVNASy5LGkxAQTceUlFcXzoeTVBWRm5YXE9IS25HXERRHyhWQFVcHzdWSk0IWSZMVE4IRiZGTRU3EEldSxsHCgYGTg5YAAIMWQEHFihYW1VLWwtIBRAaBkgYFhVQAEgHOQZEHVlTAR0aEDECJRsfCiEqIygIRyFWR2k3EEldSxsZAAdJHFxRTlRIG0ZRSlEfKDkMXUkfQggbSX5GOQxdSR9CCB5JHlpASy5LFCgQQ0QfXQgXUApDWRALFVVfExYdExgFHV4FHQVTXF86XhpIRxMYDgEXCU5xAVVDRhsGFkQMDAhGJgEQWDcQSV1LGxkTThlxHlVJX09AAgxORXEeVUlfT10YWEJDcR5VSV9PXxkWThVYTlc6DAxxAVVDRhsCCxAZGloaAREEXlZUT1xKGkFVLwEdW1dPDwxESSQWF3ouJBsuTEY6MgUgeQ8sFSMOaBA%2FLBV5G1I3PTJDDAFEBWwfAQ8iNU8DFwM2Tl4pIzcuZBcWIEd3D0g8GA5GGRYsJX0nCQgvCkcaIAA9cR5VSV9PXgQGTgNGWg4jAktZMQ03AhVcABRfK1s5FBUZdCUWMUAgFTk3NiFmIAEcLjJqOydHEHoSM08GLWkoEENEH10TCR8PEEU5BkQdWVMKGwlYF1hCKFhbVUtbFEQZAE4CRA8AFkhLaxkVRyhYW1VLWxdeSTxKQkgNV0peHF9FLSI8fgEQLwIzTgAgIihYW1VLWwtcHFhCKFhbVUtbHkQGWAoRXjcQSV1LGxcJFhoQWlZMXU4URjkGRB1ZUx0YCxBGVkFaHl1VJRhJHUZTHxlZVlROX0wZRlBBQR5dUUtVTx0oEENEH10IDVBIGkBSSkUYXFFPMQwdRFdFElsCFUReJVhEVUFCRg4ACQwVRAIATg1IGDkMXUkfQgMWDF1WUEheShxEV0NRHyhQSFlPG0JcRChYW1VLWxoQOTI2NnEeVUlfT14RAxBJHDcQSV1LGwAdA0kZXlZLWUoZKBBDRB9dC0QLEUU2Fl4xdDE2TFxBfCgQQ0QfXRYJDAtMGRZOEVUbDAsIXB83ABpRHygMCUhLbh0BVkZuCgwNDB5eUVcwB0IeFxoIXB83FxYFWAIXHB4KQVFXMAxdCEBLLhtYHUBBN14bBlxfOlsEFwVRHygWDx0MTlFXMBlEBgBcXzpDB0BBN18aDVxfOkodF1ZGbggJHANcHzcBBgYIWSYVAA1xAVVDRhsYDB5QOGcSNBcnXhw3KCQeYhdUAAwfBVYuPA5yTRQfDFoqCBtUKlkACThEFB5cSwcuZjJTFjBcB1wRAjpkJSZBLWAmVwAnSX1DExI8FDg6QDsuGyIyI0daKSETGwtkByAbGX0dFSsdMXkTQEAwCFghJRhJHUZTHwddChcYAAoQGQAHUR8oCBFIS24ZCFZGbgYLXF86QAdAQTdAHUBLLhRbHUBBN10HQEsuC0AHQEE3RAUMDQ4OQxAHAwdxHlVJX09BBwwUSWwoEBEgLB0DNzI9SiowDw9IelkPMRZOOi8%2FCwAbRiEHMhgYPTxVOF0fXQonV1IEECgyeywIRkxuIiYjGhwcOAMBJlwMLQopJmoEIxUtXDsrEw87XxsURSFmUy0LISBYFQIgQWM3EEldSxsECgdJYAU3DiErRCVcJhFjXS04PyBbAxNAA25bJhs4HHoMBEEDalJVPgEtZCQRGwJnByNBW0tFHApFG0w%2FKRwnHhUgMyAddTsrDx4pRkQiFisfJiEoHx5IPSgpJh0MSC4ZCksAFzU9HyVRGwQuSQBcRw5uDjc4WjpdJlwWBE5SDgA9OG4kVhFCYh4vCh8UWyxVPEZiKSoTJhB5HCk9NxUfER5QRA8J"
                }
            ]
        },
        {
            "media_type": "audio",
            "resource_url": "https://rr1---sn-uxax4vopj5qx-q0n6.googlevideo.com/videoplayback?expire=1747937849&ei=2RUvaK7tEL_-i9oPt_PLwQc&ip=176.1.151.103&id=o-AAXb0pQe7BgHZB9W1lYpeOGX3K9pEqLsVI4UmvP0MfiK&itag=140&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1747916249%2C&mh=S-&mm=31%2C29&mn=sn-uxax4vopj5qx-q0n6%2Csn-4g5ednd7&ms=au%2Crdu&mv=m&mvi=1&pl=17&rms=au%2Cau&initcwndbps=1613750&bui=AecWEAbC5kNWvTTdIlNwEdZ_aTp7NPKnxd7qAtdvOLbwrpBc5LZZWIcsS3Zd-Euwkms_QPLlqBsjnEsI&spc=wk1kZo2tEhDv87em2RvMqfmYNsH-Y8MREUKKdeCKGOB4dWyV6kTD&vprv=1&svpuc=1&mime=audio%2Fmp4&ns=Y96ef233er1HQHSjuVoJctEQ&rqh=1&gir=yes&clen=3762111&dur=232.408&lmt=1725424428667227&mt=1747915746&fvip=3&keepalive=yes&fexp=51331020%2C51466697&c=MWEB&sefc=1&txp=4532434&n=fhhBs-EYZS518Q&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cbui%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cns%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIgG-TdXrebYulIeZNHdQMwvJfb1bIdWwlmf6OtpSPQXgICIQCWvoGOO3TGbbP4ScGkcZkPFExw1GQXmQUb4YxM0Hlo6g%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACuhMU0wRAIgAUvb1W-jBbcQJFfy62DtF5sXE8Apk8ySz9aiEKVXm58CICZwe1LfrRqgHsD_GpFfYqPNjbBroq6UK8HrLYuagS5N&pot=MnRwLRiQ9UeN6HARYvwv3wC0CbUeWxa2wG90GlTIPthvJlF862hho6oaTLeJg8TVSiXPNvsPk0Ge_2MDQrgeIMZR0g-WtsftrFI2N4biWdt94zCeRA7CpR9epc9kyPACP3b6OuJsrmvX0O2OBOjKiThLNC8ttg=="
        }
    ]
}
{
    "text": "\u5218\u5fb7\u534e\u5168\u65b0\u732e\u5531\uff01\u4eba\u6c11\u65e5\u62a5\u676d\u5dde\u4e9a\u8fd0\u4f1a\u52a9\u5a01\u66f2\u300a\u767b\u573a\u300b",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://cn-jxjj-ct-01-08.bilivideo.com/upgcxcode/29/51/1272295129/1272295129-1-16.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&nbs=1&deadline=1747929923&gen=playurlv2&os=bcache&oi=1782024106&trid=0000dfb9d744f4054964b2295fe387de419ah&mid=0&platform=html5&og=cos&upsig=58b5b91448ce00ead9326da7d7acaceb&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform,og&cdnid=6470&bvc=vod&nettype=0&f=h_0_0&bw=49152&logo=80000000",
            "preview_url": "http://i2.hdslb.com/bfs/archive/735eb6e0c7b3d80f77f6efb184821305b94e906d.jpg"
        }
    ]
}
{
    "text": "Florence, 1501. Michelangelo and Leonardo go head-to-head | Renaissance: The Blood and the Beauty | BBC | Florence, 1501. Going head-to-head, Michelangelo and Leonardo \u2013 two very different men - will use all their creativity to push each other to... | By BBC Arts",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://video-mxp1-1.xx.fbcdn.net/o1/v/t2/f2/m69/AQN-VjAnjkRMYUaL96yIszsvMjg38_e_qhQt7k4P6JQY4hlmaUkHwf2IEWHK2rMPSef1H8xJ0ObNYwK6uRrTDJwE.mp4?strext=1&_nc_cat=107&_nc_sid=5e9851&_nc_ht=video-mxp1-1.xx.fbcdn.net&_nc_ohc=O-zIxCDaVUEQ7kNvwHCl3mG&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5GQUNFQk9PSy4uQzMuNzE4LmRhc2hfaDI2NC1iYXNpYy1nZW4yXzcyMHAiLCJ4cHZfYXNzZXRfaWQiOjU2Mzg0MDQxMzAyOTA2NiwidmlfdXNlY2FzZV9pZCI6MTAxMjIsImR1cmF0aW9uX3MiOjE0MCwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=776d9017f345ad51&_nc_vs=HBksFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTHFMdmh3eE1tMnJtUk1FQUNTQjZ1NU80ZkVyYm1kakFBQUYVAALIAQAVAhg6cGFzc3Rocm91Z2hfZXZlcnN0b3JlL0dPZENCQndBczFDd2lva0VBTlFPX2RrM1hLc2didjRHQUFBRhUCAsgBACgAGAAbAogHdXNlX29pbAExEnByb2dyZXNzaXZlX3JlY2lwZQExFQAAJpTLurjqs4ACFQIoAkMzLBdAYYAAAAAAABgZZGFzaF9oMjY0LWJhc2ljLWdlbjJfNzIwcBEAdQJllJ4BAA&_nc_zt=28&oh=00_AfJpBshCdLyzVE0Ba1q1StlskcAbvs9WL4Zhtqx73WHTqA&oe=6835022F&dl=1",
            "preview_url": "https://scontent-mxp2-1.xx.fbcdn.net/v/t15.5256-10/470038362_1086079176330287_5496252946760869303_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=596eb7&_nc_ohc=idODgm70PooQ7kNvwHT6_Rq&_nc_oc=AdnJDTgNJcFDoUGz-f6YXWvBg1NPjWt9FxlVqCFTa5y2j_kToc_kDAqY8TFhF8GotnU&_nc_zt=23&_nc_ht=scontent-mxp2-1.xx&_nc_gid=Imf0mho7g7ftUdl2q_dCvg&oh=00_AfK3ZJSrb8Q2MmZ54bmStvf3ZluSUhtk1k1ReqHw5HyazA&oe=6834FD11"
        }
    ],
    "stats": null,
    "overseas": 1
}
{
    "text": "hydrodynamica's Post",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://instagram.fiev22-2.fna.fbcdn.net/o1/v/t16/f2/m82/AQN5Zfeqq2fZi-FBOJNEGyu-dzWvA9-htQ4ZVuFu2wyqK5p9ZJSMbhQ-rgL4AYTmkDi-239JqNW45FftSH_axnlkuIuu69SflxE1Ud0.mp4?stp=dst-mp4&efg=eyJxZV9ncm91cHMiOiJbXCJpZ193ZWJfZGVsaXZlcnlfdnRzX290ZlwiXSIsInZlbmNvZGVfdGFnIjoidnRzX3ZvZF91cmxnZW4uY2xpcHMuYzIuMTA4MC5iYXNlbGluZSJ9&_nc_cat=102&vs=379762534515364_3935514953&_nc_vs=HBkcFQIYT2lnX3hwdl9yZWVsc19wZXJtYW5lbnRfcHJvZC80QTRFOTk1Q0ZFMTkzOTM5OTk0RkRDQUM2Nzk2NDhCMl92aWRlb19kYXNoaW5pdC5tcDQVAALIAQAoABgAGwAVAAAm3tLyu7vM9T8VAigCQzMsF0BLjEm6XjU%2FGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHX%2BB2XmnQEA&_nc_rid=215140ca5a&ccb=9-4&oh=00_AfJ9sjjv_QlU8Zd1y5XOg18Mavvb_6AvvnvOyC4EwzqP1Q&oe=6830F642&_nc_sid=d885a2",
            "preview_url": "https://instagram.fiev22-2.fna.fbcdn.net/v/t51.29350-15/403862609_1298355787543783_3760515111653518302_n.jpg?stp=dst-jpg_e15_tt6&_nc_ht=instagram.fiev22-2.fna.fbcdn.net&_nc_cat=107&_nc_oc=Q6cZ2QHX5VuP9fg5Ys8ABUtEpscFlT528bKhOcyq-pzX9X83BY2IQUrgDtpY4tbU-Hq0lAQ&_nc_ohc=d1lYlfwTNI8Q7kNvwEns1xX&_nc_gid=6pKaBQw9enJ3tDLI8dmMeg&edm=ANTKIIoBAAAA&ccb=7-5&oh=00_AfJvHzrTCOlvnNxYBZleHZxlSAbo99gb7TNvUfBvcdPjwQ&oe=68350E91&_nc_sid=d885a2"
        }
    ],
    "stats": null,
    "overseas": 1
}
{
    "text": "Angry car ",
    "medias": [
        {
            "media_type": "video",
            "resource_url": "https://video.twimg.com/ext_tw_video/1924691978786373636/pu/vid/avc1/720x1278/pHT_GN4OO64wZYP6.mp4?tag=12",
            "preview_url": "https://pbs.twimg.com/ext_tw_video_thumb/1924691978786373636/pu/img/-P0J21FzJQl1C4qK.jpg"
        }
    ],
    "stats": null,
    "overseas": 1
}
```

## Last updated

2025/5/23

<br/>

**1kuzus**
