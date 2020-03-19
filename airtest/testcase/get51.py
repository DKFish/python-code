#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2019-08-27 20:25
"""

# -*- coding:utf-8 -*-
import re  # 用来做正则匹配用
import requests  # 用来做网络请求用
import xlwt  # 用来创建excel文档并写入数据

# 要查询的职位
key = 'python'


# 获取原码
def get_content(page):
    headers = {'Host': 'search.51job.com',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    url = 'http://search.51job.com/list/000000,000000,0000,00,9,99,' + key + ',2,' + str(
        page) + '.html'
    r = requests.get(url, headers, timeout=10)
    s = requests.session()
    s.keep_alive = False
    r.encoding = 'gbk'
    html = r.text
    return html


# 匹配规则
def get(html):
    reg = re.compile(
        r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',
        re.S)  # 匹配换行符
    items = re.findall(reg, html)
    return items


def excel_write(items, index):
    # 爬取到的内容写入excel表格
    for item in items:  # 职位信息
        for i in range(0, 5):
            # print item[i]
            ws.write(index, i, item[i])  # 行，列，数据
        print(index)
        index += 1


newTable = "test.xls"  # 表格名称
wb = xlwt.Workbook(encoding='utf-8')  # 创建excel文件，声明编码
ws = wb.add_sheet('sheet1')  # 创建表格
headData = ['职位', '公司', '地址', '薪资', '日期']  # 表头部信息
for colnum in range(0, 5):
    ws.write(0, colnum, headData[colnum], xlwt.easyxf('font: bold on'))  # 行，列
# 查询1-10页的数据，这里的10可以改成你想查询多少页
for each in range(1, 2):
    index = (each - 1) * 50 + 1
    excel_write(get(get_content(each)), index)
