class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to (self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа нет')
        else:
            for i in range(1,new_floor+1):
                print(i)

    def __len__(self):
        return (self.number_of_floors)

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        if isinstance(other, House) and isinstance(self.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors
        else:
            print('Неверный тип данных или класс')

    def  __lt__(self, other):
        if isinstance(other, House) and isinstance(self.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
        else:
            print('Неверный тип данных или класс')

    def __le__(self, other):
        if isinstance(other, House) and isinstance(self.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
        else:
            print('Неверный тип данных или класс')

    def __gt__(self, other):
        if isinstance(other, House) and isinstance(self.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
        else:
            print('Неверный тип данных или класс')

    def __ge__(self, other):
        if isinstance(other, House) and isinstance(self.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
        else:
            print('Неверный тип данных или класс')

    def __ne__(self, other):
        if isinstance(other, House) and isinstance(self.number_of_floors, int):
            return self.number_of_floors != other.number_of_floors
        else:
            print('Неверный тип данных или класс')

    def __add__(self, value):
        if isinstance(value, int) and isinstance(self.number_of_floors, int):
            self.number_of_floors += value
            return self
        else:
            print('Не тот тип данных')

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__