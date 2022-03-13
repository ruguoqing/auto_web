# -*- coding: utf-8 -*-
# Author : ruguo
# Time : 2022/3/10 12:50 上午

class LoginData:
    login_url = 'http://121.41.14.39:6001/user/login.htm'
    login_success_data = ('sqsq001', "123456")
    login_failed_1_data = [
        ('', ""),
        ('', "123456"),
        ('sqsq001', "")
    ]
    login_failed_2_data = [
        ('ssaaaa', "123456"),
        ('sqsq001', "1234567"),
        ('ssaaaa', "1234567")
    ]


if __name__ == '__main__':
    a = LoginData.login_success_data
    print(a)