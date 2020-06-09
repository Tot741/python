class Warehouse:
    all_equip = {}
    temp_quant = 0

    def __str__(self):
        return f'Остаток на складе {self.store_name}:\n{self.all_equip}'

    @classmethod
    def acceptance(cls, name, quantity):
        if cls.all_equip:
            count = 0
            for key in cls.all_equip:
                if key == name:
                    temp_quant = cls.all_equip.get(str(name)) + quantity
                    cls.all_equip.update({key: temp_quant})
                    break
                else:
                    count += 1
            cls.all_equip.update({name: quantity}) if count == len(cls.all_equip) else count

        else:
            cls.all_equip.update({name: quantity})
        print(f'На склад поступил {name} в количестве - {quantity}')

    @classmethod
    def delivery(cls, name, quantity, department):
        temp_key = name
        temp_value = cls.all_equip.pop(temp_key)
        temp_value -= quantity
        if temp_value < 0:
            print(
                f'Вы запросили {name}, количество - {quantity}. На складе нет запрашиваемого количества! В наличии - {temp_value + quantity}')
            cls.all_equip.update({name: quantity})
        else:
            cls.all_equip.update({name: temp_value})
            print(f'{name} выдан со склада в отдел - {department}, количество - {quantity}')


class Office_equip():

    def __init__(self, name, quantity, paper='A4'):
        self.name = name
        self.quantity = quantity
        self.paper = paper

    def __str__(self):
        return f'{self.name}, количество - {self.quantity}, формат бумаги - {self.paper}'

    @staticmethod
    def to_warehouse(*equipments):
        try:
            for equip in equipments:
                Warehouse.acceptance(equip.name, equip.quantity)
        except TypeError:
            print('Количество должно быть указано в виде целого числа')

    @staticmethod
    def from_warehouse(department, *equipments):
        try:
            for equip in equipments:
                Warehouse.delivery(equip.name, equip.quantity, department)
        except TypeError:
            print('Количество должно быть указано в виде целого числа')


class Printer(Office_equip):

    def __init__(self, name, quantity, print_type, paper='A4', color=False):
        super().__init__(name, quantity, paper)
        self.print_type = print_type
        self.color = color


class Scaner(Office_equip):

    def __init__(self, name, quantity, paper='A4'):
        super().__init__(name, quantity, paper)


class Xerox(Office_equip):

    def __init__(self, name, quantity, paper='A4', color=False):
        super().__init__(name, quantity, paper)
        self.color = color


# проверка работы программы

warehouse_1 = Warehouse()
printers_1 = Printer('HP LaserJet', 3, 'Laser')
printers_2 = Printer('Canon BubbleJet', 5, 'Ink', 'A4', True)
printers_3 = Printer('Canon BubbleJet', 6, 'Ink', 'A4', True)
printers_4 = Printer('HP LaserJet', 2, 'Laser')
scaners_1 = Scaner('HP ScanJet', 2)
xerox = Xerox('Xerox', 5)
print(printers_1, '\n', printers_2, '\n', scaners_1, '\n', xerox)
print()
Office_equip.to_warehouse(printers_1, printers_2, scaners_1, xerox)
print()
print(f'Сейчас на складе: {Warehouse.all_equip}')
print()
Office_equip.from_warehouse('IT', printers_3)
Office_equip.from_warehouse('Acc', printers_4)
print()
print(f'Сейчас на складе: {warehouse_1.all_equip}')
print()
Office_equip.to_warehouse(printers_1)
print(f'Сейчас на складе: {warehouse_1.all_equip}')
