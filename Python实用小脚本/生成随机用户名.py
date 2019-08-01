#生成随机用户名
import random,string

#生成大小字母和数字一起的大字符串
all_str=string.ascii_letters+string.digits

res_lit=[]
for i in range(10):
    #从大字符串中随机生成8位数的字符，换行并转换成字符串
    res = ''.join(random.sample(all_str,8))+'\n'
    if res not in res_lit:
        res_lit.append(res)
    with open('useranme.txt','w')as fp:
        fp.writelines(res_lit)
