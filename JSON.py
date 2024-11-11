#Источник: https://pythonstart.ru/string/preobrazovanie-stroki-v-json-v-python

'''JSON: означает «JavaScript Object Notation», файлы JSON состоят из текста, который
может быть легко прочитан людьми и представлен в виде пар атрибут-значение.
Расширение файлов JSON — «.json».
Давайте посмотрим на первый подход к преобразованию строки в json в Python.
 Использование json.dumps()
Поскольку здесь цель состоит в том, чтобы преобразовать строку в файл json, мы сначала импортируем модуль json.
Следующим шагом является инициализация json-объекта, в котором у нас есть имя субъекта в качестве ключей, а затем
указываются их соответствующие значения.
После этого мы использовали dumps() для преобразования объекта Python в строку json.
Наконец, мы будем использовать load() для анализа строки JSON и преобразования ее в словарь. '''

# converting string to json
import json
# initialize the json object
i_string = {'C_code': 1, 'C++_code' : 26, 'Java_code' : 17, 'Python_code' : 28}
# printing initial json
i_string = json.dumps(i_string)
print("The declared dictionary is ", i_string)
print("It's type is ", type(i_string))
# converting string to json
res_dictionary = json.loads(i_string)
# printing the final result
print("The resultant dictionary is ", str(res_dictionary))
print("The type of resultant dictionary is", type(res_dictionary))
#________________________________________________________________________
'''Использование eval()'''
'''Давайте разберемся, что мы сделали в указанной выше программе. 
1) Сначала мы импортируем модуль json. 
2) Следующим шагом является инициализация json-объекта, в котором у нас есть имя субъекта в качестве ключей,
 а затем указываются их соответствующие значения. 
3)После этого мы использовали eval() для преобразования строки Python в json.
4) При выполнении программы отображается желаемый результат.'''

# converting string to json
import json

# initialize the json object
i_string = """ {'C_code': 1, 'C++_code' : 26, 'Java_code' : 17, 'Python_code' : 28} """

# printing initial json
print("The declared dictionary is ", i_string)
print("Its type is ", type(i_string))

# converting string to json
res_dictionary = eval(i_string)

# printing the final result
print("The resultant dictionary is ", str(res_dictionary))
print("The type of resultant dictionary is ", type(res_dictionary))

#_______________________________________________________________________
'''Получение значений 
Наконец, в последней программе мы получим значения после преобразования строки в json.
Давайте посмотрим на это.'''
import json
i_dict = '{"C_code": 1, "C++_code" : 26, "Java_code":17, "Python_code":28}'
res = json.loads(i_dict)
print(res["C_code"])
print(res["Java_code"])

'''**************************
На выходе мы можем наблюдать следующие вещи: 
1) Мы преобразовали строку в json с помощью json.loads(). 
2) После этого мы использовали ключи «C_code» и «Java_code», чтобы получить их соответствующие значения. 
Вывод: мы узнали, как преобразовать строку в json с помощью Python          '''