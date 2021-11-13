#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os

import allure
import pytest
from _pytest.config.argparsing import Parser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as CS
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.edge.service import Service as ES
from selenium.webdriver.firefox.service import Service as FS
from selenium.webdriver.ie.service import Service as IS

from common.readconfig import ini
from config.conf import cm
from page.main_header import MainHeader
from utils.utils_time import sleep

_driver: WebDriver = None


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    """初始化浏览器"""
    global _driver
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        options = Options()
        # 无痕模式
        options.add_argument("incognito")
        # 无界面模式
        # options.add_argument("headless")
        # 允许自动化控制，且不提示
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # 远程调试模式
        # options.debugger_address = "127.0.0.1:9222"
        service = CS(cm.CHROMEDRIVER_PATH)
        _driver = webdriver.Chrome(options=options, service=service)
    elif browser == "firefox":
        service = FS(cm.FIREFOXDRIVER_PATH)
        _driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        service = ES(cm.EDGEDRIVER_PATH)
        _driver = webdriver.Edge(service=service)
    elif browser == "ie":
        service = IS(cm.IEDRIVER_PATH)
        _driver = webdriver.Ie(service=service)
    env = request.config.getoption("--env")
    if env == "dev":
        _driver.get(ini.dev_url)
    elif env == "main":
        _driver.get(ini.main_url)
    elif env == "baseline":
        _driver.get(ini.baseline_url)

    yield _driver
    sleep(10)
    _driver.quit()


@pytest.fixture(scope="function", autouse=True)
def main_header(browser):
    browser.maximize_window()
    main_header = MainHeader(browser)
    return main_header


def fail_picture():
    _driver.save_screenshot(cm.screen_shot_file)
    file = cm.screen_shot_file
    allure.attach.file(file, "失败用例截图：{}".format(file), allure.attachment_type.PNG)


def pytest_collection_modifyitems(items):
    print(items)
    print(len(items))
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode-escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode-escape")


def pytest_addoption(parser: Parser):
    my_group = parser.getgroup("my_group")
    my_group.addoption("--env", action="store", default="dev", dest="env", help="设置运行环境，可选项：dev,main,baseline")
    my_group.addoption("--browser", action="store", default="chrome", dest="browser",
                       help="设置运行浏览器，可选项：chrome,firefox,edge,ie")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = "(%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(report.nodeid + extra + "\n")
        fail_picture()
