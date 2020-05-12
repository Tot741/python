time = int(input('Введите время в секундах: '))
hours = time // 3600
minute = (time - hours * 3600) // 60
second = time - hours * 3600 - minute * 60
print(f'{hours:02}:{minute:02}:{second:02}')
