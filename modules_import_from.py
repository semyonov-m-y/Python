#можно подключать сторонние модули (библиотеки) или создавать свои
#даже если модуль написан на с++, его можно подключить для программы Python
import math
import time, os #можно подключать через запятую, но так не надо - ухудшается читаемость
import random as r #присваиваем псевдоним модулю
try: #если не уверены есть ли такой подключаемый модуль
    import nomodule
except ImportError:
    print ("Модуля nomodule не существует")
import mymodule
import platform
from mymodule import hi #если хотим испортировать только одну функцию

print (math.e)
print (math.pi)
print (math.cos(1))
print (time.time())
print (os.getcwd()) #путь к этому файлу
#os.uname() #информация о нашем компьютере. Но работает не во всех ОС, лучше использовать import platform
print (platform.platform())
print (r.random())

mymodule.hi()
print (mymodule.add(45, 15))
#hi(), а не mymodule.hi() - можно вызывать теперь так, если импортировали через from
