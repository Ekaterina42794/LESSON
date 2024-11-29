'''Встроенные функции в Python

Встроенные функции в Python
На сегодняшнем занятии поговорим про встроенные функции Python.
Если на прошлых занятиях мы учились объявлять собственные функции, вызывать их,
передавать им какие-то значения, то на этом занятии и на следующем будем работать уже с готовыми функциями.
Существует перечень функций, которые встречаются при попытке преобразовать один тип данных к другому:
#int() - целое число
#float() - число с плавающей запятой
#bool() - логические значения
#str() - строки
#list() - список
#tuple() - кортеж
#dict() - словарь
#set() - множество
Запомнить их нетрудно, потому что название функции соответствует названию типа данных.
Данные функции используются часто для того, чтобы привести какой-то тип данных к нужному нам типу.
Например, вспомним с какой функцией мы работали достаточно часто - input(), запрос ввода данных от пользователя.
Когда нам необходимо, чтобы пользователь ввёл именно число, то используется запись такого рода: int(input()).
По сути, запрашивается ввод данных от человека. Всё, что вводит пользователь, изначально
принадлежит к строковому типу данных, а потом всё, что этот человек ввёл приводится к целому числу.
Если нам надо целое число преобразовать в число с плавающей запятой, то воспользуемся инструкцией float().
Когда мы захотим получить из числа допустим или из какой-то строки значение типа True или False,
 то воспользуемся bool(). С ней следует ознакомиться немного подробнее. Допустим, у нас есть какая-то строка(рис.1).
 Если передадим и воспользуемся функцией bool(), то получим True(рис.2).
 Когда передадим пустую строку, получим False.
 При работе с числами любые числа будут давать нам Тrue, за исключением нулей(рис.3).
 То есть данные сведения можно использовать для оформления различных условий.
 Так или иначе, у нас могут быть неявные преобразования и число неявно можем преобразовать в значение True или False.

 Пример. Отсутствие типа будет возвращать нам False.
 При написании None будет False(рис.4).
None — это отсутствие значения. Такое часто бывает, когда мы какой-то параметр передаём и
 выставляем ему значение по умолчанию None. Зарезервировали место,
 зарезервировали имя для определённого параметра,
  но в будущем нам, возможно, пригодится с ним как-то работать.
  Можно создать дополнительное условие, по которому будем определять то, что данный параметр существует или нет.
  Если в программе написать какой-нибудь type=None и сделать какое-нибудь условие,
  например, If tуре и вывести что-то, например “Ок”, то при запуске результата не будет,
   поскольку выполняется неявное преобразование(рис.5).
   Получается переменную tуре проверяем на наличие значения:
   напишем 1 - программа выполнится(рис.6),
   напишем 0 - программа не выполнится. Происходят неявные преобразования.
   Они сокращают нам запись. Но здесь нужно быть внимательным с тем, как вы обозначите это условие.

   В принципе, остальные функции достаточно просто работают.
   Если нам нужен список, мы можем использовать инструкцию list() для формирования списка.
    Воспользуемся точно также интерактивным режимом.
    Единственное, что сюда нужно передавать перебираемые какие-то значения.
     Например, передали строку и на основе этой строки создался список.
     Захотели сделать кортеж, передали строку, получили кортеж с элементами из этой строки(рис.7).
      То есть это всё у нас работает замечательно.

Давайте разберем практический пример и затронем несколько функций, которые раньше не использовали.
Представим, что у нас есть список salary().
Он будет содержать в себе зарплаты сотрудников в определённой компании.
 Допустим, эти зарплаты будут в долларах.
 Они имеют разную величину, потому что сотрудники находятся на разных должностях и имеют разные значения.
 Некоторые зарплаты будут целыми, другие зарплаты будут содержать ещё и центы(рис.8).

 Данный список содержит определённое количество элементов.
 Наша задача написать какую-то гибкую, динамическую программу, которую в будущем можно будет как-то развивать.
 Суть задачи состоит в том, что нам необходимо найти среднюю, максимальную,
  минимальную зарплату в компании. Также необходимо сделать из этого словарь.
  Он будет содержать имя сотрудника и соответствующую зарплату.
В первую очередь займёмся получением количества зарплат.
Чтобы узнать количество элементов в списке, мы можем воспользоваться специальной
функцией len() - в результате возвращает длину передаваемой последовательности.
В эту инструкцию len() передали список с зарплатами (salaty=[2300, 1800.80, 5000, 1234.58, 7500.12])
 и получили значение 5(рис.9).

Чтобы найти какое-то среднее значение, нам нужно всех их просуммировать и разделить на количество элементов.
В этом случае можем воспользоваться циклом for, можем создать какой-то счётчик,
пробежаться по каждому элементу и прибавлять значение этого элемента к нашей переменной.
 В конечном счёте всё-таки получим сумму элементов. Но есть решение гораздо быстрее.
  Воспользуемся функцией sum(), куда передадим список и получим сумму всех элементов.
  Сумма всех зарплат составляет 17835,5, также 5 будем считать, что это количество сотрудников(рис.10).
  Чтобы найти среднее значение, просто разделим сумму на количество сотрудников (sum(salary)/len(salary)).
  При запуске выходит, что средняя зарплата в компании составляет 3567.1(рис.11).

Теперь давайте найдём с вами максимальное и минимальное значение.
Чтобы найти максимальное, будем использовать функцию max().
Она находит максимальный элемент из переданной в неё последовательности.
Напишем, что это максимальная зарплата компании.
Данную строчку копируем, заново вставляем и ставим функцию min().
Также пишем, что это минимальная зарплата компании.
Запускаем, получаем результат: 7500,12 - максимальная зарплата, и 1234,58 - это минимальная зарплата в компании(рис.12).

Представим, что бухгалтеры немного ошиблись, либо же значения после точки много,
то при вычислениях выйдет неприятный результат(рис.13).
Можем от этого избавиться, приведя это в целое число, но всё-таки нас интересует количество центов.
 Оно будет иметь определённое значение.

Чтобы работать со знаками после точки, можем воспользоваться функцией round().
Данная функция принимает два параметра — само число и количество знаков после запятой.
По сути, сейчас мы передали в функцию значение, получившееся в результате деления суммы
на количество элементов и число 2(рис.14).
Смотрим на результат — это средняя зарплата в компании(рис.15).
Два знака после запятой даст нам два, но так как последняя цифра 0, поэтому его не видно.
Тем не менее тут два знака, то есть 3567. и 10 центов. Три знака после запятой даст нам три(рис.16).

Давайте то же самое сделаем и с максимальной зарплатой, и с минимальной. Здесь будет уже видно, как это работает.
Запускаем(рис.17).
Получается, что с помощью функции round() получилось округлить и избавиться от лишних знаков после точки.

Теперь нам нужно создать некий словарик, содержащий в себе имена и зарплаты.
Допустим, у нас есть имена сотрудников: Денис, Антон, Егор, Катя, Женя.
Далее нам нужно как-то их объединить. Здесь подразумевается, что в списке зарплат и в списке
с именами пять значений, и зарплата соответствует определённому имени:
2300 будет соответствовать Денису, Антону - 1800, Егору - 5000, Кате - 1234, Жене - 7500.
Для данной задачи создадим какую-нибудь переменную zipped и воспользуемся функцией zip().
Передадим туда имена и зарплаты. Если мы выведем эту переменную, то получим “zip object at ...”,
то есть эта функция вернула нам объект(рис.18).
С этим объектом можно работать так, как нам необходимо.
Например, воспользуемся функцией list(), получим список(рис.19).
 У нас получилось слияние двух списков:
получили список, в котором элементами являются кортежи со значениями из первого списка и из второго.

Если хотим этот объект привести, например, в словарь, то получим словарь(рис.20)
В нем значениями будут элементы из первого списка и ключами — элементы из второго списка.

Теперь, получается, можно всё это дело обернуть в словарь и доставать зарплаты определенных
сотрудников, обращаясь по ключу.
 Теперь скажем, что это зарплата Дениса, только не из списка names, а уже из zipped.
  Получается 2300 — это зарплата Дениса(рис.21).


'''
# int()  --> int(input())
# float()
# bool()
# str()
# list()
# tuple()
# dict()
# set()
# округлим- round(sum(salary)/len(salary), кол-во знаков после запятой)
# zip(names, salary)#слияние двух списков zip obekt
'''salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary)/len(salary), 2), ' - средняя зарплата в компании')
print(round(max(salary), 2), ' - максимальная зарплата в компании')
print(round(min(salary), 2), ' - минимальная зарплата в компании')

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = dict(zip(names, salary))
print(zipped['Денис'], '- зарплата Дениса')'''

