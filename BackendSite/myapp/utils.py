#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@ Author: HeliantHuS
@ Codes are far away from bugs with the animal protecting
@ Time:  2019/12/24
@ FileName: utils.py
"""
import paramiko
from django.conf import settings
from .serializer import *
from django.http import JsonResponse


# SSH ssh客户端
def SSH(hostname, port, username, password, command) -> bool:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # 密码验证失败尝试用公钥
        try:
            ssh.connect(hostname=hostname, port=port, username=username, password=password, timeout=5)
        except:
            ssh.connect(hostname=hostname, port=port, username=username, pkey=settings.PKEY_PATH, timeout=5)
        a, b, c = ssh.exec_command(command)
        return b.readlines()
    except:
        return False
    finally:
        ssh.close()


def isSuperUser(func):
    def check_super_user(request):
        res = Response()
        if request.user.is_superuser:
            return func(request)
        else:
            return JsonResponse(res)

    return check_super_user
