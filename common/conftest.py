#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/17 21:39
# @Author  : Mannix
# @Site    : 
# @File    : conftest.py.py
# @Software: PyCharm

import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def driver(request):
    driver = webdriver.Chrome

    def end():
        driver.quit()
    request.addfinalizer(end)
    return driver