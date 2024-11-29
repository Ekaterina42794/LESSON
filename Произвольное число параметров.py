'''def test_funk(*params):
    print('тип: ', params, type(params))
    print('аргумент: ', params)

#

test_funk(1, 2, 3, 4, 5, 6, 7, 8, 9)

def summator(txt,*values,тип='тип'):
    s=0
    for i in values:
        s+=i
    return f'{txt} {s}; {тип} - {type}'
print(summator('сумма чисел: ',1,2,3,4,5,6))'''


'''def info(abc,*posic,name_avtor='KAT',**values):
    print('avtor', name_avtor)
    print('тип',type(values))
    print('аргумент', values)
    for key, values in values.items():
        print(key,'-', values)
    print(posic)
info(1,2,3,name='Katja',kurs='Pyton')'''


def my_sum(n, *args, txt='сумма числ:'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(args)
    print(txt + ':', s)
    print()


my_sum(2, 2, 3, 4, 5, txt='сумма квадратов')
my_sum(3, 2, 3, 4, 5, txt= 'сумма кубов')
