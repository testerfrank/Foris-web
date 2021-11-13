#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from config.conf import cm
from utils.utils_config import Config


class ReadConfig:
    _cf = Config(cm.ini_file)

    @property
    def dev_url(self):
        """获取dev_url值"""
        return self._cf.get("environment", "dev_url")

    @dev_url.setter
    def dev_url(self, value):
        """设置dev_url值"""
        self._cf.set("environment", "dev_url", value)


ini = ReadConfig()
if __name__ == "__main__":
    print(ini.dev_url)
