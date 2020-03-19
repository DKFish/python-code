#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-07-18 19:53
"""
from concurrent.futures.thread import ThreadPoolExecutor

from utils.devices import *


def install_chanels(devices=None):
    """
    安装渠道包
    :param devices:
    :return:
    """
    if not devices:
        devices = get_devices()
    else:
        devices = devices
    apk = apk_devices()
    auto_connect(devices=devices)
    package = get_package('bestriver')
    # script content
    for k in apk:
        set_current(apk[k])
        if check_app(apk[k], package):
            uninstall(package)
        install_app(apk=k, device=apk[k])


def install_nochanels(devices=None, package=None, test=False):
    """
    安装指定包
    :param devices:
    :return:
    """

    base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    if not devices:
        devices = get_devices()
    else:
        devices = devices

    if not package:
        package_name = 'bestriver'
    else:
        package_name = package
    args = [(d, test) for d in devices]
    auto_connect(devices=devices)
    with ThreadPoolExecutor(len(devices)) as executor:
        executor.map(install, args)


def install(args):
    dev = args[0]
    test = args[1]

    package = get_package('bestriver')
    if check_app(dev.split('/')[-1], package):
        set_current(dev.split('/')[-1])
        uninstall(package)
    if test:
        path = "/Users/finup/Desktop/work/dev/bestriveruitest/resource/no-chanels/test"
        install_app(apk='BestRiver_debug_V1.3.6-1361-2019-10-24-14-58-05.apk', chanel=False, device=dev.split('/')[-1],
                    path=path)
    else:
        install_app(apk='BestRiver_release_V1.3.6-1361-2019-10-24-17-44-26.apk', chanel=False, device=dev.split('/')[-1])


if __name__ == '__main__':
    # install_nochanels()
    install_nochanels(test=True)
    # install_chanels()
