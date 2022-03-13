# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/8 8:02 下午
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.chrome.service import Service

# 新版本的实例化驱动
s = Service("../driverfiles/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get('https://www.baidu.com')

# 隐式等待
driver.implicitly_wait(20)

driver.find_element(By.ID,'kw').send_keys('python')
driver.find_element(By.XPATH,"//input[@id='su']").click()

# 显示等待，WebDriverWait与expected_conditions结合使用，自定义等待条件
WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//a[text()='(计算机编程语言) - 百度百科']")))
driver.find_element(By.XPATH,"//div[@class='s_tab_inner']/a[text()='贴吧']").click()

#  强制等待，结合显示等待使用
# time.sleep(2)
WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.ID,'j_head_focus_btn')))

driver.find_element(By.ID,'j_head_focus_btn').click()
print('运行结束了')
time.sleep(2)
driver.quit()