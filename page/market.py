#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from base.basepage import BasePage
from common.readelement import ReadElement
from page.trade import Trade
from utils.utils_time import sleep

markets_element = ReadElement("market")


class Market(BasePage):
    """market页面"""

    def switch_to_usdc(self):
        """
        点击“USDC”
        :return:
        """
        # 显示等待
        self.wait_for_element(5, markets_element["USDC"])
        # 点击“USDC”
        self.find_and_click(markets_element["USDC"])

    def goto_trade_page(self):
        """
        点击"CRO/USDC",返回trade page
        :return:
        """
        self.wait_for_element(5, markets_element["CRO/USDC"])
        self.find_and_click(markets_element["CRO/USDC"])
        return Trade(self._driver)
