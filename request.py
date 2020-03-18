#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2020-02-18 16:33
"""
import requests
import csv
import datetime
from concurrent.futures.thread import ThreadPoolExecutor
from lxml import html
import os


def get_pagenum():
    """
    获取总页数
    :return:
    """
    url = 'http://fw.ybj.beijing.gov.cn/ddyy/ddyy2/list'
    re = requests.get(url=url)
    re.encoding = re.apparent_encoding
    etree = html.etree
    dom = etree.HTML(re.text)
    total = int((dom.xpath('/html/body/div/div[2]/div[3]/p/b[1]/text()')[0]).split('/')[1])
    return total


def get_num(page):
    """
    获取指定页的医院编号
    :return:
    """

    url = 'http://fw.ybj.beijing.gov.cn/ddyy/ddyy2/list'
    if page:
        data = {'page': page}
        re = requests.post(url=url, data=data)
        re.encoding = re.apparent_encoding
        etree = html.etree
        dom = etree.HTML(re.text)
        num = dom.xpath('//tbody/tr/td[1]/text()')
    else:
        num = 0
    return num


def get_detail(num):
    """
    根据编号(num),获取定点医院的具体信息
    :param num: 医院编号
    :return: data(元祖)包括：医院名称(name),所在区县(county),详细地址(address)
    """
    url = 'http://fw.ybj.beijing.gov.cn/ddyy/ddyy2/findByName?id=' + num
    re = requests.get(url)
    re.encoding = re.apparent_encoding
    etree = html.etree
    dom = etree.HTML(re.text)
    name = dom.xpath('//table/tr[1]/td/text()')
    county = dom.xpath('//table/tr[3]/td/text()')
    address = dom.xpath('//table/tr[4]/td/text()')
    data = (num, name[0], county[0], address[0])
    return data


def main(page):
    """
    返回指定页(page)的药店的具体信息
    :param page:
    :return: 药店信息
    """
    re = []
    page_num = get_num(page)
    for n in page_num:
        detail = get_detail(n)
        re.append(detail)
    return re


if __name__ == '__main__':

    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data', 'data.csv')
    start = datetime.datetime.now()
    details = []
    header = ('编码', '药店名', '所在区县', '地址')
    total_page = get_pagenum()

    # 启动多线程，每个线程处理一页数据
    with ThreadPoolExecutor(max_workers=20) as executor:
        temp = [executor.submit(main, page) for page in range(1, total_page + 1)]

    # 处理返回数据
    for de in temp:
        details.extend(de.result())

    with open(file, 'w') as f:
        write = csv.writer(f)
        write.writerow(header)
        write.writerows(details)

    end = datetime.datetime.now()
    print("总耗时:{0}".format((end - start).seconds))
