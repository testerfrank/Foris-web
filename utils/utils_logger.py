#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import logging

from config.conf import cm


class Log:
    def __init__(self):
        # 创建日志对象
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 创建handler写入文件
        fh = logging.FileHandler(cm.logs_file, encoding="utf-8")
        fh.setLevel(logging.INFO)

        # 创建handler输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义日志输出格式formatter
        formatter = logging.Formatter(self.fmt)

        # 给handler添加formatter
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给日志添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        # 关闭文件
        fh.close()
        ch.close()

    @property
    def fmt(self):
        """日志输出格式"""
        return "[%(asctime)s]\t[%(filename)s:%(funcName)s]\t[line:%(lineno)d]\t%(levelname)s\t %(message)s"


log = Log().logger
if __name__ == "__main__":
    log.info("日志记录")
