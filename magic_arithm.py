from Class_point2D import Point2D

''''
Лекция 11.2

В Class_point2D записал часть 2 - имеется ввиду, что в предыдущем коде будем что то дописывать под
эту главу

В очередной раз, преподователь не подготовился и сидит гадает, что же нужно писать в параметрах метода
'''

if __name__ == '__main__':
    point1 = Point2D(1, 1)
    point2 = Point2D(1, 2)

    print('метод __eq__:', point1 == point2) # пока не появился метод __eq__, был результат False

    print('работа метода __lt__:', point1 < point2) # работа метода __lt__

    print('Метод __add__:', point1 + point2)

    print('после написания:', point1+1) # будет корректно работать, если будет isinstance(other, int)

    print(' метод __float__, мы прописали, что бы он выводил distance:\n', float(point1))


