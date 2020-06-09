class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def date_number(cls, date_string):
        try:
            temp_list = date_string.split('-')
            day = int(temp_list[0])
            month = int(temp_list[1])
            year = int(temp_list[2])
            return day, month, year
        except ValueError:
            print('Введены неверные данные. Данные должны быть в формате "дд-мм-гггг"')

    @staticmethod
    def check_date(day, month, year):
        if 1 <= day <= 31:
            print(f'{day} - введен корректный день')
        else:
            print(f'{day} -  введен некорректный день')
        if 1 <= month <= 12:
            print(f'{month} - введен корректный месяц')
        else:
            print(f'{month} -  введен некорректный месяц')
        if 1 <= year <= 3000:
            print(f'{year} - введен корректный год')
        else:
            print(f'{year} -  введен некорректный год')


try:
    a = Date('12-05-2020')
    d, m, y = a.date_number('12-05-2020')
    print(Date.date_number('12-05-2020'))
    Date.check_date(d, m, y)
except TypeError:
    pass
