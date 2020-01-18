from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from .serializer import *
from .utils import SSH, isSuperUser
from .models import Hosts, Group, AuthTab
from django.contrib.auth.models import User
from django.contrib import auth
import json


# Ping /api/ping
def Ping(request):
    res = Response()
    return JsonResponse(res)


# Error 未登录就跳转这个！  /api/user/error
def Error(request):
    res = Response()

    res['code'] = UserPremissionNotFound,
    res['msg'] = "You Not Login, Plz To Login~",

    return JsonResponse(res)


# TestHosts 测试所有主机是否存活
@login_required(login_url='/api/user/error')
def TestHosts(request):
    res = Response()
    if request.method == "GET":
        db = Hosts.objects.all()
        res['data'] = [{"hostid": i.id, "remark": i.remark, "hostname": i.hostname} for i in db]

    elif request.method == "OPTIONS":
        db = Hosts.objects.all()
        result = {}
        for i in db:
            ex = SSH(i.hostname, i.port, i.username, i.password, "echo Pong")
            if ex:
                result[i.hostname] = "online"
            else:
                result[i.hostname] = "die"
        res['data'] = result
    return JsonResponse(res)


# Host 主机执行命令 以及 添加主机 以及 删除主机 和 修改主机
@login_required(login_url='/api/user/error')
def Host(request):
    res = Response()
    # 根据ID获得主机信息
    if request.method == "GET":
        try:
            if request.user.is_superuser:
                db = Hosts.objects.all()
            else:
                userid = request.user.id
                # 当前用户拥有的组id
                auth_groupid = [i.group_id for i in AuthTab.objects.filter(user_id=userid)]
                db = Hosts.objects.filter(group__in=auth_groupid)

            result = [
                {"id": i.id,
                 "remark": i.remark,
                 "hostname": i.hostname,
                 "port": i.port,
                 "username": i.username,
                 }
                for i in db
            ]
            res['data'] = result
        except:
            res['msg'] = "Not Data!"

    # 添加主机
    elif request.method == "POST":
        body = json.loads(request.body)
        hostname = body.get("hostname", None)
        port = body.get("port", 22)
        remark = body.get("remark", None)
        username = body.get("username", "root")
        password = body.get("password", None)
        group = body.get("group", None)

        if (hostname is not None) and (remark is not None) and (password is not None) and (group is not None):
            try:
                # 验证组id是否合法
                groupid = [i.id for i in Group.objects.all()]
                if group in groupid:  # 如果提交的group_id是表内合法的group_id才会验证ssh连通性
                    ex = SSH(hostname=hostname, port=port, username=username, password=password, command="echo Pong")
                    if ex:
                        print(ex)
                        db = Hosts.objects.create(hostname=hostname, port=port, remark=remark, username=username, password=password, group=group)  # group
                        db.save()
                        res["msg"] = "Add Host is Success!"
                    else:
                        res["code"] = UserInputError
                        res['msg'] = "Host is Not Online!"
                else:
                    res['code'] = UserInputError
                    res['msg'] = "Group_id verification failed"
            except:
                res['code'] = UserInputError
                res['msg'] = "The Host is Exits."

        # 用户输入不正确！
        else:
            res['code'] = UserInputError
            res['msg'] = "Input Error!"


    # 修改主机信息
    elif request.method == "PUT":
        pass
    # 删除主机
    elif request.method == "DELETE":
        pass
    else:
        res['code'] = UserInputError
        res['msg'] = "Error Methods!"
    return JsonResponse(res)


# Exec 执行命令
@login_required(login_url="/api/user/error")
def Exec(request):
    res = Response()
    userid = request.user.id
    if request.method == "POST":
        body = json.loads(request.body)
        host_id = body.get("hostid", [])
        command = body.get("command", None)

        db = Hosts.objects.filter(id__in=host_id)
        # 当前用户拥有的组id
        auth_groupid = [i.group_id for i in AuthTab.objects.filter(user_id=userid)]

        # 提交要执行命令的主机Host组id
        hostids = [i.group for i in Hosts.objects.filter(id__in=host_id)]

        # 设置一个标志
        flag = True
        for hostid in hostids:
            if hostid not in auth_groupid:
                flag = False
                break

        if flag:
            result = {}
            for i in db:
                ex = SSH(hostname=i.hostname, port=i.port, username=i.username, password=i.password, command=command)
                if ex:
                    result[i.hostname] = ex
                else:
                    result[i.hostname] = "die"
            res['data'] = result
        else:
            res['code'] = UserPremissionNotFound
            res['msg'] = "Host Permission verification failed"

    return JsonResponse(res)


