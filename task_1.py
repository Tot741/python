import time


class TrafficLight:
    __color = {'red': 7, 'yellow': 2, 'green': 7}

    def running(self):
        pass
        while True:
            for t in self.__color:
                if t == 'red':
                    print(f'\033[31m\U00000298', end='')
                elif t == 'yellow':
                    print(f'\033[33m\U000000a4',
                          end='')  # здесь специально другой символ, а то желтый не сильно от зеленного отличается
                else:
                    print(f'\033[32m\U00000298', end='')
                time.sleep(self.__color[t])
                print('\r', end='')


a = TrafficLight()
a.running()
