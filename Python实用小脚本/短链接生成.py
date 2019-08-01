# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import requests
url = input("请输入要压缩的链接：")
short = "http://api.weibo.com/2/short_url/shorten.json?source=2849184197&url_long="
result = requests.get(short + url).json()
print("短链接为：", result["urls"][0]["url_short"] + "\n")