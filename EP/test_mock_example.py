#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
from unittest.mock import Mock, patch, DEFAULT


def get_animals(database, species):
    return species.get(''), database[11]


def get_food_period(database, species):
    # 查询数据库，获取时间间隔
    pass


def feed_animal(database, name, when):
    # 写入数据库
    pass


def do_rounds(database, species):
    now = datetime.utcnow()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0
    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1
    return fed


# 一种办法是把想要注入模拟逻辑的地方全都改成 只能通过关键字来指定的参数
def do_rounds_1(database, species, *,
                now_func=datetime.utcnow,
                food_func=get_food_period,
                animal_func=get_animals,
                feed_func=feed_animal
                ):
    now = now_func()
    feeding_timedelta = food_func(database, species)
    animals = animal_func(database, species)
    fed = 0
    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_func(database, name, now)
            fed += 1
    return fed

# 为了测试do_rounds函数，必须先把所有的Mock实例创建出来，并 把它们在受到调用时所应返回的值指定好。
now_func = Mock(spec=datetime.utcnow)
now_func.return_value = datetime(2022, 6, 5, 15, 45)

food_func = Mock(spec=get_food_period)
food_func.return_value = timedelta(hours=3)

animal_func = Mock(spec=get_animals)
animal_func.return_value = [
    ('spot', datetime(2022, 6, 5, 11, 15)),
    ('Fluffy', datetime(2022, 6, 5, 12, 30)),
    ('Jojo', datetime(2022, 6, 5, 12, 45))
]

feed_func = Mock(spec=feed_animal)

result = do_rounds_1(object(), 'Meerkat',
                     now_func=now_func,
                     food_func=food_func,
                     animal_func=animal_func,
                     feed_func=feed_func)
assert result == 2


# 2、用unittest.mock.patch系列的函数来注入mock逻辑要比这简单。
def do_rounds_2(database, species, *, utcnow=datetime.utcnow):
    now = utcnow()
    feeding_timedelta = get_food_period(database, species)
    animals = get_animals(database, species)
    fed = 0
    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            feed_animal(database, name, now)
            fed += 1
    return fed


with patch.multiple('__main__',
                    get_food_period=DEFAULT,
                    get_animals=DEFAULT,
                    feed_animal=DEFAULT):
    now_func = Mock(spec=datetime.utcnow)
    now_func.return_value = datetime(2022, 6, 5, 15, 45)

    get_food_period.return_value = timedelta(hours=3)

    get_animals.return_value = [
        ('spot', datetime(2022, 6, 5, 11, 15)),
        ('Fluffy', datetime(2022, 6, 5, 12, 30)),
        ('Jojo', datetime(2022, 6, 5, 12, 45))
    ]

    res = get_animals('', '')
    print(res)

    result = do_rounds_2(object(), 'Meerkat', utcnow=now_func)
    assert result == 2