#!/usr/bin/env python
# -*- coding:utf-8 -*-
import copy
import gc
import sys


def test_reference_count():
    found_objects = gc.get_objects()
    print(len(found_objects))

    test_dict = {}
    ls = 78
    print(sys.getrefcount(test_dict))

    found_objects = gc.get_objects()
    print(len(found_objects))


if __name__ == '__main__':
    test_reference_count()
    found_objects = gc.get_objects()
    print(len(found_objects))

