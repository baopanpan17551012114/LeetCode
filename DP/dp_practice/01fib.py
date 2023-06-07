#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
"""

class Solution:
    def fib(self, n: int) -> int:
        # base case
        if n == 1 or n == 0:
            return n
        return self.fib(n-1) + self.fib(n-2)
