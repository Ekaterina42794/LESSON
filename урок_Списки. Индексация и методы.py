food=["яблоки","кокос","банан","ананас","12","100"]
print(food) #весь список
print(food[0]) # первый пункт списка
print(food[1]) # второй пункт списка
print(food[2]) # третий пункт списка
print(food[:3]) # первые 3 пункта списка
print(food[1:6:2]) # с 2го по 6ой пункт списка через один (шаг 2)
print(food[0:5:2]) # с начала списка по 5ый пункт с шагом 2(через 1)
print(food[:0:-2])# в обратном порядке весь список через один(шаг -2)
print(food[-1]) #последний пункт списка
food[1]="ТОРТ" # ЗАМЕНИЛИ ВТОРОЙ ПУНКТ СПИСКА
print(food)
food. append("мимоза") # метод .append добавляет новый элемент спиcка в конце
print(food)
food.extend("абвгд") # метод .extend() добавляет в конец списка строку поэлементно, НО
print(food)
food.extend(["абвгд",2]) # ...НО если добавить 2 элемента одновременно,
# то предпоследний обьединится
print(food)

food=["яблоки","кокос","банан","ананас","12","100"]
print(food)
food.remove("яблоки") # метод  .remove() удаляет указанный пункт списка
print(food)
food.remove("12") # метод  .remove() удаляет указанный пункт списка
print(food)

#"команды для работы со списсками"
print("Команды для работы со списками")
food=["яблоки","кокос","банан","ананас","12","100"]
print(food)
print("12" in food) # команда in проверяет есть ли указанный пункт в списке
print("0" in food)
print("12" not in food)   #команда not in проверяет отсутствует ли указанный пункт в списке
print("0" not in food)
#СРЕЗЫ
print("'СРЕЗЫ' ")
food=["яблоки","кокос","банан","ананас","12","100"]
print(food)
print(food[0:6:2])

