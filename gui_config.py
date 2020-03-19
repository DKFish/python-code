#!/usr/bin/python
"""
 # @author kangyanwen
 # @Description
 # @create 2020-02-24 11:30
"""
import json
import copy
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

name = '*******@1***.com'
password = '*******'
home_url = 'https://portal.shadowsocks.nl/index.php'
configs = []

# 设置启动模式
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(executable_path='/Users/finup/Desktop/work/dev/ybj/driver/chromedriver',
#                           chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path='ybj/driver/chromedriver')

driver.get(url=home_url)

driver.find_element(by=By.XPATH, value='//*[@id="primary-nav"]/div/a[2]').click()  # 进入登录界面
# 登录
driver.find_element(by=By.ID, value='inputEmail').send_keys(name)
driver.find_element(by=By.XPATH, value='//*[@id="inputPassword"]').send_keys(password)
driver.find_element(by=By.XPATH, value='//*[@id="login"]').click()

# 服务详情页
productdetails = 'https://portal.shadowsocks.nl/clientarea.php?action=productdetails&id=1167332'
driver.get(productdetails)

# 获取
size = len(driver.find_elements(By.XPATH, value='//*[@id="listqr"]/tbody/tr'))
xpaths = ['//*[@id="listqr"]/tbody/tr[{index}]/td[2]/code'.format(index=n) for n in range(1, size)]

# 构造配置文件
for xpath in xpaths:
    config = {"password": "GqPMt8rEh5BeGwZK4M",
              "server_port": 443,
              "tcp_fast_open": False,
              "verify": True}
    remarks = driver.find_element(By.XPATH, xpath).text
    config['remarks'] = remarks
    config['server'] = remarks
    configs.append(config)

gui_config = {'configs': configs, 'localPort': 8080, 'shareOverLan': False}
gui_json = json.dumps(gui_config)

with open(os.path.dirname(__file__), "w") as f:
    json.dump(gui_config, f)

driver.quit()
