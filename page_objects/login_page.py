# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/9 11:55 下午
import datetime
from page_locators.login_locator import LoginLocator as loc
from commons.base_page import BasePage


# 登录操作
class LoginPage(BasePage):
    # 输入用户名，密码，点击登录

    def login(self, user, pwd):
        doc = '登录页面—点击登录'
        self.wait_elevisibility(loc.user_input, doc=doc)
        self.input_element(loc.user_input, user, doc=doc)
        self.input_element(loc.pwd_input, pwd, doc=doc)
        self.click_element(loc.login_btn, doc=doc)

        # WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((loc.user_input)))
        # self.driver.find_element(*loc.user_input).send_keys(user)
        # self.driver.find_element(*loc.pwd_input).send_keys(pwd)
        # self.driver.find_element(*loc.login_btn).click()

    def isexist_none_input_msg(self):
        doc = '登录页面_点击登录_错误'
        try:
            self.wait_elevisibility(loc.none_input_msg, doc=doc)
            return True
        except:
            return False
