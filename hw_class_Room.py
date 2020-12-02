'''
Домашнее задание  по главе 11
Здесь находится класс, на который буду писать магические методы
'''


class Room(): # Простая модель комнаты

    '''
    Метод 1  __init__ 
    отвечает за инициализацию
    '''

    def __init__(self, name, length, width, height):
        '''
         Инициализируем атрибуты
         Длина, Ширина, Высота
        '''
        print('    Старт метод Метод 1 __init__.')
        self.length = length
        self.width = width
        self.height = height
        self.name = name

    def __str__(self):
        '''
        Метод 2 __str__
        ОТвечает за отображение объекта,
        т.е. если к нему применить print
        '''

        # print('    Старт метод Метод 2 __str__.')
        return f"Помещение:{self.name} "

    def __repr__(self):
        '''
        Метод 3 __repr__ОТвечает за то,
        как он будет оттображаться в системе,
        т.е. как его будут видеть разработчики.
        '''

        # print('    Старт метод Метод 3 __repr__.')
        return f" Объект имя: {self.name}"

    def __add__(self, other_length):
        '''
        Метод 4 __add__
        Отвечает за операцию '+'
        Предположим после перепланировки параметр
        lenght (длина) увеличится.
        '''

        # print('    Старт метод Метод 4 __add__. Увеличиваем длину')
        if isinstance(other_length, (int, float)):
            return self.length + other_length

    def __radd__(self, other):
        '''
        Метод 5 __radd__
        Как и метод __add__ отвечает за сложение,
        но в случаях, когда главный объект находится
        СПРАВА
        '''

        # print('    Старт метод Метод 5 __radd__. Увеличиваем длину, объект СПРАВА')
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

        # print('    Старт метод Метод 6 __eq__.')
        return isinstance(other, Room) and \
               self.length == other.length and self.width == other.width

    def __bool__(self):
        '''
        Метод 7  __bool__
        Если хотя бы один параметр в габаритах комнаты
        будет равен ноль (помещение не реальное), метод выведет False
        '''
        # print('    Старт метод Метод 7 __bool__.')
        return (self.length != 0 and self.width != 0 and self.height != 0)




    # !?!?!Эльдар, не могу составить код, что бы прибавлялись все три габарита в одной строке
    # def __add__(self, other_length, other_width, other_height):
    #     '''
    #     Метод 4 __add__
    #     Предположим после перепланировки какой то из
    #     параметров (габаритов) комнаты увеличился.
    #     '''
    #     print('    Старт метод Метод 4 __add__')
    #     if isinstance(other, (int, float)):
    #         return self.length + other_length, self.width + other_width,  self.height + other_height




    # def __len__(self):  # что то пока не так
    #     '''
    #     Метод 7  __len__
    #
    #     '''
    #     print('    Старт метод Метод 7 __len__.')
    #     # res = float(abs(self.length - self.width))
    #     # print(res)
    #     # if res > 0 or res < 0:
    #     #     return 'Помещение прямоугольное'
    #     # return 'Помещение квадратное'
    #     return len(self.name)




    def __dir__(self):
        # print('  НЕ ИДЕТ  Старт метод Метод 9 __dir__.')
        # return self.name
        return

    # def __new__(cls, *args, **kwargs):
    #     return




if __name__ == '__main__':
    kitchen_room = Room('кухня', 20, 3, 3)








    # print('lenLen', len.kitchen_room)



    #print(bool(kitchen_room))




    print(kitchen_room.__dir__())





    # new_lenght = kitchen_room.length+10
    # print(new_lenght)
    # new_lenght_2 = kitchen_room+10
