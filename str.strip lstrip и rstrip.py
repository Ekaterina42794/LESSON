''' Метод str.strip() lstrip() и rstrip() в Python'''
#
'''  Метод strip() возвращает копию строки, удаляя как начальные, 
так и конечные символы (в зависимости от переданного строкового аргумента). 
Метод удаляет символы как слева, так и справа в зависимости от аргумента
 (строка, определяющая набор символов, которые необходимо удалить). 
 string.strip([chars])
Источник: https://pythonstart.ru/string/strip-python

Параметры 
chars (необязательно) ‒ строка, определяющая набор символов, которые нужно удалить из левой и правой части строки. 
Если аргумент chars не указан, все начальные и конечные пробелы удаляются из строки. 
Возвращаемое значение
 Команда возвращает копию строки с удаленными начальными и конечными символами. 
 Работа метода strip() 
 Когда символ строки слева не совпадает со всеми символами в аргументе chars, он перестает удалять ведущие символы. 
 Точно так же, когда символ строки справа не совпадает со всеми символами в аргументе chars, 
 он перестает удалять завершающие символы. 
 Пример

'''
print(' "Пример" ')
string = '  xoxo love xoxo   '

# Начальные и конечные пробелы удаляются/Leading and trailing whitespaces are removed
print(string.strip())

# Все символы <whitespace>,x,o,e слева и справа строки удаляются/
# All <whitespace>,x,o,e characters in the left and right of string are removed
print(string.strip(' xoe'))

# Аргумент не содержит пробела
#  Никакие символы не удаляются.
# Argument doesn't contain space No characters are removed.
print(string.strip('stx'))

string = 'android is awesome'
print(string.strip('an'))

''' Здесь мы видим, что первое выражение string.strip() без каких-либо аргументов удалило пробелы 
слева и справа от строки. 
string.strip (‘xoe’) удалил все пробелы, x, o и e, ведущие или завершающие строку. 
Поскольку строка имеет пробелы в начале и в конце, выражение string.strip (‘stx’) не меняет строку. 
X не удаляется, так как он находится в середине строки (пробелы ведут и следуют за строкой). 
string.strip (‘an’) удалил начало строки.'''
#
''' Метод lstrip() возвращает копию строки с удаленными ведущими символами 
(на основе переданного строкового аргумента). Команда удаляет символы слева на основе аргумента 
(строка, определяющая набор символов, которые необходимо удалить). 
Синтаксис: string.lstrip([chars])
'''
print('" Метод lstrip() возвращает копию строки с удаленными ведущими символами ',
      '(на основе переданного строкового аргумента). Команда удаляет символы слева на основе аргумента ',
      '(строка, определяющая набор символов, которые необходимо удалить)." ',sep='\n')
'''     Параметры 
lstrip() chars (необязательно) ‒ строка, определяющая набор символов, которые нужно удалить. 
Если аргумент chars не указан, все начальные пробелы удаляются из строки. 
lstrip() возвращает копию строки с удаленными начальными символами. 
Все комбинации символов в аргументе chars удаляются из левой части строки до первого несоответствия.'''

print("Пример")
random_string = '   this is good '

# Leading whitepsace are removed
print(random_string.lstrip())

# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('sti'))

print(random_string.lstrip('s ti'))

website = 'https://pythonstart.ru/'
print(website.lstrip('htps:/.'))
