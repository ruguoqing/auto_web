# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/11 7:15 下午
from selenium.webdriver.common.by import By


class SearchResLocator:
    smallgoods = (By.CLASS_NAME, 'smallgoods')
    no_goods = (By.XPATH,'//b[text()="对不起，没有对应的数据!"]')
