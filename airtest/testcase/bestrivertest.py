#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-07-02 16:42
"""
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from pages.bestlogin import Login
from utils.devices import *
from pages.homepage import HomePage
from testcase.common.install_case import *

if __name__ == '__main__':
    devices = get_devices()
    apk = apk_devices()
    auto_connect(devices=devices)
    package = get_package('bestriver')
    # install_chanels()
    mobile = '18500976300'
    code = '000000'
    # script content
    print("start...")
    start_app(package)
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
    poco(text="我的").click()
    if poco("com.finupcredit.bestriver:id/fra_mine_phonenum").get_text() == "未登录":
        poco("com.finupcredit.bestriver:id/fra_mine_phonenum").click()

    login = Login(poco, mobile=mobile, code=code)
    home_page = HomePage(poco)
    login.mobile = '18500976200'
    login.login()
    poco(text="首页").click()
    ui = home_page.hot_products
    print(type(ui))
    ui[0].click()
    time.sleep(6)
    stop_app(package)
