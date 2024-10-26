
print('<< Словари и множества >>')
phone_book = {"Катя": 10000, "Оля": 222222}
print(phone_book)
phone_book['Катя'] = 33333  # изменить значение ключа
print(phone_book)
phone_book['Кира'] = 44444 # новые ключ-значение в конец словаря
print(phone_book)

'''del'''
print('<< del >>')
del phone_book['Оля']  # удаление ключ-значение  словаря
print(phone_book)

'''update'''
print('<< update >>')
phone_book.update({'Kei':2121,'Alex':3232}) # update добавляет и обновляет несколько
                                            # пар ключ-значение
# ??? этот метод принимает другой словарь,который указываем в скобках Scripts ???
print(phone_book)

'''get'''
print('<< get >>')
print(phone_book.get('Kei'))     #выводит значение ключа
print(phone_book.get('Denis'))   # None если нет такого ключа
print(phone_book.get('Denis',"такого ключа нет")) # или запись

'''pop''' # извлекает ключ-значение
print('<< pop >>')
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
print('<< keys >>')
print(phone_book)
print(phone_book.keys()) # dict_keys(['Кира', 'Kei', 'Alex'])

''' values ''' # вывод списка значений словаря
print('<< values >>')
print(phone_book.values()) # dict_values([44444, 2121, 3232])

'''метод items''' # вывод пар ключ-значение
print('<< items >>')
print(phone_book.items())  #dict_items([('Кира', 44444), ('Kei', 2121), ('Alex', 3232)])

# ??? большая часть данных в веб-разработке это словари JSON ???