# 获得所有分组
@login_required(login_url='/api/user/error')
def CrudGroup(request):
    res = Response()
    if request.method == "GET":
        group = [{"id": i.id, "group_name": i.gorup_name} for i in Group.objects.all()]
        res['data'] = group
    elif request.method == "POST":
        body = json.loads(request.body)
        group_name = body.get("group", False)
        if group_name.strip() != "":
            # 创建这个组名 成功了就返回id 和 组名
            try:
                db = Group.objects.create(gorup_name=group_name)
                res["data"] = {"id": db.id, "group_name": db.gorup_name}
                res["msg"] = "Create Success"
            # 失败了就告诉用户创建失败
            except:
                res['code'] = UserInputPanic
                res["msg"] = "Create failed"
        else:
            res['code'] = UserInputError
            res['msg'] = "'group' is required!"
    else:
        res['code'] = UserInputError
        res['msg'] = "Methods Error!"
    return JsonResponse(res)


# Login 登录
def Login(request):
    res = Response()
    if request.method == "POST":
        body = json.loads(request.body)
        username = body.get("username", False)
        password = body.get("password", False)
        if username and password:
            login = auth.authenticate(request=request, username=username, password=password)
            if login is not None:
                auth.login(request=request, user=login)
                res['msg'] = "Login Success!"
            else:
                res['code'] = UserInputError
                res['msg'] = "Login Error! Username or Password input error!"
        else:
            res['code'] = UserInputPanic
            res['msg'] = "Illegal input"
    else:
        res['code'] = UserInputPanic
        res['msg'] = 'Method error!'
    return JsonResponse(res)


# Logout 注销
def Logout(request):
    res = Response()
    auth.logout(request)
    res['msg'] = "Logout Success!"
    return JsonResponse(res)


# isLogin 判断是否登录
@login_required(login_url='/api/user/error')
def isLogin(request):
    res = Response()
    res['msg'] = 'is login!'
    return JsonResponse(res)


# AuthConf 设置权限
@login_required(login_url="/api/user/error")
@isSuperUser  # 判断是否为超级管理员
def AuthConf(request):
    res = Response()
    if request.method == "GET":
        pass
    elif request.method == "POST":
        body = json.loads(request.body)
        userid = body.get("userid", None)
        groupid = body.get("groupid", None)
        # 判断输入是否不为空
        if (userid is not None) and (groupid is not None):
            temp = AuthTab.objects.filter(user_id=userid, group_id=groupid)
            if len(temp) > 0:
                res['code'] = UserInputError
                res['msg'] = "The Rule is Exits"
            else:
                try:
                    username = User.objects.get(id=userid).username
                    groupname = Group.objects.get(id=groupid).gorup_name
                    AuthTab.objects.create(user_id=userid, group_id=groupid)
                    result = {
                        "user": username,
                        "group": groupname
                    }
                    res['data'] = result
                except:
                    res['code'] = UserInputPanic
                    res['msg'] = "user or group not found."
        else:
            res['code'] = UserInputError
            res['msg'] = "Input Error!"

    return JsonResponse(res)


# Status 返回主机的概况
# "online_total": len([1 for i in db if SSH(i.hostname, i.port, i.username, i.password, "echo Pong")])
# @login_required(login_url='/api/user/error')
def Status(request):
    res = Response()
    if request.method == "GET":
        hosts_count = Hosts.objects.all().count()
        users_count = User.objects.all().count()
        result = {
            "hosts_count": hosts_count,
            "users_count": users_count,
        }
        res['data'] = result
    else:
        res['code'] = UserInputPanic
        res['msg'] = "Method Error!"

    return JsonResponse(res)
