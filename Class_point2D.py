''''
Лекция 11.1
Магические методы класса

!!! Почему так велется лекция, почему преподователь не гтовится заранее, а на средине лекции
меняеются начальные условия и потом идут исправления по всему коду


Как вот так... преподователь что то делает делает а потом говорит видимо не получается... ПОчему?
'''



# Часть 1 - т.е для лекции 11.1
class Point2D():

    # Часть 1
    def __init__(self, x, y):
        self.coord = [x, y]


    def __str__(self):
        '''' ПРи вызове Print, выведет сторочное представлене, а не номер ячейки '''
        return f'Point: ({self.coord[0]}, {self.coord[1]})'

    def __del__(self):
        '''' Метод для удаления параметров объекта '''
        del self.coord

    def __getitem__(self, key):
        return self.coord[key]

    def __len__(self):
        '''' Вывкдкт длину, но не совсем корректно, т.к. для округления приенил str'''
        return int((self.coord[0]**2 + self.coord[1]**2)**0.5)

    def distance(self):
        '''' Аналог len'''
        return (self.coord[0]**2 + self.coord[1]**2)**0.5

    # Часть 2---------------------------------------------

    def __eq__(self, other):
        ''''Напишкем магич.метод котор будет работать при сравнении'''
        return (self.coord[0] == other.coord[0]) & (self.coord[1]== other.coord[1])

    def __lt__(self, other):
        ''''
        метод сравнения, на уроке не не скажут,что этот метод подразузомивает,
        что левая част неравенства, должна быть меньше правой, в этом случае результат True.
        Есть противополождые методы
        '''
        return (self.distance() < other.distance())

    def __add__(self, other):
        '''' if isinstance(other) отвечает за тип объекта'''
        if isinstance(other, Point2D): # это мы дописыввем, что бы можно было выполнить point1+1
            return Point2D(self.coord[0] + other.coord[0], self.coord[1] + other.coord[1])
        if isinstance(other, int):
            return Point2D(self.coord[0] + other, self.coord[1] + other)

    def __float__(self): # Point2D -> float
        return self.distance()





    # Часть 3-----------------------------------------------
    def __getstate__(self):
        ''''
        Этот магич метод, при сериализации сохранит некоторую
        информацию об объекте
        '''
        return self.coord

    def __setstate__(self, state):
        ''''
        Метод передаст состояние и объекта и после
        этого будет произведена сериализация
        '''
        self.coord = state




    # Часть 4 -----Статические методы и методы класса------------
    '''' Статический метод '''
    @staticmethod  # забронированно слово-декоратор
    def stat_method_ex(x, y):  # это статическая функция данного класса
        if(x**2 + y**2)**0.5 > 1:
            return 1
        return 0

    ''' Метод класса '''
    @classmethod
    def class_method_ex(cls):
        ''' Сделаем что бы возвращался лист из объектов класса '''
        point_list = []
        for i in range(10):
            point_list.append(cls(i, i + 1))
        return point_list
    ''''
    Стат методы и методы класса исполбзуются реже, чем методы
    класса.
    
    На вход стат методу подаются некоторые парамтры и не подаются не объекты не классы
    Методы класса обычно используют для генерации каких то спец. объектов
    На вход подаётся сам класс'''















if __name__ == '__main__':
    # point1 = Point2D(1,1)
    # print('Работа метода __str__: ',point1)
    # # del point1 # закоментил,т.к дальше print не будет работать
    # str1 = 'volvo'
    # list_test = [1,2,3,4]
    # print('Работа метода __len__ (в 3-ем Len):',len(str1), len(list_test), len(point1))
    # print('Метод dictance:',point1.distance())
    #
    # for item in str1:
    #     print('Проэтирировали volvo:',item)
    #
    # for item in list_test:
    #     print('Проэтирировали list_test:',item)
    #
    # print('Вычислим, находятся ли точки в диапазоне:\n',2 in point1, 1 in point1) # это мы тестим getitem
    #
    # for coord in point1:
    #     print(coord)



# Предыдущее закоментил, т.к. дальше Стат метод и метод класса

    list_ = Point2D.class_method_ex()
    ''' т.к. это метод класса, то он вызывается через класс точка и данный метод'''
    print(' не красиво, str здесь не работатет:',list_)
    '''' print(list_) - выведет некрасиво'''
    for i in range(10):
        '''' Запринтим каждый элемент листа'''
        print(list_[i])

    print(Point2D.stat_method_ex(1, 2))
    ''''
    Работаем со стат методом. 
    У вектора (1, 2) расстояние > 1
    поэтому должен вернуть 1
    '''