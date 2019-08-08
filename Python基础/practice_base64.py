# /usr/bin/env python
# -*- coding: utf-8 -*-
# author = 'Han Kai'
import base64
#base64加密
print(base64.b64encode('hsk'.encode('utf-8')))
#base64解密
print(base64.b64decode('aHNr'.encode('utf-8')))
