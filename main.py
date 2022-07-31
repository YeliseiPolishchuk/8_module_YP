from datetime import datetime
from names import get_first_name
from random import randint
from collections import defaultdict

users = []


def generate_human(count: int):
    '''Функция генерирует объект с именем и датой'''
    c = 0
    while c < count:
        users.append({'name': get_first_name(),
                      'birth': datetime(year=(randint(1950, 2022)), day=randint(1, 28), month=randint(1, 12))})
        c += 1


generate_human(10)


def get_birthdays_per_week(people: list) -> list:
    weekday_group = defaultdict(list)
    weekday_dict = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    for human in people:
        weekday_group[weekday_dict[human['birth'].weekday()]].append(human['name'])
    return weekday_group.items()


for i in get_birthdays_per_week(users):
    print(i)