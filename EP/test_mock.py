#!/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from datetime import datetime
from unittest.mock import Mock, ANY, MagicMock, create_autospec


class DatabaseConnection:
    pass


def get_animals(database, species):
    pass


mock = Mock(spec=get_animals)
expected = [
    ('spot', datetime(2022, 6, 5, 11, 15)),
    ('Fluffy', datetime(2022, 6, 5, 12, 30)),
    ('Jojo', datetime(2022, 6, 5, 12, 45))
]
mock.return_value = expected

database = object()
result = mock(database, 'Meerkat')
assert result == expected

# 我们还想知道，程序在调用mock时给第二个参数所传的值是不是指定的值 （也就是'Meerkat'）
mock.assert_called_once_with(database, 'Meerkat')
# mock.assert_called_once_with(database, 'Giraffe')
"""
AssertionError: Expected call: mock(<object object at 0x7f91680a01c0>, 'Giraffe')
Actual call: mock(<object object at 0x7f91680a01c0>, 'Meerkat')
"""

# 如果我们不关心某个参数的取值, 那么可以用unittest.mock.ANY常量表达这个意思
# 只要参数的取值不影响要测试的关键行为，那就可以在验证时通过 ANY忽略这个参数。
mock.assert_called_with(ANY, 'Meerkat')


# Mock类还能够模拟调用时抛出异常的情况
class MyError(Exception):
    def __init__(self, message):
        self.message = message

mock = Mock(spec=get_animals)
# mock.side_effect = MyError('big problem')
result = mock(database, 'Meerkat')


# side_effect参数和return_value是相反的。它给mock分配了可替换的结果，覆盖了return_value。
# 简单的说，调用将返回side_effect值，而不是return_value。
def side_effect(a, b, c):
    return a, b, c


mock = Mock(return_value=13, side_effect=side_effect)
result1 = mock(1, 2, 3)
print(result1)

