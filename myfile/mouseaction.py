# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/9 12:35 上午

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# 新版本的实例化驱动
s = Service("../driverfiles/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get('https://www.baidu.com')

# 鼠标操作，先找到元素，鼠标悬浮

WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//span[text()='设置']")))
ele = driver.find_element(By.XPATH,"//span[text()='设置']")
# # 实例化一个鼠标操作
# ac = ActionChains(driver)
# # 移动鼠标到目标元素
# ac.move_to_element(ele)
# # 执行操作
# ac.perform()
# 连写
ActionChains(driver).move_to_element(ele).click().perform()

WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//a[text()='高级搜索']")))
driver.find_element(By.XPATH,"//a[text()='高级搜索']").click()

# WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//span[text()='所有网页和文件']")))
# ele2 = driver.find_element(By.XPATH,"//span[text()='所有网页和文件']")
# # select下拉选择元素
# Select(ele2).select_by_value('all')
# Select(ele2).select_by_index(2)
# Select(ele2).select_by_visible_text('RTF 文件 （.rtf)')


# 键盘操作 Keys
ele.send_keys(Keys.ENTER)