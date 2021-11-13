#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from page.main_header import MainHeader
from utils.utils_time import sleep


class TestTrade:
    def test_favorite(self, main_header: MainHeader):
        """测试：收藏”CRO/USDC“后，验证CRO/USDC在收藏列表中"""
        # 点击market，进入market页面
        market = main_header.goto_market()
        # 切换到usdc
        market.switch_to_usdc()
        # 点击CRO/USDC, 进入trade页面
        trade = market.goto_trade_page()
        # # 点击左侧收藏图标
        trade.imp_wait(20)
        trade.click_favorite()
        # 点击现货交易列表
        trade.click_trade_pair_list()
        # 切换到收藏列表
        trade.switch_to_favorites()
        # 搜索CRO/USDC
        trade.search("CRO/USDC")
        # 获取搜索结果
        text = trade.search_result()
        # 验证搜索结果
        assert "CRO/USDC" in text
