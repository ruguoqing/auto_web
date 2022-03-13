# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/9 10:23 上午


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("../driverfiles/chromedriver")
driver = webdriver.Chrome(service=s)

# 滚动鼠标 用js脚本执行
element = 'ele'
# 找到元素element对象的底端与当前窗口的底部对齐
driver.execute_script("arguments[0].scrollIntoView(false);",element)
# 找到元素element对象的顶端与当前窗口的顶部对齐
driver.execute_script("arguments[0].scrollIntoView();",element)
# 移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# 移动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0);")

# 执行js语句 对应dom 元素执行一系列操作
js = 'var ele = docuemnt.getElementById("train_date");ele.readonly = false;ele.value="2022-03-15";'
driver.execute_script(js)