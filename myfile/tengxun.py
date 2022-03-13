# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/8 9:19 下午

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.chrome.service import Service

# 新版本的实例化驱动
s = Service("../driverfiles/chromedriver")
driver = webdriver.Chrome(service=s)

driver.get('https://ke.qq.com/')
driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME,'mod-entry-login').click()
time.sleep(2)
# iframe 切换
driver.switch_to.frame(driver.find_element(By.XPATH, "//div[@class='login-qq-iframe-wrap']/iframe"))
# driver.switch_to.frame(2)

WebDriverWait(driver,10).until(ec.visibility_of_element_located((By.XPATH,"//a[text()='帐号密码登录']")))
driver.find_element(By.XPATH,"//a[text()='帐号密码登录']").click()


# # alert 切换
# alert = driver.switch_to.alert
# alert.accept()
# alert.dismiss()



driver.quit()