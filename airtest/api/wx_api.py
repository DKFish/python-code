#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2020-03-13 11:01
"""
import requests
import time
import json

base = "http://bestriverwxapp-beta.renmaitech.com"


def sent_moblie(mobile):
    """发送短信验证名
    :param mobile:手机号码
    :return:
    """
    sent_url = base + "/app/mobileCode/send"
    data = {"mobile": mobile, "mobileCodeType": "LOGIN"}
    bd = json.dumps(data)
    header = {"Content-Type": "application/json"}
    re = requests.post(url=sent_url, headers=header, data=bd)
    print(re.text)


def login(mobile):
    """
    登录
    :param mobile: 登录手机号码
    :return:
    """
    url = base + "/app/auth/mobile/login"
    data = {"mobile": mobile, "code": "000000", "loginType": "WX"}
    bd = json.dumps(data)
    header = {"Content-Type": "application/json"}
    re = requests.post(url=url, headers=header, data=bd)
    print(re.text)


def sign():
    pass


if __name__ == '__main__':
    # mobile = 18500977100
    # mobile = 18320000001
    # mobile = 18320000004
    mobile = 18500000001
    sent_moblie(mobile)
    login(mobile)
