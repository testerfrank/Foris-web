#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

import yaml

from config.conf import cm


class ReadElement:
    def __init__(self, filename):
        self.file = f"{filename}.yaml"
        self.file_path = os.path.join(cm.ELEMENT_DIR, self.file)
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"{self.file_path}文件不存在！")
        with open(self.file_path, encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        data = self.data.get(item)
        if data:
            by, locator = data["by"], data["locator"]
            return by, locator
        raise ArithmeticError(f"{self.file}中不存在关键字{item}")
