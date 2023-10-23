#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。
"""


# 第一种：普通装饰器
def logger(func):
    def wrapper(*args, **kwargs):
        print('执行之前......')
        func(*args, **kwargs)
        print('执行之后......')
    return wrapper

# @logger
def add(x, y):
    print('{} + {} = {}'.format(x, y, x+y))

my_fun = logger(add)


# 第二种：带参数的函数装饰器
def logger_with_args(country):
    def wrapper(func):
        def deco(*args, **kwargs):
            if country == 'china':
                print('你好', end='_')
            if country == 'america':
                print('hello', end='_')
            # 函数执行的地方
            func(*args, **kwargs)
        return deco
    return wrapper

# @logger_with_args('china')
def send(message):
    print(message)

my_fun1 = logger_with_args('china')
my_fun2 = my_fun1(send)


# 第三种：不带参数的类装饰器
"""
基于类装饰器的实现，必须实现 __call__ 和 __init__两个内置函数。 __init__ ：接收被装饰函数 __call__ ：实现装饰逻辑。
"""

class DecoratorCla:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('function_name: {0}'.format(self.func.__name__))
        self.func(*args, **kwargs)

# @DecoratorCla
def say(something):
    print("say {}!".format(something))

my_cla = DecoratorCla(say)


# 第四种：带参数的类装饰器
# __init__ ：不再接收被装饰函数，而是接收传入参数。 __call__ ：接收被装饰函数，实现装饰逻辑。
class DecoratorClaArgs:
    def __init__(self, level):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print("[{level}]: the function {func}() is running..." \
                  .format(level=self.level, func=func.__name__))
            func(*args, **kwargs)
        return wrapper

# @DecoratorClaArgs('WARNING')
def say1(something):
    print("say {}!".format(something))

my_cla1 = DecoratorClaArgs('WARNING')
my_cla2 = my_cla1(say1)


# 第五种：使用偏函数与类实现装饰器
import time
import functools

class DelayFunc:
    def __init__(self,  duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)


def delay(duration):
    """
    装饰器：推迟某个函数的执行。
    """
    # 此处为了避免定义额外函数，直接使用 functools.partial 帮助构造 DelayFunc 实例
    return functools.partial(DelayFunc, duration)

@delay(duration=2)
def add1(x, y):
    print('{} + {} = {}'.format(x, y, x+y))


if __name__ == '__main__':
    # my_fun(2, 4)
    # my_fun2('我爱你')
    # my_cla('我爱你')
    # my_cla2('我爱你')
    add1(3, 5)