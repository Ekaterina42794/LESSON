'''  Метод rfind() возвращает наивысший индекс подстроки (если найден).
Если не найден, возвращается -1.
Синтаксис: str.rfind(sub[, start[, end]] )

Параметры
Метод rfind() в Python принимает не более трех параметров:
sub ‒ это подстрока, которую нужно искать в строке str.
start и end (необязательно) ‒ поиск подстроки выполняется в str [start: end].
Возвращаемое значение Метод возвращает целочисленное значение:
Если подстрока существует внутри строки, он возвращает наивысший индекс, в котором найдена подстрока.
 Если подстроки не существует внутри строки, возвращается -1.'''
print('*** "Пример 1: Без начального и конечного аргументов"')
quote = 'Let it be, let it be, let it be'

result = quote.rfind('let it')
print("Substring/ Подстрока 'let it':", result)

result = quote.rfind('small')
print("Substring/ Подстрока 'small/маленький':", result)

result = quote.rfind('be,')
if  (result != -1):
  print("Highest index where 'be,' occurs:/Самый высокий индекс, где встречается «be»:", result)
else:
  print("Doesn't contain substring/Не содержит подстроку")
#

print('*** "Пример 2: С начальным и конечным аргументами"')
quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.rfind('things', 10))

# Substring is searched in ' small things with great love'
print(quote.rfind('t', 2))

# Substring is searched in 'hings with great lov'
print(quote.rfind('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.rfind('th', 6, 20))
print('________Метод find()_____________________')
'''Метод find() возвращает индекс первого вхождения подстроки (если найден). 
Если не найден, возвращается -1. 
Синтаксис метода: str.find(sub[, start[, end]] )

Параметры 
Метод find() в Python принимает максимум три параметра: 
sub ‒ это подстрока, которую нужно искать в строке str. 
start и end (необязательно) ‒ диапазон str [start: end], в котором ищется подстрока. 
Возвращаемое значение 
Метод возвращает целочисленное значение: 
Если подстрока существует внутри строки, он возвращает индекс первого появления подстроки.
Если подстроки не существует внутри строки, возвращается -1. 
'''
print('*** "Пример find(): Без начального и конечного аргументов"')
quote = 'Let it be, let it be, let it be'

# first occurance of 'let it'(case sensitive)
result = quote.find('let it')
print("Substring 'let it':", result)

# find returns -1 if substring not found
result = quote.find('small')
print("Substring 'small ' / Подстрока маленькая:", result)

# How to use find()
if (quote.find('be,') != -1):
    print("Contains substring /Содержит подстроку 'be,'")
else:
    print("Doesn't contain substring/ Не содержит подстроку")



print('*** "Пример с аргументами start и end"')

quote = 'Do small things with great love'

# Substring is searched in 'hings with great love'
print(quote.find('small things', 10))

# Substring is searched in ' small things with great love'
print(quote.find('small things', 2))

# Substring is searched in 'hings with great lov'
print(quote.find('o small ', 10, -1))

# Substring is searched in 'll things with'
print(quote.find('things ', 6, 20))