# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/9 11:59 下午

import time
from page_locators.index_locator import IndexLocator as loc
from commons.base_page import BasePage


class IndexPage(BasePage):

    # 用户登录后，是否有退出按钮
    def isexist_logout(self):
        doc = '首页—退出'
        try:
            self.wait_elevisibility(loc.logout,doc=doc)
            return True
        except:
            return False

    # 用户登录失败后，是否有登录失败信息
    def isexist_loginfailed(self):
        doc = '首页—登录失败'
        try:
            self.wait_elevisibility(loc.login_failed,doc=doc)
            return True
        except:
            return False

    def search_goods(self,goods):
        doc = '首页—搜索框-搜索商品'
        self.wait_elevisibility(loc.search_input, doc=doc)
        self.input_element(loc.search_input,goods)
        self.click_element(loc.search_btn)
        self.switch_window()

