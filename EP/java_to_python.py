#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import time

# 时间与验证码
time_now = str(time.time())
tokenKey = vars.get("token_key")
# 自定义的参数
AdRequestInfo = vars.get("AdRequestInfo")
AdExtendInfo = vars.get("AdExtendInfo")
# 参数排序
param = "AdExtendInfo="+AdExtendInfo+"AdRequestInfo="+AdRequestInfo + "Time="+time_now + tokenKey
# 生成签名
# MessageDigest md = MessageDigest.getInstance("MD5");
md = hashlib.md5()
md.update(param.encode(encoding="UTF-8"))
b = bytes(md.digest())
#
hexValue = []
for i in range(len(b)):
    val = int(b[i]) & 0xff  # python中该写法似乎不必要
    # val = int(b[i])
    if val < 16:
        hexValue.append("0")
    hexValue.append(hex(val))
sign = ''.join(hexValue)

vars["Time"] = time_now
vars["Sign"] = sign
vars["AdExtendInfo"] = AdExtendInfo
vars["AdRequestInfo"] = AdRequestInfo