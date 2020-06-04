from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def pants(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def coat(self):
        return round(self.size / 6.5 + 0.5, 2)

    def pants(self):
        pass


class Pants(Clothes):
    def __init__(self, height):
        self.height = height

    def coat(self):
        pass

    @property
    def pants(self):
        return round(2 * self.height + 0.3, 2)


a = Coat(40)
print(a.coat)
b = Pants(115)
print(b.pants)
