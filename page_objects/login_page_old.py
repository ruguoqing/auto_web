# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/9 11:55 下午

from page_locators.login_locator import LoginLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from commons.do_log import RunLog

# 登录操作
class LoginPage:
    # print(loc.user_input)
    def __init__(self, driver):
        self.driver = driver

    # 输入用户名，密码，点击登录
    def login(self, user, pwd):
        RunLog().info('---找元素吧----')
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((loc.user_input)))
        self.driver.find_element(*loc.user_input).send_keys(user)
        self.driver.find_element(*loc.pwd_input).send_keys(pwd)
        self.driver.find_element(*loc.login_btn).click()

    def isexist_none_input_msg(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((loc.none_input_msg)))
            return True
        except:
            return False