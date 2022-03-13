# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/11 6:37 下午

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from test_datas.login_data import LoginData
from test_datas.index_data import IndexData
from commons.do_log import RunLog
from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from page_objects.searchres_page import SearchResPage


class TestIndex(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        RunLog().info('----用例类前置：初始化浏览器会话，登录商城系统')
        cls.driver = webdriver.Chrome(service=Service("../driverfiles/chromedriver"))
        cls.driver.maximize_window()
        cls.driver.get(LoginData.login_url)
        cls.lg = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        RunLog().info('----用例类后置：关闭浏览器会话，清理环境')
        cls.driver.quit()

    def tearDown(self) -> None:
        RunLog().info('----执行用例后刷新页面')
        self.driver.refresh()

    # 搜索存在的商品
    def test_searchgoods_exist(self):
        self.lg.login(*LoginData.login_success_data)
        IndexPage(self.driver).search_goods(IndexData.goods_exist)
        try:
            self.assertTrue(SearchResPage(self.driver).isexist_goods())
            RunLog().info('测试通过-----------')
        except:
            RunLog().error('测试失败-----------')
            raise

    # 搜索不存在的商品
    def test_searchgoods_noexist(self):
        IndexPage(self.driver).search_goods(IndexData.goods_noexist)
        try:
            self.assertTrue(SearchResPage(self.driver).noexist_goods())
            RunLog().info('测试通过-----------')
        except:
            RunLog().error('测试失败-----------')
            raise


if __name__ == '__main__':
    unittest.main('-s')