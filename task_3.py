class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = ''
list_of_number = []
while inp_data != 'stop':
    inp_data = input('Введите число или "stop" для прекращения ввода: ')

    try:
        if inp_data.isdigit() == False and inp_data != 'stop':
            raise OwnError("Вы ввели не число")
        elif inp_data == 'stop':
            break
    except OwnError as err:
        print(err)
    else:
        inp_data = int(inp_data)
        list_of_number.append(inp_data)

print(f'Итоговый список чисел - {list_of_number}')
