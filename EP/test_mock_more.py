#!/usr/bin/env python
# -*- coding:utf-8 -*-
import contextlib
import io
from datetime import datetime, timedelta
from unittest.mock import patch
from test_mock_base import ZooDatabase, do_rounds

DATABASE = None


def get_database():
    global DATABASE
    if DATABASE is None:
        DATABASE = ZooDatabase()
    return DATABASE


def main(argv):
    database = get_database()
    species = argv[1]
    count = do_rounds(database, species)
    print(f'Fed {count} {species}(s)')
    return 0


with patch('__main__.DATABASE', spec=ZooDatabase):
    now = datetime.utcnow()
    DATABASE.get_food_period.return_value = timedelta(hours=3)
    DATABASE.get_animals.return_value = [
        ('spot', now - timedelta(minutes=4.5)),
        ('Fluffy', now - timedelta(hours=3.25)),
        ('Jojo', now - timedelta(hours=3))
    ]
    fake_stdout = io.StringIO()
    with contextlib.redirect_stdout(fake_stdout):
        main(['', 'Meerkat'])
    found = fake_stdout.getvalue()
    expected = 'Fed 2 Meerkat(s)\n'
    assert found == expected
