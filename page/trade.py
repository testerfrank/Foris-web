#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from base.basepage import BasePage
from common.readelement import ReadElement

trade_element = ReadElement("trade")


class Trade(BasePage):
    """trade页面"""

    def click_favorite(self):
        """点击收藏"""
        self.scroll(0, -10000)
        self.find_and_click(trade_element["favorite"])

    def click_trade_pair_list(self):
        """点击现货交易列表"""
        self.wait_for_element(20, trade_element["trade-pair-list"])
        self.find_and_click(trade_element["trade-pair-list"])

    def switch_to_favorites(self):
        """现货交易列表中点击”Favorites“"""
        self.find_and_click(trade_element["Favorites"])

    def search(self, text):
        self.find_and_send(trade_element["search"], text)

    def search_result(self):
        return self.get_text(trade_element["favorities-search-result"])
