#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

from utils.utils_time import dt_strftime


class ConfigManager:
    """目录管理"""
    # 根目录
    BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据存放目录
    DATA_DIR = os.path.join(BASEDIR, "data")

    # 浏览器驱动目录
    DRIVER_DIR = os.path.join(BASEDIR, "driver")

    # chrome浏览器驱动路径
    CHROMEDRIVER_PATH = os.path.join(DRIVER_DIR, "chromedriver.exe")

    # firefox浏览器驱动路径
    FIREFOXDRIVER_PATH = os.path.join(DRIVER_DIR, "eckodriver.exe")

    # IE浏览器驱动路径
    IEDRIVER_PATH = os.path.join(DRIVER_DIR, "EDriverServer.exe")

    # Edge浏览器驱动路径
    EDGEDRIVER_PATH = os.path.join(DRIVER_DIR, "msedgedriver.exe")

    # 页面元素存放目录
    ELEMENT_DIR = os.path.join(BASEDIR, "page_element")

    # 测试报告存放目录
    REPORT_DIR = os.path.join(BASEDIR, "report")

    @property
    def logs_file(self):
        """日志文件"""
        log_dir = os.path.join(self.BASEDIR, "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        file = os.path.join(log_dir, "{}.log".format(dt_strftime("%Y%m%d")))
        return file

    @property
    def screen_shot_file(self):
        """截图文件"""
        screen_shot_dir = os.path.join(self.BASEDIR, "screen_shot")
        if not os.path.exists(screen_shot_dir):
            os.makedirs(screen_shot_dir)
        file = os.path.join(screen_shot_dir, "{}.png".format(dt_strftime("%Y%m%d%H%M%S")))
        return file

    @property
    def screen_record_file(self):
        """视频文件"""
        screen_record_dir = os.path.join(self.BASEDIR, "screen_record")
        if not os.path.exists(screen_record_dir):
            os.makedirs(screen_record_dir)
        file = os.path.join(screen_record_dir, "{}.mp4".format(dt_strftime("%Y%m%d%H%M%S")))
        return file

    @property
    def ini_file(self):
        """config.ini配置文件"""
        file = os.path.join(self.BASEDIR, "config", "config.ini")
        if not os.path.exists(file):
            raise FileNotFoundError(f"{file}配置文件不存在！")
        return file


cm = ConfigManager()
if __name__ == "__main__":
    print("根目录：{}".format(cm.BASEDIR))
    print("测试数据存放目录:{}".format(cm.DATA_DIR))
    print("浏览器驱动目录:{}".format(cm.DRIVER_DIR))
    print("chrome浏览器驱动路径:{}".format(cm.CHROMEDRIVER_PATH))
    print("firefox浏览器驱动路径:{}".format(cm.FIREFOXDRIVER_PATH))
    print("IE浏览器驱动路径:{}".format(cm.IEDRIVER_PATH))
    print("Edge浏览器驱动路径:{}".format(cm.EDGEDRIVER_PATH))
    print("页面元素存放目录:{}".format(cm.ELEMENT_DIR))
    print("测试报告存放目录:{}".format(cm.REPORT_DIR))
    print("日志文件:{}".format(cm.logs_file))
    print("截图文件:{}".format(cm.screen_shot_file))
    print("视频文件:{}".format(cm.screen_record_file))
    print("config.ini配置文件:{}".format(cm.ini_file))
