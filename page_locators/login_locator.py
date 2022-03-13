# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/10 12:01 上午
from selenium.webdriver.common.by import By


class LoginLocator:

    user_input = (By.ID, 'username')
    pwd_input = (By.ID, 'password')
    login_btn = (By.XPATH,'//input[@value="登录"]')

    none_user_msg = (By.XPATH,'//label[text()="用户名不能为空"]')
    none_pwd_msg = (By.XPATH,'//label[text()="密码不能为空"]')
    none_input_msg = (By.XPATH,'//label[contains(text(),"不能为空")]')