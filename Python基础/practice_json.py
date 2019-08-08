# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import json
import demjson

data = {
    "name":"hankai",
    "age":29,
}

#把字典转为json
json_str = json.dumps(data)
#把字典转为json存入文件中
with open('data.json','w')as f:
    json.dump(data,f)

#把json转为字典
json_dict = json.loads(json_str)
#把json转为字典读取出来
with open('data.json','r')as f:
    text = json.load(f)
    print(text['age'])

#-------------------------------------

#字典转为json
demjson_json_data = demjson.encode(data)
print(demjson_json_data)
print(type(demjson_json_data))

#json转为字典
demjson_dict_data = demjson.decode(demjson_json_data)
print(demjson_dict_data)
print(type(demjson_dict_data))

