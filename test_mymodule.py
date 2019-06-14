#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@time: 2019/4/3 11:07

@author: ZMJ

@file: test_mymodule.py.py

'''

import sys
import pytest

pyversion = pytest.mark.skipif(sys.version_info < (3,7), reason='requires python3.6 or higher')

@pyversion
def test_function():
    return False