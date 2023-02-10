#!/usr/bin/env python
# -*- coding:utf-8 -*-
from unittest import TestCase, main

# 作用于一个文件，整个文件级别上只调用一次 setUp/tearDown
def setUpModule():
    print('setUpModule')


def tearDownModule():
    print('tearDownModule')


class EnvironmentTest(TestCase):
    # 全程只调用一次setUpClass()/tearDownClass(),必须使用@classmethod 装饰器
    @classmethod
    def setUpClass(cls):
        print('setUpClass1')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass1')

# 每个测试方法执行前执行
    def setUp(self):
        print('setUp')

    # 每个测试方法执行后执行
    def tearDown(self):
        print('tearDown')

    def test_test1(self):
        print('test_test1')

    def test_test2(self):
        print('test_test2')


class EnvironmentTest2(TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass2')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass2')

    # 每个测试方法执行前执行
    def setUp(self):
        print('setUp2')

    # 每个测试方法执行后执行
    def tearDown(self):
        print('tearDown2')

    def test_test1(self):
        print('test_test2_1')

    def test_test2(self):
        print('test_test2_2')


if __name__ == '__main__':
    main()
