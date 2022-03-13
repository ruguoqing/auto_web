# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/10 8:29 下午
import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from commons.do_log import RunLog
from commons.path_config import screenshots_path


# 实现日志记录，截图功能，异常捕捉
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素出现
    def wait_elevisibility(self, loc, timeout=20, poll_frequency=0.5, doc='等待元素截图'):
        '''
        :param loc: 元素定位，元组形式（定位方式，定位地址）
        :param timeout: 最长等待时长
        :param poll_frequency: 检查频率
        :param doc: 截屏文件
        :return:
        '''
        RunLog().info(f'等待元素{loc}可见')
        try:
            start_time = datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(ec.visibility_of_element_located(loc))
            finish_time = datetime.datetime.now()
            spend_time = (finish_time - start_time).seconds
            RunLog().info(f'元素已经出现，等待时长为：{spend_time}')
        except:
            RunLog().error(f'没有等到元素{loc}')
            self.save_page_screenshot(doc)
            raise

    # 找到元素
    def __get_element(self, loc, doc='查找元素截图'):
        RunLog().info(f'开始查找元素{loc}')
        try:
            return self.driver.find_element(*loc)
        except:
            RunLog().error(f'未找到元素{loc}')
            self.save_page_screenshot(doc)

    # 元素输入
    def input_element(self, loc, text, doc='元素输入截图'):
        ele = self.__get_element(loc, doc)
        RunLog().info(f'在元素{loc}输入值{text}')
        try:
            ele.send_keys(text)
        except:
            RunLog().error('元素输入失败')
            self.save_page_screenshot(doc)

    # 元素点击
    def click_element(self, loc, doc='点击元素截图'):
        ele = self.__get_element(loc, doc)
        RunLog().info(f'点击元素{loc}')
        try:
            ele.click()
        except:
            RunLog().error('元素点击失败')
            self.save_page_screenshot(doc)

    # 页面截图
    def save_page_screenshot(self, filename):
        # 文件名称可包含模块名称，页面名称，页面操作，当前时间 png格式
        filepath = screenshots_path + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + filename + '.png'
        try:
            self.driver.save_screenshot(filepath)
            RunLog().info(f'截图成功,截图文件为{filename}')
        except:
            RunLog().error('截图失败')

    # 窗口跳转
    def switch_window(self, number=-1, doc='窗口跳转截图'):
        window_handles = self.driver.window_handles
        # print(window_handles)
        # print(window_handles[-2])
        RunLog().info(f'开始跳转窗口到{window_handles[number]}')
        try:
            self.driver.switch_to.window(window_handles[number])
            RunLog().info('跳转窗口成功')
        except:
            RunLog().info('跳转窗口失败')
            self.save_page_screenshot(doc)

    # 关闭当前窗口
    def close_current_window(self,doc='关闭窗口截图'):
        RunLog().info('开始关闭当前窗口}')
        try:
            self.driver.execute_script("window.close();")
            RunLog().info('关闭当前窗口成功')
        except:
            RunLog().info('关闭当前窗口失败')
            self.save_page_screenshot(doc)

    # iframe切换
    def switch_iframe(self, loc,doc='跳转frame截图'):
        frame = self.__get_element(loc)
        RunLog().info('开始跳转frame}')
        try:
            self.driver.switch_to.frame(frame)
            RunLog().info('跳转frame成功')
        except:
            RunLog().info('跳转frame失败')
            self.save_page_screenshot(doc)

    # alert处理,默认确定
    def alert_option(self, mode=1,doc='关闭弹框截图'):
        alert = self.driver.switch_to.alert
        try:
            if mode == 1:
                RunLog().info('即将点击确定关闭弹框')
                alert.accept()
            else:
                RunLog().info('即将点击取消关闭弹框')
                alert.dismiss()
            RunLog().info('关闭弹框成功')
        except:
            RunLog().info('关闭弹框失败')
            self.save_page_screenshot(doc)


