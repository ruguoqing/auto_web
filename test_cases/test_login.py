# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/10 12:10 上午

import unittest
from ddt import ddt, data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from page_objects.login_page import LoginPage
from page_objects.index_page import IndexPage
from test_datas.login_data import LoginData
from commons.do_log import RunLog


@ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service("../driverfiles/chromedriver"))
        cls.driver.get(LoginData.login_url)

        window_handles = cls.driver.window_handles
        cls.driver.switch_to.window(window_handles[-1])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self) -> None:
        self.driver.refresh()

    # 正常登录
    def test_login_3_success(self):
        # 输入正确的用户和密码，正确登录
        LoginPage(self.driver).login(*LoginData.login_success_data)
        # 断言 登录成功页是否有退出
        try:
            self.assertTrue(IndexPage(self.driver).isexist_logout())
            RunLog().info('测试通过-----------')
        except:
            RunLog().error('测试失败-----------')
            raise

    # 异常登录，用户名错误,密码错误
    @data(*LoginData.login_failed_2_data)
    def test_login_2_failed(self, false_data):
        # 输入错误用户名或者密码，登录失败
        LoginPage(self.driver).login(*false_data)
        # 断言 登录成功页是否有退出
        try:
            self.assertFalse(IndexPage(self.driver).isexist_logout())
            RunLog().info('测试通过-----------')
        except:
            RunLog().error('测试失败-----------')
            raise

    # 异常登录，用户名或者密码为空
    @data(*LoginData.login_failed_1_data)
    def test_login_1_failed(self, false_data):
        # 不输入用户名或者密码，登录失败
        LoginPage(self.driver).login(*false_data)
        # 断言 登录区域是否有错误提示信息
        try:
            self.assertTrue(LoginPage(self.driver).isexist_none_input_msg())
            RunLog().info('测试通过-----------')
        except:
            RunLog().error('测试失败-----------')
            raise


if __name__ == '__main__':
    unittest.main('-s')