'''Встроенные функции. 1.2

На сегодняшнем занятии продолжаем тему о встроенных функциях, разберём функцию any(), 
функцию аll() и поговорим про интроспекцию.
Начнём с any() и аII(). Представим, что у вас есть список и он содержит какие-то элементы, 
например, True, False, False. Функция any() проверяет объект, его содержимое,
 то есть пробегает по элементам. При условии, что хотя бы один из элементов внутри объекта будет True, 
 функция вернёт нам True, в противном случае вернёт False. 
 Передадим в функцию any() наш объект ‘а’ (наш список) и получим ответ True(рис.1). 
 Если в объекте вместо True написать False, то и в ответ получим False(рис.2).
 
Можно подумать, что это применяется только с True и False, но нет. 
На самом деле есть же ещё и неявные преобразования. 
Если смотреть на числа, например, с точки зрения логических значений,
 то любые числа, кроме 0, будут давать True. 
 Проверяем - получаем ответ True(рис.3). 
 Если будут все нули, то и в ответе получим False(рис.4).
 
Также это применимо к строкам. 
Например, у нас есть строка с содержимым в видео цифры 0(рис.5). 
Можно было бы подумать, что и в ответе получим False, но нет. 
На строки мы смотрим с точки зрения наличия в ней символов. 
Если строка пустая, тогда False(рис.6). 
При наличии в строке хотя бы одного элемента, получим True. 
Так что не стоит забывать о неявных преобразованиях.

Помимо функции any() есть ещё и функция aII(). 
По названию уже понятно, как она работает. 
Когда any() достаточно хотя бы одного элемента True, функции aII() нужны все элементы. 
Если все элементы True получаем True. Если хотя бы один элемент False - получаем False. 
В объекте элементы 1, 1 — True, 0 — False. B ответе получили False(рис.7). 
Заменим 0 на 1, получим True(рис.8).

Данные функции могут помочь вам, например, в каких-то функциях, которые работают 
с определёнными последовательностями и выполняют определённые действия. 
Tо есть вы можете проверить что вернуть в случае, если есть какой-то элемент в вашей последовательности.
Дальше поговорим про интроспекции.


Интроспекция — это способность какого-либо объекта получить информацию об атрибутах и 
методах в процесс выполнения программы. 
К функциям интроспекции относятся такие функции, как dir(). 
Эта функция позволяет получить информацию об атрибутах объекта. 
Передадим туда “а” и получим отсортированный в алфавитном порядке список целой кучи атрибутов(рис.9). 
С двойным подчёркиванием нас сейчас особо не интересуют. 
Пролистав до конца этого списка, увидим уже вполне знакомые для себя методы. 
Например, append() добавляет элемент в конец списка, remove() убирает элемент из списка. 
Это уже вам более знакомо. 
Если также посмотрим для строки, то получим точно такую же информацию и доступные методы.

Что нам может пригодиться? Мы сомневаемся, например, в том, что ‘b’ - это строка. 
Проверить можно с помощью функции type(). В ответе получим класс ‘str’(рис.10). 
Допустим, нам не нужно описание класса. 
Мы хотим сравнить, проверить и получить в ответе, например, True или False. 
Можем использовать функцию isinstance(). 
Она принимает объект для проверки и вторым - это класс, с которым будем сравнивать, то есть b и str. 
При запуске получаем True(рис.11). 
То есть проверили является ли b классом и получили в ответе True. 
В случае написания int вместо str - получим False(рис.12).

Аналогичного результата можно добиться и с функцией type. 
Укажем, что у нас tуре(b) == str. Запускаем, получаем True(рис.13).


Данные методы можно использовать для того, чтобы понять, к какому типу у нас относится тот или иной объект. 
Также представим ситуацию, что мы сомневаемся. 
У нас есть два списка, содержащие по три элемента. При проверке, что ‘a == d’, 
получаем ответ Тrue(рис.14), потому что их содержимое одинаково. 
Но 'а’ не является одним и тем же объектом, как и “d”. Если напишем ‘a is d’, 
то получим False(рис.15), потому что имя ‘a’ и имя ‘d’ ведёт к абсолютно разным объектам.
Чтобы получить информацию об уникальном номере, об ID объекта, то есть его адресе памяти, 
используем соответствующую функцию id(). 
Запускаем. Видим(рис.16), что у нас абсолютно разные адреса, соответственно, эти объекты абсолютно разные. 
 Если будем вносить изменения в одном списке, они не коснутся другого.
 
 При этом нужно быть внимательным, если у нас есть второе имя. 
 Например, добавили переменную ‘с = d’. По сути, просто создали новое имя. 
 Оно будет вести на объект ‘d’, на вот этот самый список.
  При выводе id этой переменной ‘c’, получим тот же самый адрес, что и у переменной ‘d’(рис.17). 
  Вот здесь нужно быть аккуратным. Изменения, которые будем вносить в список ‘c’, они тоже будут касаться списка ‘d’.
   Если их сейчас вывести получим два одинаковых списка(рис.18). 
   Поэтому id() достаточно полезная функция. 
 Можем проверить, ведёт ли это у нас к одному и тому же объекту или нет. 
 ID есть у каждого объекта, даже у обычного числа(рис.19).
 
Существует интересная особенность. 
Видим ID у 2. 
Запускаем ещё раз и видим снова один и тот же ID(рис.20). 
Дело в том то, что ряд чисел у нас уже хранится в памяти, 
но с большими числами всё-таки приходится создавать новое место в памяти под них. 
То есть ID используется для получения информации о том, где объект находится в памяти.
 Если сравним, например, что у нас объект ‘c’ является объектом ‘d’, мы получим True(рис.21).
 
 Давайте рассмотрим еще одну функцию, которая может помочь вам, если вы, допустим,
  забыли или нуждаетесь в помощи. 
 Допустим забыли, как работать со списком. Воспользовались функцией Help(), передали туда список, 
 получили информацию о содержимом данного класса, об атрибутах, методах и краткую документацию, подсказки(рис.22). 
 Также можно получить о каких-то конкретных функциях. 
 Написали print() и видим, что функция рrint() выводит какие-то значения и имеет какие-то атрибуты, 
 их описание(рис.23). Такое достигается с помощью строк документирования. 
 Их можно оставлять, когда вы пишете собственные функции, или в будущем, когда будете писать собственные классы.
 
 Если вы хотите увидеть тот же результат, например, для собственной функции, которую вы создали, 
 то первая строка после объявления функции будет являться строкой документирования, по-другому ещё doc string. 
 Напишем “Эта функция-помощник”, сделаем заглушку(рис.24) и засунем эту функцию Helper() в функцию Help(). 
 Получим ответ: “Эта функция-помощник”(рис.25).
 
 Аналогично работает атрибут __doc__. 
 При использовании метода __doc__ для функции helper(), получим то же самое сообщение, 
 строку документирования: “Эта функция-помощник”(рис.26).
 
 '''
