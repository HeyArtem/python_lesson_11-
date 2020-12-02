'''
Домашнее задание  по главе 11
Здесь находится класс, на который буду писать магические методы
'''


class Room(): # Простая модель комнаты

    '''
    Метод 1  __init__ 
    отвечает за инициализацию
    '''

    def __init__(self, name, length, width):
        '''
         Инициализируем атрибуты
         Длина, Ширина
        '''
        print('    Старт метод Метод 1 __init__.')
        self.length = length
        self.width = width
        self.name = name

    def __str__(self):
        '''
        Метод 2 __str__
        ОТвечает за отображение объекта,
        т.е. если к нему применить print
        '''
        return f"Помещение: {self.name} "

    def __repr__(self):
        '''
        Метод 3 __repr__ОТвечает за то,
        как он будет оттображаться в системе,
        т.е. как его будут видеть разработчики.
        '''
        return f" Объект имя: {self.name}"

    def __add__(self, other_length):
        '''
        Метод 4 __add__
        Отвечает за операцию '+'
        Предположим после перепланировки параметр
        lenght (длина) увеличится.
        '''
        if isinstance(other_length, (int, float)):
            return self.length + other_length

    def __radd__(self, other):
        '''
        Метод 5 __radd__
        Как и метод __add__ отвечает за сложение,
        но в случаях, когда главный объект находится
        СПРАВА
        '''
        if isinstance(other, (int, float)):
            return self + other


    def __eq__(self, other):
        '''
        Метод 6 __eq__
        Отвечает за сравнение чисел.
        В моем примере, метод сравнивает длину и ширину двух помещений (площадь)
        (экземпляров класса Room) и выдает:
        True-> если величины равны
        False-> если величины отличаются
        '''
        return isinstance(other, Room) and \
               self.length == other.length and self.width == other.width


    def __bool__(self):
        '''
        Метод 7  __bool__
        Если хотя бы один параметр в габаритах комнаты
        будет равен ноль (помещение не реальное), метод выведет False
        '''
        return (self.length != 0 and self.width != 0)

    def __mul__(self):
        ''''
        Метод 8 __mul__ Умножение
        Я считаю площадь помещения
        перемножая length(длину) & width (ширину)
        '''
        return (self.length * self.width)


    def __sub__(self, other):
        ''''
        Метод 9 __sub__ Вычитание
        Здесь считаю разницу в площадях
        между двумя помещениями
        '''
        return f"Метод 9 __sub__ Разница площадей у помещений: {abs((self.length * self.width) - (other.length * other.width))} кв.м"


    def __format__(self):
        ''''
        Метод 10 форматное представление
        '''
        return f"Метод 10. Помещение: {self.name}, Длина:{self.length}м. Ширина:{self.width}м. Общая площадь:{self.length*self.width}кв.м"





if __name__ == '__main__':
    kitchen_room = Room('Kухня', 1, 2)
    kitchen_room_2 = Room('Кухня_2', 10, 2)

    print(kitchen_room.__sub__(kitchen_room_2))

    print(kitchen_room.__format__())







