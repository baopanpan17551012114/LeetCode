#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime, timedelta
from unittest.mock import Mock, patch


class ZooDatabase:
    def get_animals(self, species):
        pass

    def get_food_period(self, species):
        pass

    def feed_animal(self, name, when):
        pass


def do_rounds(database, species, *, utcnow=datetime.utcnow):
    now = utcnow()
    feeding_timedelta = database.get_food_period(database, species)
    animals = database.get_animals(database, species)
    fed = 0
    for name, last_mealtime in animals:
        if (now - last_mealtime) > feeding_timedelta:
            database.feed_animal(database, name, now)
            fed += 1
    return fed


now_func = Mock(spec=datetime.utcnow)
now_func.return_value = datetime(2022, 6, 5, 15, 45)

database = Mock(spec=ZooDatabase)
database.get_food_period.return_value = timedelta(hours=3)
database.get_animals.return_value = [
    ('spot', datetime(2022, 6, 5, 11, 15)),
    ('Fluffy', datetime(2022, 6, 5, 12, 30)),
    ('Jojo', datetime(2022, 6, 5, 12, 45))
]

result = do_rounds(database, 'Meerkat', utcnow=now_func)
assert result == 2