#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from page.main_header import MainHeader


class TestMarket:
    def test_goto_trade(self, main_header: MainHeader):
        """测试：点击CRO/USDC，进入CRO/USDC交易页面"""
        market = main_header.goto_market()
        market.switch_to_usdc()
        market.goto_trade_page()
