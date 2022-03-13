# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/10 12:32 上午

from selenium.webdriver.common.by import By


class IndexLocator:

    logout = (By.XPATH, '//a[text()="[退出]"]')
    login_failed = (By.XPATH, '//span[text()="登录失败！"]')
    # 产品搜索
    search_input = (By.ID, 'keyword')
    search_btn = (By.XPATH, '//input[@name="input"]')


