food=["яблоки","кокос","банан","ананас","12","100"]# СПИСОК
print(type(food))
'''тип список list '''

tuple = 1,2,3,4,'мама',100     # КОРТЕЖ выводит (1, 2.3, 4, 'мама', 100)
print(type(tuple))

print(tuple)
tuple_2 = (1,2,3,4,'мама',100)
print(tuple_2)
print(type(tuple))
'''тип КОРТЕЖ  <class 'tuple'>'''

print(tuple[0])
print(tuple[2])
print(tuple[4])
'''tuple[0]=200    #неизменяется
print(tuple)'''
tuple = 1,2,3,4,'мама',100
print(type(tuple))
list = [1,2,3,4,'мама',100]
print(type(list))
print(tuple.__sizeof__())
print(list.__sizeof__())

tuple = [1,2,3,4],'мама',100  # КОРТЕЖ НЕИЗМЕНЯЕТСЯ, НО СПИСОК ВНУТРИ МОЖНО ИЗЕНИТЬ
print(tuple)
tuple[0][0]=55  #ИЗМЕНИМ 1ый пункт списка с 1 на 55
print(tuple)

tuple = ([1,2,3,4],'мама',100) + (1,2) # сложение кортежей
tuple[0][0]=55  #ИЗМЕНИМ 1ый пункт списка с 1 на 55
print(tuple)
tuple = (1,1,3,3)*3 #умножение кортежей
print(tuple)
tuple = 3*(1,1,3,3) #умножение кортежей
print(tuple)



