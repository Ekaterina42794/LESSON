''' Метод isidentifier() возвращает True, если строка является допустимым идентификатором в Python.
Если нет, возвращается False.    Источник: https://pythonstart.ru/string/isidentifier-python
 Синтаксис:  string.isidentifier()'''
#
'''Параметры 
isidentifier() в Python не принимает никаких параметров. 
 Метод возвращает: 
True, если строка является допустимым идентификатором. 
False, если строка не является недопустимым идентификатором. 
'''
print('"Пример 1: Как работает isidentifier()?"  ',
      ' Метод возвращает:',
      'Истинно, если строка является допустимым идентификатором. ',
      'False, если строка не является недопустимым идентификатором."',sep='\n')

str = 'Python'
print("'Python'", str.isidentifier())

str = "'Py thon'"
print(str,str.isidentifier())

str = '22Python'
print("'22Python'", str.isidentifier())

str = "' '"
print( "' '", str.isidentifier())

print('"Пример 2."')
str = '"root33"'
if str.isidentifier() == True:
    print(str, 'является действительным идентификатором./is a valid identifier.')
else:
    print(str, 'НЕ является допустимым идентификатором./ is not a valid identifier.')

str = '"33root"'
if str.isidentifier() == True:
    print(str, 'является действительным идентификатором./is a valid identifier.')
else:
    print(str, 'НЕ является допустимым идентификатором./ is not a valid identifier.')

str = '"root 33"'
if str.isidentifier() == True:
    print(str, 'является действительным идентификатором./is a valid identifier.')
else:
    print(str, 'НЕ является допустимым идентификатором./ is not a valid identifier.')