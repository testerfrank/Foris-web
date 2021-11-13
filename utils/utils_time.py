#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import datetime
import time
from functools import wraps


def timestamp():
    """返回时间戳"""
    return time.time()


def sleep(seconds=3):
    """休眠时间"""
    time.sleep(seconds)


def dt_strftime(fmt="%Y%m%d"):
    """返回当前日期时间格式化字符串"""
    return datetime.datetime.now().strftime(fmt)


def running_time(func):
    """函数运行时间"""

    @wraps
    def wrappers(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("{}运行完成！耗时{}".format(func.__name__, timestamp() - start))
        return res

    return wrappers
