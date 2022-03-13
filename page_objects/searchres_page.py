# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/11 7:19 下午
from page_locators.searchres_locator import SearchResLocator as loc
from commons.base_page import BasePage

# 登录操作
class SearchResPage(BasePage):

    # 商品查询结果
    def isexist_goods(self):
        doc = '商品查询-查询结果-有商品'
        try:
            self.wait_elevisibility(loc.smallgoods,doc=doc)
            return True
        except:
            return False

    def noexist_goods(self):
        doc = '商品查询-查询结果-没有商品'
        try:
            self.wait_elevisibility(loc.no_goods,doc=doc)
            return True
        except:
            return False