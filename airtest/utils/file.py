#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-07-03 18:09
"""
import os
import yaml
from xlrd import open_workbook


# 读取配置文件，使用yaml文件
class YamlReader(object):
    def __init__(self, yamlfile_path):
        if os.path.exists(yamlfile_path):
            self.file_path = yamlfile_path
        else:
            raise FileNotFoundError("文件不存在！")
        self._data = None

    @property
    def data(self):
        if not self._data:
            with open(self.file_path, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


# 读取excle
class ExcelReader(object):
    def __init__(self, path, sheet=0, title=True):
        if os.path.exists(path):
            self.excel_path = path
        else:
            raise Exception("文件不存在")
        self.sheet = sheet
        self.title_line = title
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel_path)
            if type(self.sheet) not in [int, str]:
                raise Exception('sheet：{0} 索引不支持'.format(type(self.sheet)))
            elif type(self.sheet) == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                # 首行为标题时，将标题添加到
                title = s.row_values(0)
                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))
            else:
                for col in range(0, s.nrows):
                    self._data.append(s.row_values(col))
        return self._data