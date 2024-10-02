name="Катя"
print(name)
print("TYPE определяет тип данных в скобках")
print("PRINT для вывода информации")
print("TYPE определяет тип данных в скобках")
print("____числа________")
print("ЧИСЛА бывают целые и дробные, неизменяемый тип данных")
print()
print(5)
print(type (5)) #тип данных Int - INTEGER целое число
print("тип данных Int - INTEGER целое число")
print()
print("+,-,*,**,/,//, %")
print(5+5)
print(5-5)
print(5*5)   # умножение
print(5**3)  # возведение в степень
print(5/5)   # деление
print(14//5) # выводит только целую часть при делении
print(13%5)  # вывод только остатка при делении
print()
print(2.0)   # FLOAT дробные числа
print(type (2.0))
print(2.0+5)
print(type (2.0+5)) # дробное+целое= дробное число
print("______строки________")
# строки
print("Heloo world") #слов нужны кавычки
print(type("Heloo world")) # str - кавычки ' и " string - строка
print('Heloo'+'world') #  + единственная математическая операция для строк
print("Heloo" + 'world')
print("Heloo "+'world .')
# print(" 1 "+1) # разные типы "concatenate str (not "int") to str"
print("1"+"1")   # сложение строк
print(type ("1""1"))
print(1+1)
print(type (1+1)) # сложение целых чисел
print("__  bool - логический тип данных  __")
# true-верно(правда), false-неверно(ложь)
print("True-верно(правда), False-неверно(ложь)")
print(type (True)), print(type (False))
print(5>10)        #ответ в логическом виде
print("(5>10,5<1,5<=5,5>=5,5==5,5!=5)    == равенство, != неравенство")
print(5>10,5<1,5<=5,5>=5,5==5,5!=5)   # == равенство, != неравенство
print(" ")
print("and (и) Верно, только если ВСЕ выражения ВЕРНЫ")
print("or (или) НЕ верно если ВСЕ НЕ верны, верно если хоть что-то верно")
print(5>1 and  5==5 and 5!=5)
print(5>1  and 5==5 and 5!=11)
print(5<1  or 5==5 or 5!=11)
print(5<1  or  5==11) # неверно, только  если ВСЁ неверно
print(5<10 and 5>1 or 5>10) # (T*T)+(T+F)=T+T=T
print(5>10 and 5>1 or 5!=5) # (F*T)+(T+F)=F+T=F
print("__ изменение типа данных__")

print(type(5)), print(type(int("5")))# число и перевод в число
print("__")
print(type("5")), print(type(str(5)))  # строка и перевод в строку