class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.color} {self.name} поехала')

    def stop(self):
        print(f'Машина {self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость - {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Ваша скорость {self.speed}. Это больше 60 км/ч. Вы превышаете!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Ваша скорость {self.speed}. Это больше 40 км/ч. Вы превышаете!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police == True:
            print('Это полицейская машина!')


a = Car(60, 'красный', 'BMW', False)
a.go()
a.stop()
a.turn('влево')
a.show_speed()
b = TownCar(70, 'белый', 'Skoda', False)
b.go()
b.stop()
b.turn('вправо')
print(f'Текущая скорость - {b.speed}')
b.show_speed()
c = SportCar(150, 'красный', 'Porche', False)
c.go()
c.stop()
c.turn('назад')
c.show_speed()
d = WorkCar(60, 'белый', 'Skoda', False)
d.go()
d.stop()
d.turn('влево')
d.show_speed()
e = PoliceCar(60, 'синий', 'Chevrolet', True)
e.go()
e.stop()
e.turn('вправо')
e.show_speed()
