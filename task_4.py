import requests

URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
KEY = "trnsl.1.1.20200526T044420Z.45356d47c64802bf.23948a7f49eb0b70aa9115cd6a71f6f9aca06b33"


def translate_me(mytext):
    params = {
        "key": KEY,
        "text": mytext,
        "lang": 'en-ru'
    }
    response = requests.get(URL, params=params)
    response = response.json()
    return ''.join(response['text'])


try:
    with open('text_4.txt') as read_obj:
        with open('text_4_ru.txt', 'w', encoding='utf-8') as write_obj:
            for line in read_obj:
                line = line.split()
                ru = translate_me(line[0])
                print(ru, line[1], line[2], file=write_obj)
except FileNotFoundError:
    print('Файл с данными не найден или имеет неправильное имя.\nИмя файла должно быть text_4.txt')