print('bool')
print(bool(0))# False
print(bool(None))#False
#print(bool(a))# имя «a» не определено/ NameError: name 'a' is not defined
print(bool(1))#True
print(bool("a"))#True
#print(bool(0,1))#bool ожидалось не более 1 аргумента, получено 2/ TypeError: bool expected at most 1 argument, got 2

print('list')
print(list('abcd')) #['a', 'b', 'c', 'd'] список
print(tuple('abcd')) # ('a', 'b', 'c', 'd') кортеж

salary = [230540, 108024.899234, 500210, 123458.3434, 700500.122323]
print(len(salary),'значений зарплат;', 'сумма зарплат: ',sum(salary))

print(round(sum(salary)/len(salary), 2), ' - средняя зарплата в компании')
# округлим- round(sum(salary)/len(salary), кол-во знаков после запятой)

print(round(max(salary), 2), ' - максимальная зарплата в компании')
print(round(min(salary), 2), ' - минимальная зарплата в компании')
print('-')
print('список из 2х списков, в котором элементами стали кортежи')
names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = zip(names, salary)#слияние двух списков zip obekt
print(list(zipped))# переводим zip obekt в список в котором элементами стали кортежи
#[('Денис', 2300), ('Антон', 1800.899234), ('Егор', 5000), ('Катя', 1234.583434), ('Женя', 7500.122323)]

