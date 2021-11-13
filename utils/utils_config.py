#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import configparser
import os


class Config:
    def __init__(self, file):
        self.file = file
        if not os.path.exists(self.file):
            raise FileNotFoundError(f"{self.file}配置文件不存在！")
        self.config = configparser.RawConfigParser()
        self.config.read(self.file, encoding="utf-8")

    def sections(self):
        """获取所有sections"""
        return self.config.sections()

    def options(self, section):
        """获取某个section的所有options"""
        return self.config.options(section)

    def get(self, section, option):
        """获取值"""
        return self.config.get(section, option)

    def set(self, section, option, value):
        """更新值"""
        self.config.set(section, option, value)
        with open(self.file, "w", encoding="utf-8") as f:
            self.config.write(f)
