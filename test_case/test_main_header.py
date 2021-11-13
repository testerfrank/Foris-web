#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from page.main_header import MainHeader


class TestMainHeader:
    def test_goto_market(self, main_header: MainHeader):
        """测试：点击“market”按钮，进入market页面"""
        main_header.goto_market()

