from sys import argv


def wages(hours, rate, reward):
    hours, rate, reward = float(hours), float(rate), float(reward)
    return round((hours * rate + reward), 2)


try:
    script_name, hours, rate, reward = argv
    print(f'Заработная плата составит {wages(hours, rate, reward)}')
except ValueError:
    print(
        '!!!Неверные входные данные!!!\nДля расчета заработной платы необхдимо запустить скрипт\nс 3 параметрами - количеством отработанных часов, ставкой и премией.\nНапример:\npython task_1.py 80 500 5000')
