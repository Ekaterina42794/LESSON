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