print('-')
print('словарь из 2х списков')
names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = zip(names, salary)
print(dict(zipped))
print('-------------------------')
print('ф-ция any - если хотя бы один из элементов True, ф-ция any вернёт True')
a=(True,False,True)
print(any(a))  #True
a=(True,False,False)
print(any(a)) # True
a=(1,None,0)
print(any(a)) #True

a=(False,False,False)
print(any(a)) # False
a=(False,None,0)
print(any(a)) # False
# если хотя бы один из элементов True, ф-ция any вернёт True

print('ф-ция all - только если ВСЕ элементы True, ф-ция all вернёт True')
a=[True,False,1]
print(all(a))  # False
a=(1,'False',0)
print(all(a)) # False
#только если ВСЕ элементы True, ф-ция all вернёт True
a=('False',1,True)
print(all(a)) # True
print('-------')
print('Интроспекция — это способность какого-либо объекта получить информацию об атрибутах и методах в процесс выполнения программы.')
print('dir()-Эта функция позволяет получить информацию об атрибутах объекта. ')

'''Передадим туда “а” и получим отсортированный в алфавитном порядке список целой кучи атрибутов.
Bидим уже вполне знакомые для себя методы.
Например, append() добавляет элемент в конец списка,
 remove() убирает элемент из списка.'''
