# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/10 12:10 上午

import pytest

from page_objects.index_page import IndexPage
from page_objects.login_page import LoginPage
from test_datas.login_data import LoginData
from commons.do_log import RunLog


@pytest.mark.usefixtures('refresh_page')
@pytest.mark.usefixtures('access_web')  # 在运行的时候，会去运行access_web函数
class TestLogin:

    # 正常登录
    @pytest.mark.smoke
    def test_login_3_success(self, access_web):
        # 输入正确的用户和密码，正确登录
        LoginPage(access_web).login(*LoginData.login_success_data)
        # 断言 登录成功页是否有退出
        try:
            assert IndexPage(access_web).isexist_logout()
            RunLog().info('测试通过-----------')
        except AssertionError:
            RunLog().error('测试失败-----------')
            raise

    # 异常登录，用户名错误,密码错误
    @pytest.mark.falsed
    @pytest.mark.parametrize('false_data',LoginData.login_failed_2_data)
    def test_login_2_failed(self, access_web,false_data):
        # 输入错误用户名或者密码，登录失败
        LoginPage(access_web).login(*false_data)
        # 断言 登录成功页是否有退出
        try:
            assert IndexPage(access_web).isexist_loginfailed()
            RunLog().info('测试通过-----------')
        except AssertionError:
            RunLog().error('测试失败-----------')
            raise

    # 异常登录，用户名或者密码为空
    @pytest.mark.falsed
    @pytest.mark.parametrize('false_data',LoginData.login_failed_1_data)
    def test_login_1_failed(self, access_web,false_data):
        # 不输入用户名或者密码，登录失败
        LoginPage(access_web).login(*false_data)
        # 断言 登录区域是否有错误提示信息
        try:
            assert LoginPage(access_web).isexist_none_input_msg()
            RunLog().info('测试通过-----------')
        except AssertionError:
            RunLog().error('测试失败-----------')
            raise


if __name__ == '__main__':
    pytest.main(['test_00_login.py -s'])
