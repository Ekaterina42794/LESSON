def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)
print(summa(5))


'''def recursion():
    recursion()
recursion() 
#RecursionError: превышена максимальная глубина рекурсии /RecursionError: maximum recursion depth exceeded
'''
stack = []
stack.append(1)
print('Добавили элемент' , stack)
stack.append(2)
print('Добавили элемент' , stack)
stack.append(3)
print('Добавили элемент' , stack)
print(stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)