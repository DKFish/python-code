#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-07-03 18:04
"""
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.error import AirtestError

from utils.config import Config
from airtest.core.android.adb import ADB

CONF = Config().get('devices')


def get_devices():
    """
    :return: 返回设备列表
    """

    base = CONF.get('base')
    child = CONF.get('child')
    return [(base + v) for v in child.values()]


def apk_devices():
    """
    获取对应设备的APK
    :return:
    """
    return CONF.get('child')


def auto_connect(devices, logdir: object = None) -> object:
    """
    :param devices:
    :param logdir:
    :return:
    """
    if not cli_setup():
        auto_setup(__file__, logdir=logdir, devices=devices)


def install_app(apk, device, chanel=True, path=None):
    """
    :param apk:渠道名/安装包名
    :param device:设备uuid or index of initialized device instance
    :param chanel:是否开启渠道，默默开启
    :param path: 自定义apk
    :return:
    """
    version = CONF.get('version')
    base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    apkname = 'BestRiver_aligned_signed_' + apk + '.apk'
    if chanel:
        file_path = os.path.join(base_path, 'resource', 'chanels', version, apkname)
    else:
        file_path = os.path.join(base_path, 'resource', 'no-chanels', apk)
    if path:
        file_path = os.path.join(path, apk)

    try:
        set_current(device)
        install(file_path, replace=True)
    except IndexError:
        raise Exception('file:{0} ,在设备{1}上安装失败'.format(file_path, device))


def get_package(name):
    """
    获取app包名
    :param name: 应用名称
    :return:
    """
    return CONF.get('packages').get(name)


def check_app(device, name):
    try:
        set_current(device)
        return ADB(device).check_app(name)
    except AirtestError:
        return False


if __name__ == '__main__':
    get_devices()
