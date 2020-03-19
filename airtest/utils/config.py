#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-07-03 18:08
"""

import os
from .file import YamlReader

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH = os.path.join(BASE_PATH, 'config', 'config.yml')
LOG_PATH = os.path.join(BASE_PATH, 'logs')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
RESOURCE_PATH = os.path.join(BASE_PATH, 'resource')


class Config(object):
    def __init__(self, config=CONFIG_PATH):
        print('配置文件：', config)
        self.config = YamlReader(config).data

    def get(self, element, index=0):
        return self.config[index].get(element)
