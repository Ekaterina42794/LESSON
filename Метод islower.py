'''Метод islower() возвращает True, если все алфавиты в строке являются строчными.
Если строка содержит хотя бы один алфавит в верхнем регистре, возвращается значение False.

Синтаксис: string.islower()
'''
''' Метод islower() в Python не принимает никаких параметров. 
Возвращаемое значение Метод возвращает: 
True, если все алфавиты, существующие в строке, являются строчными. 
False, если строка содержит хотя бы один алфавит в верхнем регистре.'''

print('Пример 1: Возвращаемое значение' )
#
s = 'this is good'
print(s.islower())

s = 'th!s is a1so g00d'
print(s.islower())

s = 'this is Not good'
print(s.islower())
'''Пример 2: Как использовать в программе?'''
print('Пример 2: Как использовать в программе?')

s = 'this is good'
if s.islower() == True:
    print('Does not contain uppercase letter./ Не содержит заглавных букв. ')
else:
    print('Contains uppercase letter. Содержит заглавную букву.')
#_____________
s = 'this is Good'
if s.islower() == True:
    print('Does not contain uppercase letter. / Не содержит заглавных букв.')
else:
    print('Contains uppercase letter. Содержит заглавную букву.')