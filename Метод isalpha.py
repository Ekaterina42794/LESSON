'''Метод isalpha() возвращает True, если все символы в строке являются алфавитными.
Если нет, возвращается False.
Синтаксис: string.isalpha()
Параметры
Метод isalpha() в Python не принимает никаких параметров.
Возвращаемое значение Модуль возвращает:
Истинно, если все символы в строке являются алфавитными (могут быть как строчными, так и прописными).
Неверно, если хотя бы один символ не является алфавитом.
  '''
print(' Пример 1: Как работает? Метод isalpha() возвращает True, если все символы в строке'
      ' являются АЛФАВИТНЫМИ. Если нет, возвращается False.')

name = "Monica"
print('"Monica"',name.isalpha())

# contains whitespace
name = "Monica Geller"
print('"Monica Geller"',name.isalpha())

# contains number
name = "Mo3nicaGell22er"
print('"Mo3nicaGell22er"',name.isalpha())
print("______________")
print("ПРИМЕР")
name = "098Mon916ler"

if name.isalpha() == True:
    print(name, '- "Все символы являются алфавитами./All characters are alphabets"')
else:
    print(name, '- "Не все символы являются алфавитами./All characters are not alphabets." ')

name = "Monller"

if name.isalpha() == True:
    print(name, '- "Все символы являются алфавитами./All characters are alphabets"')
else:
    print(name, '- "Не все символы являются алфавитами./All characters are not alphabets." ')

name = "Monica Geller"

if name.isalpha() == True:
    print(name, '- "Все символы являются алфавитами./All characters are alphabets"')
else:
    print(name, '- "Не все символы являются алфавитами./All characters are not alphabets." ')
#
