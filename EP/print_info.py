#!/usr/bin/env python
# -*- coding:utf-8 -*-

print(5)
print('5')

print(repr(5))
print(repr('5'))
print({'runoob': 'runoob.com', 'google': 'google.com'}, repr({'runoob': 'runoob.com', 'google': 'google.com'}))
print([1, '2'], repr([1, '2']))

# print('%r' % 5)
# print('%r' % '5')
#
# int_value = 5
# str_value = '5'
# print(f'{int_value!r}')
# print(f'{str_value!r}')

class OpaqueClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = OpaqueClass(1, '1')
print(obj)


class BetterClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'BetterClass({self.x!r}, {self.y!r})'


obj = BetterClass(2, '2')
print(obj)

obj = OpaqueClass(4, '4')
print(obj.__dict__)


