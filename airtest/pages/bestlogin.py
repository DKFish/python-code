#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-07-10 17:11
"""


class Login:
    def __init__(self, popcui, mobile, code):
        self._android_ui = popcui
        self._mobile = mobile
        self._code = code
        pass

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        self._mobile = mobile

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    def set_mobile(self, mobile):
        self._android_ui('com.finupcredit.bestriver:id/mobile_et').set_text(mobile)

    def set_code(self, code):
        self._android_ui('com.finupcredit.bestriver:id/code_et').set_text(code)

    def get_mobile_code(self):
        self._android_ui('com.finupcredit.bestriver:id/get_mobile_code_tv').click()

    def auth_protocol(self):
        self._android_ui('com.finupcredit.bestriver:id/auth_protocol').click()

    # 默认登陆流程
    def login(self):
        self.set_mobile(self._mobile)
        self.get_mobile_code()
        self.set_code(self._code)
        self.auth_protocol()
        self._android_ui('com.finupcredit.bestriver:id/login_bt').click()
