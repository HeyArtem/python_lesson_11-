import pickle

from Class_point2D import Point2D
''''
Глава 11.3
Сериализация обьектов

В Class_point2D записал часть 3
'''

point1 = Point2D(1,1)
#     Cериализация
# data = {'1' : (1, 2),
#         '2' : 'volvo',
#         '3' : True,
#         '4' : point1}
# f = open ('data.pkl', 'wb') # wb-режим байтовая запись

f = open ('point.pkl', 'wb') # wb-режим байтовая запись
pickle.dump(point1, f) # начинаем сериализацию

f.close() # закрываем.
'''' После запуска появится фаил -> data.pkl или data.pkl '''


#     ДеCериализация

#f = open ('data.pkl', 'rb') # rb-режим байтовоя чтение
f = open('point.pkl', 'rb')

#data_new = pickle.load(f)
point_new = pickle.load(f)


# print('data_new:', data_new)
# print('Data:', data) # я закоментил процедуру сериализации *начиная с f=open по f.close

print(point1)
print('point_new:', point_new)

f.close() # закрываем.