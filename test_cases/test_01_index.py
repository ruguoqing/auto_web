# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/11 6:37 下午

import pytest
from test_datas.login_data import LoginData
from page_objects.login_page import LoginPage
from test_datas.index_data import IndexData
from commons.do_log import RunLog
from page_objects.index_page import IndexPage
from page_objects.searchres_page import SearchResPage


@pytest.mark.usefixtures('refresh_page')
@pytest.mark.usefixtures('access_web')  # 在运行的时候，会去运行access_web函数
class TestIndex():

    # 搜索存在的商品
    @pytest.mark.smoke
    def test_searchgoods_exist(self, access_web):
        LoginPage(access_web).login(*LoginData.login_success_data)
        IndexPage(access_web).search_goods(IndexData.goods_exist)
        try:
            assert SearchResPage(access_web).isexist_goods()
            RunLog().info('测试通过-----------')
        except AssertionError:
            RunLog().error('测试失败-----------')
            raise
        IndexPage(access_web).switch_window(0)  # 待后续有想法去优化，考虑是不是把这个方法写在 page 比较好

    # 搜索不存在的商品
    def test_searchgoods_noexist(self, access_web):
        IndexPage(access_web).search_goods(IndexData.goods_noexist)
        try:
            assert SearchResPage(access_web).noexist_goods()
            RunLog().info('测试通过-----------')
        except AssertionError:
            RunLog().error('测试失败-----------')
            raise
        IndexPage(access_web).switch_window(0)


if __name__ == '__main__':
    pytest.main(['test_01_index.py', '-s', '--alluredir=outputs/allure_reports'])
