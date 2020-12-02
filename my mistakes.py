''''
Эльдар здравствуйте, прошу помочь, мне разобраться, пока
я реализовывал магические методы что то не пошло

Изначаьлно, я задумал работать с классом, который принимал бы 4 аргумента
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



    def __sub__(self, other):
        ''''
        Метод 9 __sub__ Вычитание
        Здесь считаю разницу в площадях
        между двумя помещениями
        '''
        # return f"Метод 9 __sub__ Разница площадей у {self}& {other} \составляет:{abs((self.length * self.width) - (other.length * other.width))} кв.м."
        '''
        Если оставить первый return(в строке есть {self}& {other}), то он 
        и не закоментированный метод 10(__format__) будут выдавать ошибку.
        Поэтому на контрольной работе я прописал, как return нижний
        Если закоментировать __format__, то будет работать любой из return
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
