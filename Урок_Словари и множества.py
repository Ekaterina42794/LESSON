phone_book = {"Катя": 10000, "Оля": 222222}
print(phone_book)
phone_book['Катя'] = 33333  # изменить значение ключа
print(phone_book)
phone_book['Кира'] = 44444 # новые ключ-значение в конец словаря
print(phone_book)

'''del'''
del phone_book['Оля']  # удаление ключ-значение  словаря
print(phone_book)

'''update'''
phone_book.update({'Kei':2121,'Alex':3232}) # update добавляет и обновляет несколько
                                            # пар ключ-значение
# ??? этот метод принимает другой словарь,который указываем в скобках Scripts ???
print(phone_book)

'''get'''
print(phone_book.get('Kei'))     #выводит значение ключа
print(phone_book.get('Denis'))   # None если нет такого ключа
print(phone_book.get('Denis',"такого ключа нет")) # или запись

'''pop''' # извлекает ключ-значение
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

