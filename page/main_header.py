#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from base.basepage import BasePage
from common.readelement import ReadElement
from page.market import Market

main_header_element = ReadElement("main_header")


class MainHeader(BasePage):
    """头部导航栏"""

    def goto_exchange(self):
        """
        点击”crypto.com“logo图标
        返回exchange页面
        :return:
        """
        pass

    def goto_market(self):
        """
        点击”market“按钮，返回market页面
        :return:
        """
        self.find_and_click(main_header_element["markets"])
        return Market(self._driver)

    def goto_spot(self):
        """
        点击”spot"按钮，返回spot页面
        :return:
        """
        pass

    def goto_margin(self):
        """
        点击“margin”按钮，返回margin页面
        :return:
        """
        pass

    def goto_derivatives(self):
        """
        点击”derivatives“，返回derivatives页面
        :return:
        """
        pass

    def goto_lending(self):
        """
        点击“lending”按钮，返回lending页面
        :return:
        """
        pass

    def goto_login(self):
        """
        点击“login”按钮，返回login页面
        :return:
        """
        pass

    def goto_signup(self):
        """
        点击“sign up”按钮，返回sign up页面
        :return:
        """
        pass
