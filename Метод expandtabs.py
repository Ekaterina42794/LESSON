''' Метод expandtabs() возвращает копию строки, в которой все символы табуляции ‘\ t’ заменены
пробелами до следующего кратного значения параметра tabsize.
string.expandtabs(tabsize)
        Параметры
expandtabs() Команда в Python  принимает целочисленный аргумент tabsize.'''
#Размер табуляции по умолчанию ‒ 8. Возвращаемое значение Модуль возвращает строку,
# в которой все символы \ t заменяются пробелами до следующего кратного параметра tabsize.
print('"Пример 1: Без аргумента"')

str = 'xyz\t12345\tabc'

# no argument is passed/аргумент не передан
# default tabsize is 8/размер табуляции по умолчанию 8

result = str.expandtabs()

print(result)

'''   Как работает? 
Модуль отслеживает текущую позицию курсора. 
Позиция первого символа ‘\ t’ в приведенной выше программе ‒ 3. 
И размер табуляции равен 8 (если аргумент не передан). 
Символ expandtabs() заменяет ‘\ t’ пробелом до следующей позиции табуляции. 
Позиция ‘\ t’ ‒ 3, а первая позиция табуляции ‒ 8. 
Следовательно, количество пробелов после ‘xyz’ равно 5. 
Следующие позиции табуляции кратны размеру табуляции. 
Следующие позиции табуляции ‒ 16, 24, 32 и так далее. 
Теперь позиция второго символа «\ t» ‒ 13. 
И следующая позиция табуляции ‒ 16. 
Следовательно, после «12345» есть 3 пробела. 
  '''
print('Пример 2: С другим аргументом')

str = "xyz\t12345\tabc"
print('Original String:', str)

# tabsize is set to 2/ размер табуляции установлен на 2
print('Tabsize/ Размер вкладки 2:', str.expandtabs(2))

# tabsize is set to 3/ размер табуляции установлен на 3
print('Tabsize/ Размер вкладки 3:', str.expandtabs(3))

print('Tabsize/ Размер вкладки 4:', str.expandtabs(4))

print('Tabsize/ Размер вкладки 5:', str.expandtabs(5))

print('Tabsize/ Размер вкладки 6:', str.expandtabs(6))

'''   Объяснение 
Размер табуляции по умолчанию ‒ 8. 
Шаг табуляции ‒ 8, 16 и так далее. 
Следовательно, при печати исходной строки после «xyz» ставится 5 пробелов, 
а после «12345» ‒ 3. 
Когда вы устанавливаете размер табуляции на 2. 
Шаг табуляции ‒ 2, 4, 6, 8 и так далее. 
Для «xyz» позиция табуляции равна 4, а для «12345» ‒ 10. 
Следовательно, после «xyz» стоит 1 пробел, а после «12345» ‒ 1 пробел. 
Когда вы устанавливаете размер табуляции на 3. 
Позиции табуляции ‒ 3, 6, 9 и так далее. 
Для «xyz» позиция табуляции равна 6, а для «12345» ‒ 12. 
Следовательно, есть 3 пробела после «xyz» и 1 пробел после «12345». 
Когда вы устанавливаете размер табуляции на 4. 
Позиции табуляции ‒ 4, 8, 12 и так далее. 
Для «xyz» позиция табуляции равна 4, а для «12345» ‒ 12. 
Следовательно, после «xyz» стоит 1 пробел, а после «12345» ‒ 3 пробела. 
Когда вы устанавливаете размер табуляции на 5. Позиции табуляции 5, 10, 15 и так далее. 
Для «xyz» позиция табуляции равна 5, а для «12345» ‒ позиция табуляции 15. 
Следовательно, после «xyz» есть 2 пробела, а после «12345» ‒ 5 пробелов. 
Когда вы устанавливаете размер табуляции на 6. 
Позиции табуляции ‒ 6, 12, 18 и так далее. 
Для «xyz» позиция табуляции равна 6, а для «12345» ‒ 12. 
Следовательно, после «xyz» стоит 3 пробела, а после «12345» ‒ 1 пробел. '''


