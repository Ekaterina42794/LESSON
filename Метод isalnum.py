'''
Метод isalnum() возвращает True, если все символы в строке являются буквенно-цифровыми (либо алфавитами, либо цифрами).
 Если нет, возвращается False.

 Синтаксис:
 '''

'''Параметры 
Метод в Python не принимает никаких параметров. 
Возвращаемое значение isalnum() в Python возвращает: Истинно, если все символы в строке буквенно-цифровые
 Неверно, если хотя бы один символ не является буквенно-цифровым. '''
#
'''Пример 1: Как работает?'''
name = "M234onica"
print(name.isalnum())

# contains whitespace
name = "M3onica Gell22er "
print(name.isalnum())

name = "Mo3nicaGell22er"
print(name.isalnum())

name = "133"
print(name.isalnum())
#____________________________________________________
'''  Пример 2: Работа isalnum() '''

name = "M0n1caG3ll3r"

if name.isalnum() == True:
   print("All characters of string (name) are alphanumeric./Все символы строки (имени) являются буквенно-цифровыми.")
else:
    print("All characters are not alphanumeric./ Не все символы являются буквенно-цифровыми")

name1 = "a 1 + * / , . "

if name1.isalnum() == True:
   print("All characters of string (name) are alphanumeric./Все символы строки (имени) являются буквенно-цифровыми.")
else:
    print("All characters are not alphanumeric./ Не все символы являются буквенно-цифровыми")

'''     '''