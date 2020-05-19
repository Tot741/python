def user_list(name='', s_name='', birthday='', city='Москва', email='Отсутствует', tel='Отсутствует'):
    return f'Пользователь {name} {s_name} родился в {birthday} году. Проживает в городе {city}, адрес электронной почты - {email}, телефон - {tel}'


name = input('Введите имя пользователя: ')
s_name = input('Введите фамилию пользователя: ')
birthday = input('Введите год рождения пользователя: ')
city = input('Введите город проживания пользователя: ')
email = input('Введите адрес электронной почты пользователя: ')
tel = input('Введите номер телефона пользователя: ')
print(user_list(name, s_name, birthday, city, email, tel))
