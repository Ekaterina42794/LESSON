print('             << СЛОВАРИ  >>')
phone_book = {"Катя": 10000, "Оля": 222222}
print(phone_book)
phone_book['Катя'] = 33333  # изменить значение ключа
print(phone_book)
phone_book['Кира'] = 44444 # новые ключ-значение в конец словаря
print(phone_book)

'''del'''
print('         << del >>')
print(phone_book)
del phone_book['Оля']  # удаление ключ-значение  словаря
print(phone_book)

'''update'''
print('         << update >>')
print(phone_book)
phone_book.update({'Kei':2121,'Alex':3232}) # update добавляет и обновляет несколько
                                            # пар ключ-значение
# ??? этот метод принимает другой словарь,который указываем в скобках Scripts ???
print(phone_book)

'''get'''
print('         << get >>')
print(phone_book)
print(phone_book.get('Kei'))     #выводит значение ключа
print(phone_book.get('Denis'))   # None если нет такого ключа
print(phone_book.get('Denis',"такого ключа нет")) # или запись

'''pop''' # извлекает ключ-значение
print('         << pop >>')
print(phone_book)
'''phone_book.pop('Катя')'''  # удаляет ключ
a = phone_book.pop('Катя')    # ,но можно сохранить его значение в переменной
print("'Катя'удалили, значение сохранили в переменную a =",a)
print(phone_book)

# со списками по индексу
list_=[1,2,3]
list_.pop(0)
print(list_)
list_2=[4,5,6,7,8]
print(list_2)
b=list_2.pop(1)
print(list_2)
print(b)
print(list_2.pop(1))
print(list_2)

'''keys''' #вывод (списка)коллекции ключей
print('         << keys >>')
print(phone_book)
print(phone_book.keys()) # dict_keys(['Кира', 'Kei', 'Alex'])

''' values ''' # вывод списка значений словаря
print('         << values >>')
print(phone_book)
print(phone_book.values()) # dict_values([44444, 2121, 3232])

'''метод items''' # вывод пар ключ-значение
print('         << items >>')
print(phone_book)
print(phone_book.items())  #dict_items([('Кира', 44444), ('Kei', 2121), ('Alex', 3232)])

# ??? большая часть данных в веб-разработке это словари JSON ???

'''                  <<МНОЖЕСТВА>> '''
print("             <<  МНОЖЕСТВА >>")
# тоже коллекция, как и словарь, но хранит только УНИКАЛЬНЫЕ значения
set_A = {1, 2, 1, 3, 2, 4, 5, 1, 2}
print(set_A)  # {1, 2, 3, 4, 5}
set_A = {1, 5, 1, 2, 1, 3, 4, "STRING", True, (1, 2, 3)} # {1, 2, 3, 4, 5, 'STRING', (1, 2, 3)}
print(set_A, "множество")
LIST_ = [1, 1, 4, 1, 2, 2, 3, 2, ]
print(LIST_, "список")
print(set(LIST_), "список переведенный в множество") # {1, 2, 3, 4}
"               <<  метод discard >>"
print("          <<  метод discard >>")
list_ = [1, 1, 2, 2, 3, 3]
print(list_, " наш список ")
list_ = set(list_)
print(list_, "список переведенный в множество")
print(list_, "список ")
print(list_.discard(2), "??????(discard удаляет элемент из множества, которое было списком)")
print(list_, " список после discard(2) ")  # {1, 3}
# discard не выводит ошибку, если нет такого элемента
print(list_.discard(5), "(???? discard не выводит ошибку, если нет такого элемента)")
"               <<  метод remove >>"
print("          <<  метод remove >>")
list_ = [1, 1, 2, 2, 3, 3]
print(list_, " наш список ")
list_ = set(list_)
print(list_.remove(2),"(???? remove не выводит ошибку, если нет такого элемента)")
'''  ??????????????   '''



