# -*- coding: utf-8 -*-

"""
监控工具
"""

import time
from functools import wraps

data = {}

def register(func):
    """注册一个方法"""
    data[func.__name__] = {
        'count': 0,
        'time': 0
    }
    @wraps(func)
    def _wrapper(*args, **kwargs):
        data[func.__name__]['count'] = data[func.__name__]['count'] + 1
        start_time = time.time()
        result = func(*args, **kwargs)
        data[func.__name__]['time'] = time.time() - start_time + data[func.__name__]['time']
        return result
    return _wrapper

def report():
    """导出报告"""
    data_backup = data.copy()
    for func_name in data:
        data[func_name] = {
            'count': 0,
            'time': 0
        }
    return data_backup
