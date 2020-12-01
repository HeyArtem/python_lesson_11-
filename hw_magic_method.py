'''
Домашнее задание  по главе 11
Магические методы, утиная типизация, статические методы

Реализовать собственный класс с использованием магических методов (не менее 10ти).
Можно использовать собственный класс из вебинара 10.
'''



class Room():
    ''' Простая модель комнаты '''

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

        print('    Старт метод Метод 2 __str__.')
        return f"Помещение:{self.name} "



    def __repr__(self):
        '''
        Метод 3 __repr__ОТвечает за то,
        как он будет оттображаться в системе,
        т.е. как его будут видеть разработчики.
        '''

        print('    Старт метод Метод 3 __repr__.')
        return f" Объект имя: {self.name}"

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

    def __add__(self, other_length):
        '''
        Метод 4 __add__
        Отвечает за операцию '+'
        Предположим после перепланировки параметр
        lenght увеличился.
        '''

        print('    Старт метод Метод 4 __add__. Увеличиваем длину')
        if isinstance(other_length, (int, float)):
            return self.length + other_length

    def __radd__(self, other):
        '''
        Метод 5 __radd__
        Как и метод __add__ отвечает за сложение,
        но в случаях, когда главный объект находится
        СПРАВА
        '''

        print('    Старт метод Метод 5 __radd__. Увеличиваем длину, объект СПРАВА')
        if isinstance(other, (int, float)):
            return self + other

    def __eq__(self, other):
        '''
        Метод 6 __eq__
        Отвечает за сравнение чисел.
        В моем примере, метод сравнивает длину и ширину двух помещений
        (экземпляров класса Room) и выдает:
        True-> если величины равны
        False-> если величины отличаются
        '''

        print('    Старт метод Метод 6 __eq__.')
        return isinstance(other,Room) and \
               self.length == other.length and self.width == other.width

    # def __len__(self):  # что то пока не так
    #     '''
    #     Метод 7  __len__
    #
    #     '''
    #     print('    Старт метод Метод 7 __len__.')
    #     res = float(abs(self.length - self.width))
    #     print(res)
        # if res > 0 or res < 0:
        #     return 'Помещение прямоугольное'
        # return 'Помещение квадратное'







if __name__ == '__main__':
    kitchen_room = Room( 'кухня', 100, 2, 3)
    '''Экземпляр от класса Room '''


    print('Методы __str__ или __repr__ подхватывают друг друга:\n', kitchen_room)


    new_lenght = kitchen_room + 102.6
    print('Новая длина комнаты:', new_lenght, 'метров.')


    new_lenght_on_right = 200 + kitchen_room
    print('New_lenght_on_right=', new_lenght_on_right)

    room = Room('кладовка', 20, 2, 3)
    print('Сравниваем lenght & width: ', kitchen_room == room)

    # print((len(kitchen_room)))


    # new_lenght = kitchen_room.length+10
    # print(new_lenght)
    # new_lenght_2 = kitchen_room+10

