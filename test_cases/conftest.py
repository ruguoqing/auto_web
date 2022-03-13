# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/11 7:58 下午

import pytest

from commons.do_log import RunLog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from page_objects.login_page import LoginPage
from test_datas.login_data import LoginData

driver = None


@pytest.fixture(scope='class')
def access_web():
    global driver
    RunLog().info('----用例类前置：初始化浏览器会话，登录商城系统')
    driver = webdriver.Chrome(service=Service("/Users/meidi/PycharmProjects/AUTO_WEB_01/driverfiles/chromedriver"))
    driver.maximize_window()
    driver.get(LoginData.login_url)
    # LoginPage(driver).login(*LoginData.login_success_data) # 先登录成功
    # lg = LoginPage(driver)
    yield (driver)
    RunLog().info('----用例类后置：关闭浏览器会话，清理环境')
    driver.quit()


@pytest.fixture
def refresh_page():
    global driver
    RunLog().info('----执行用例后刷新页面')
    driver.refresh()
