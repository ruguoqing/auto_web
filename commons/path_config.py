# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/11 5:14 下午
import datetime
import os

# 当前文件路径
base_dir = os.path.abspath(__file__)
base_path = base_dir.split('/commons/path_config.py')[0]
print(base_path)
# 日志路径
logs_path = os.path.join(base_path,'outputs/logs/run_test_logs.txt')
# 截图路径
screenshots_path = os.path.join(base_path,'outputs/screenshots/')
# 登录地址
login_url = 'http://121.41.14.39:6001/user/login.htm'
