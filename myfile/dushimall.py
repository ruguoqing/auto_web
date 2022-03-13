# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/8 10:38 下午

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.chrome.service import Service

# 新版本的实例化驱动
s = Service("../driverfiles/chromedriver")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.get('http://121.41.14.39:6001/index.htm')
driver.find_element(By.XPATH,"//a[text()='iphone 11']").click()

time.sleep(2)
window_handles = driver.window_handles
print(window_handles)
driver.switch_to.window(window_handles[-1])

# driver.find_element(By.XPATH,"//a[text()='                                                                                           【限时享24期免息】Apple/苹果 iPhone 11 移动联通电信全网通4G 超广角拍照手机\"']").click()
driver.find_element(By.XPATH,"//a[contains(text(),'限时享24期免息】Apple/苹果 iPhone 11 移动联通电信全网通4G 超广角拍照手机\"')]").click()

driver.quit()