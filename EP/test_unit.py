#!/usr/bin/env python
# -*- coding:utf-8 -*-
from unittest import TestCase, main


# class UtilsErrorTestCase(TestCase):
#     def test_to_str_bad(self):
#         with self.assertRaises(TypeError):
#             list(2)

class NumbersTest(TestCase):
    def test_even(self):
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

    # def test_odd(self):
    #     for i in range(0, 6):
    #         self.assertEqual(i % 2, 1)



