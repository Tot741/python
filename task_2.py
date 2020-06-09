class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


number_1 = input("Введите целое число (делимое): ")
number_2 = input("Введите целое число (делитель): ")

try:
    number_1 = int(number_1)
    number_2 = int(number_2)
    if number_2 == 0:
        raise OwnError("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f'Результат деления - {number_1 / number_2}')