a = [1, 1, 1]
b = ''
print(dir(a))
print(dir(b))

print('isinstance()')
'''Мы хотим сравнить, проверить и получить в ответе, например, True или False. 
Можем использовать функцию isinstance(). 
Она принимает объект для проверки и вторым - это класс, с которым будем сравнивать, то есть b и str. '''
a = [1, 1, 1]
b = ''
c = True
print(isinstance(a,str)) #False
print(isinstance(a,list))#True
print(isinstance(b,str)) #True
print(isinstance(c,str)) #False
print(isinstance(c,bool)) #True
'''Аналогичного результата можно добиться и с функцией type'''
print(type(c)==bool) #True
'''Данные методы можно использовать для того, чтобы понять, к какому типу у нас относится тот или иной объект.'''
print('функция id() - Чтобы получить информацию об уникальном номере, об ID объекта, то есть его адресе памяти')
a=[1,2,3]
b=[1,2,3]
d=[0,9,8]
c=d
print(a==b) #При проверке, что ‘a == d’, получаем ответ Тrue, потому что их содержимое одинаково.
# но
print(a is b) # получим False, потому что имя ‘a’ и имя ‘d’ ведёт к абсолютно разным объектам

print(id(a)) # id 1880696559808
print(id(b)) # id 1880696845440
# разные адреса.Если будем вносить изменения в одном списке, они не коснутся другого
# но если c=d,то адрес будет один и изменения каснуться d.
print(id(d)) #      2223285167552
print(id(c)) # id d 2223285167552
print(c is d) #Тrue, потому что один адрес
'''ID есть у каждого объекта, даже у обычного числа'''
print(id(5)) # 140727936027192 -32
print(id(4)) # 140727936027160 -32
print(id(3)) # 140727936027128
print(id(256))
# 140727936035224
# 140727936035224
#но уже у 257 id меняется
print(id(257))
# 2403714466160
# 2908673278320
# 1587986628976
# id одинаковый,  но меняется каждый раз в отличии от маленьких чисел
''' 
Существует интересная особенность. 
Видим ID у 2. 
Запускаем ещё раз и видим снова один и тот же ID 
Дело в том то, что ряд чисел у нас уже хранится в памяти, 

но с большими числами всё-таки приходится создавать новое место в памяти под них. 
То есть ID используется для получения информации о том, где объект находится в памяти.'''









'''a = [1, 1, 1]
b = ''
d = [1, 1, 1]
c = d
c[0] = 2
print(c)
print(d)
print(id(a))
print(id(d))
print(id(c))
print(c is d)


def helper():
    """
    Эта функция-помощник
    """
    pass

print(helper.__doc__)
print('из словаря по ключу находим значение')
zipped = dict(zip(names, salary))
print(round(zipped['Катя'],2), '- зарплата Кати')

a = [1, 1, 1]
b = ''
d = [1, 1, 1]
c = d
c[0] = 2
print(c)
print(d)
print(id(a))
print(id(d))
print(id(c))
print(c is d)


def helper():
    """
    Эта функция-помощник
    """
    pass

print(helper.__doc__)'''