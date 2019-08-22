# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import json,requests
from fake_useragent import UserAgent

def return_text():
    url = "http://t.weather.sojson.com/api/weather/city/101011100"
    headers = {
        'User-Agent':UserAgent().random,
        'Content-Type':'application/json;charset=UTF-8'
    }
    response = requests.get(url=url,headers=headers)
    dict_text = eval(response.text)
    tomorrow = dict_text['data']['forecast'][1]
    list1 = []
    for k,w in tomorrow.items():
        list1.append(w)
    text = '明天:\n\n%s，%s，%s，%s，风速：%s，风向：%s，天气：%s\n\n寄语：%s'%(list1[3],list1[4],list1[1],list1[2],list1[9],list1[8],list1[10],list1[11])
    return text

# print(return_text())

"""
官方发送内容文档 https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq
"""
def send_date():
    #text文本
    text_request_date = {
        "msgtype": "text",
        "text": {
            "content": "测试一下，马上出发"
        },
        "at": {
            "atMobiles": [],
            "isAtAll": True
        }
    }
    #markdown类型
    markdown_request_date = {
         "msgtype": "markdown",
         "markdown": {
             "title":"北京天气",
             "text": "#### 天气预报\n" +
                     "> "+return_text()+"\n" +
                     "> ![screenshot](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1566454152645\
                     &di=d3aab9058675ae157cf2dde97b6b8665&imgtype=0&src=http%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2016%2F08%2F16%2F23%2F14%2Frock-outcrop-1599212_960_720.jpg)\n"
         },
        "at": {
            "atMobiles": [],
            "isAtAll": True
        }
     }

    request_date = json.dumps(markdown_request_date)
    return request_date
#字符串中unicode转中文
print(send_date().encode('utf-8').decode('unicode_escape'))


def send_weather():
    url = "https://oapi.dingtalk.com/robot/send?access_token=73f3bd48a98ff1xxxxxxxxxxxxxxxxxxx19447707f77"
    headers = {
        'Content-Type':'application/json',
        'Chartset':'utf-8'}
    response = requests.post(url=url,headers=headers,data=send_date())
    content = response.content.decode()
    print(content)

send_weather()

