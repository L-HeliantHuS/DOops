#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ Author: HeliantHuS
@ Codes are far away from bugs with the animal protecting
@ Time:  2019/12/23
@ FileName: serializer.py
"""
import time

# 定义变量

# 用户操作不正确
UserInputError = 40001

# 用户操作不合法
UserInputPanic = 40002

# 用户没权限
UserPremissionNotFound = 40003

# 服务器异常
ServerError = 50001


# Response 基础序列化器
def Response(code=0, data="", msg="", error=""):
    return {
        "code": code,
        "data": data,
        "msg": msg,
        "error": error,
        "timestamp": int(time.time())
    }
