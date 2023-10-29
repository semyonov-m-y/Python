def func (x, a):
    return x + a
    #или так  res = a + x
    #return res
print (func (23, 12))
print (func ('Hello', ' World'))



def func1 (y):
    def add (b):
        return y + b
    return add

test = func1 (100)
print (test (200)) #100 (это y) + 200 (это b) = 300


def func2 ():
    pass #пропускаем - ничего не делаем
print (func2 ()) #выведет None


def func3 (r, w, z = 2): #z - это параметр по умолчанию, записываются последними после не определенных параметров, иначе будет ошибка
    res = r + w
    res *= z
    return res
print (func3 (2, 4)) #можем не указывать z, тк он уже известен, но если укажем 5 например, то просто 2 заменится на 5. Тут выведет 12



def func4 (*args): #кортеж указывается как аргумент
    return args
print (func4 (2, 4, 3)) #выведет (2, 4, 3)


def func5 (**args1): #словарь указывается как аргумент
    return args1
print (func5 (f = 23, g = 56, h = 90))#выведет {'f': 23, 'g': 56, 'h': 90}


#лямбда функции или анонимные функции - может выполнять лишь 1 операцию, а не много, как def func
add = lambda m, n: m * n
print (add (1, 5)) #6
print (add ('q', 5)) #qqqqq


print ((lambda m, n: m + n)(2, 6)) #8 - то есть эту функцию можно не присваивать к переменной


func6 = lambda *args: args
print (func6 (2, 56, 78.56)) #(2, 56, 78.56)









