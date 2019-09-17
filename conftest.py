#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/3/19 20:09

@author: ZMJ

@file: conftest.py

'''

from selenium import webdriver
import pytest

driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped) and xfail or (report.failed and not xfail):
            file_name = report.nodeid.replace('::', '_')+'.png'
            screen_img = _capture_screenshot()
            if file_name:
                html = "<div><img src='data:image/png;base64,%s' alt='screenshot', style='width:600px;height:300px;'"\
                       "onclick='window.open(this.src)' align='right'/></div>" % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
        # report.description = str(item.funciton.__doc__)

# @pytest.mark.optionalhook
# def pytest_html_result_table_header(cells):
#     cells.insert(1, html.th('D'))

def _capture_screenshot():
    return driver.get_screenshot_as_base64()

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver

@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver

@pytest.fixture()
def login():
    print('输入账号，密码先登录')

@pytest.fixture(scope='session')
def first1():
    print('score=session')
    a = 'yoyo'
    return a

