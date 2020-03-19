#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-10-14 15:42
"""


class My_Page():
    def __init__(self, popoui):
        self._android_ui = popoui

    def get_phonenum(self):
        self._android_ui('com.finupcredit.bestriver:id/fra_mine_phonenum').text

    def into_login(self):
        self._android_ui('com.finupcredit.bestriver:id/fra_mine_phonenum ').click()
