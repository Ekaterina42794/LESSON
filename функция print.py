'''https://pythonchik.ru/osnovy/funkciya-print'''

print(type('one'),'one')
print(type(12),12)
print(type(3.14),3.14)
print(type(True),True)
print(type([1,2,3]),[1,2,3])
print(type({'red','green'}),{'red','green'})
print(type({'name':'Alice','age':42}),{'name':'Alice','age':42})
print(type((1,2,3)),(1,2,3))
# one two
print("<<< sep >>>")
print('hello', 'world', sep=None)

print('hello', 'world', sep=' ')
print('hello', 'world')
print('перенос', 'строки', sep='\n') # перенос строки
print('hello', 'world', sep='-')

print('Если функция должна выводить аргументы в виде отдельных строк,'
      'можно передать символ экранирования: \n')
print('hello', 'world', sep='\n')
print('Более полезный пример — вывод аргументов в виде пути к файлу: / ')
print('home', 'user', 'documents', sep='/')

print('<<< end >>>')
'''Второй необязательный параметр — end.
Он позволяет предотвратить разрыв строки, когда выведенное сообщение не должно 
заканчиваться символом новой строки. Для этого передается пустая строка:
'''
print('Checking file integrity...',end='')
# end=''  скрепляет две строки 'Checking file integrity...ok'
print('ok')
print('Checking file integrity...',end='  ')
# end=''  скрепляет две строки 'Checking file integrity...  ok'
print('ok')
print('Checking file integrity...',end='*')
# end=''  скрепляет две строки 'Checking file integrity...  ok'
print('ok')

'''Как и в случае с sep, end можно использовать для объединения отдельных фрагментов 
в один большой. При этом вместо объединения аргументов текст из каждого вызова функции 
будет располагаться в одной строке:'''

print('The first sentence', end='. ')
print('The second sentence', end='. ')
print('The last sentence.')
#The first sentence. The second sentence. The last sentence.

'''При необходимости можно указывать одновременно два ключевых аргумента:'''
print('Mercury', 'Venus', 'Earth', sep=', ', end='!')
# Mercury, Venus, Earth!
print() # остановить склейку строк
'''Еще одни параметры print() file и flush. В примере ниже реализована запись логов в файл 
порциями. С помощью параметра file  данные выводятся не на экран, а в файл.
Flush незамедлительно сбрасывает накопленный буфер в файл каждые 10 итераций.'''

print('<<< file и flush >>>')
import time

source_file = open('parse.txt', 'w')
for i in range(0, 30):
    if i % 10 == 0 and i > 0:
        print(f"iteration #{i}", file=source_file, flush=True)
    else:
        print(f"iteration #{i}", file=source_file)
    time.sleep(1)

source_file.close()

'''Блочная буферизация (block-buffered)
Операции ввода и вывода иногда буферизуются с целью повышения производительности. 
Рассмотрим пример:
'''
import time

num_seconds = 1
for countdown in reversed(range(num_seconds + 1)):
    if countdown > 0:
        print(countdown, end="...")
        time.sleep(1)
    else:
        print('Go!')
'''В качестве конца строки мы используем "...". В такой реализации функция print() будет
накапливать строки в буфер, и выведет сразу весь результат после вызова '''
print('Go!')
print('Go!')
'''Линейная буферизация (line-buffered)
Линейная буферизация потока, перед началом ввода/вывода, ожидает момента, пока в буфере 
не появится разрыв строки. Изменив print() в примере выше на следующий:

print(countdown, end="\n")
мы увидим последовательную печать на экран:
'''
from time import sleep


def progress(percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print('\r[', '#' * left, ' ' * right, ']',
          f' {percent:.0f}%',
          sep='', end='', flush=True)


for i in range(101):
    progress(i)
    sleep(0.1)
