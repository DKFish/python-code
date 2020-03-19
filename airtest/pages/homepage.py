#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-07-11 19:21
"""


class HomePage:
    def __init__(self, popcui):
        self._ui = popcui

    @property
    def app_name(self):
        """
        获取当前App名
        :return:app名
        """
        return self._ui('com.finupcredit.bestriver:id/appName').get_text()

    @property
    def hot_products(self):
        """

        :return:
        """
        return self._ui('com.finupcredit.bestriver:id/ll_hot_product_list').child('android.view.ViewGroup')
