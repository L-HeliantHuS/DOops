from django.db import models


# Create your models here.

# 保存远程主机
class Hosts(models.Model):
    id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=100, unique=True, verbose_name="主机地址")  # 主机地址
    port = models.IntegerField(default=22, verbose_name="端口")  # 端口
    remark = models.CharField(max_length=255, verbose_name="描述", unique=True)  # 描述
    username = models.CharField(max_length=255, verbose_name="用户名")  # 用户名
    password = models.CharField(max_length=255, verbose_name="密码")  # 密码
    group = models.IntegerField(verbose_name="组")  # 组


# 保存所有组 用于添加组和删除组
class Group(models.Model):
    id = models.AutoField(primary_key=True)
    gorup_name = models.CharField(max_length=255, unique=True, verbose_name="组名")


# 用户 以及 组权限映射
class AuthTab(models.Model):
    user_id = models.IntegerField(verbose_name="用户ID")
    group_id = models.IntegerField(verbose_name="组ID")
