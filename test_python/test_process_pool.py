# -*- coding: utf-8 -*-
"""
Copy from
https://github.com/mowshon/bounded_pool_executor
"""

from __future__ import absolute_import

import datetime
import multiprocessing
import time
import traceback
from concurrent.futures import ProcessPoolExecutor


class BoundedProcessPoolExecutor(ProcessPoolExecutor):

    def __init__(self, max_workers=None):
        if max_workers is None:
            max_workers = multiprocessing.cpu_count()
        super(BoundedProcessPoolExecutor, self).__init__(max_workers=max_workers)
        self.semaphore = multiprocessing.BoundedSemaphore(max_workers)

    def acquire(self):
        self.semaphore.acquire()

    def release(self, f):
        self.semaphore.release()

    def submit(self, fn, *args, **kwargs):
        self.acquire()
        future = super(BoundedProcessPoolExecutor, self).submit(fn, *args, **kwargs)
        future.add_done_callback(self.release)
        return future

def my_task(a, b):
    print('in func')
    return a + b



if __name__ == '__main__':
    # executors
    process_pool_executor = BoundedProcessPoolExecutor(8)
    future = process_pool_executor.submit(my_task, 1, 2)
    print('after submit')
    res = future.result(timeout=0.1)  # 真正执行的地方
    print(res)
