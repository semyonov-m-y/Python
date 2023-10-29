d = {'test' : 1, 'test_2' : "TEST"} #создание словаря (фигурные скобки)
print (d) #вывести весь словарь
print (d['test_2']) #вывести 2-й элемент словаря, выводится всегда по ключу


d1 = dict (short='dict', longer='dictionary') #создание словаря (круглые скобки)
print (d1)


d2 = dict (short='dict', longer='dictionary') #создание словаря (круглые скобки)
d2['short'] = 234 #замена значения элемента словаря
print (d2)


d3 = dict ([(23, 34), (54, 87)]) #списки в словаре
print (d3)


d4 = dict.fromkeys(['a', 'b']) #создание ключей без значений
print (d4)


d5 = dict.fromkeys(['a', 'b'], 1) #создание ключей c одинаковым значением
print (d5)


d6 = {a : a ** 2 for a in range(7)} #значение ключа увеличиваем 7 раз
print (d6)


person = {'name' : {'last_name' : 'Ivanov', 'first_name' : 'Ivan',
'middle_name' : 'Ivanovich'}, 'address' : ['Moscow', 'Lenin street'],
'phone' : {'home_phone' : '34-67-12', 'mobile_phone' : '89159159115',}}
print (person)
print (person ['phone']['mobile_phone'])


#dict.items() - возвращает пары (ключ, значение)
print (person.items())
#dict_items([('name', {'last_name': 'Ivanov', 'first_name': 'Ivan', 'middle_name': 'Ivanovich'}), ('address', ['Moscow', 'Lenin street']), ('phone', {'home_phone': '34-67-12', 'mobile_phone': '89159159115'})])

#dict.keys() - возвращает ключи в словаре
print (person.keys())
#dict_keys(['name', 'address', 'phone'])

#dict.popitems() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

#dict.setdefault(key, default) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default

#dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются

#dict.values() - возвращает значения в словаре

#dict.clear() - очищает словарь

#dict.copy() - возвращает копию словаря
print (person.copy())

          
