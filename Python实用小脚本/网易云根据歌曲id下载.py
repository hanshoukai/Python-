# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import requests,re
import urllib.request

def getResponse(url, headers):
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return response
        return None
    except Exception as e:
        return None

def getSongname(songid):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }
        url = 'https://music.163.com/song?id={}'.format(songid)
        html = getResponse(url, headers=headers).text
        # print(html)
        title = re.findall('<title>(.*?)</title>', html, re.S)
        print('----------------')
        print(title)
        name = title[0].split('-')[0]
        return name.strip()
    except:
        print("获取歌名失败")

if __name__ == '__main__':
    songid = input("请输入要下载的歌曲id：")
    url = 'http://music.163.com/song/media/outer/url?id={}'.format(int(songid))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    download_url = getResponse(url, headers).url
    Songname = getSongname(int(songid))
    print("下载的地址：",download_url)
    print("下载的歌曲：", Songname)
    #和with open类似，这个方法可以根据地址另存为
    urllib.request.urlretrieve(download_url, Songname + '.mp3')

