#функция with... as в любом случае закроет файл (file.close()), даже если пользователь введет вместо числа строку и выпадет ошибка. Соответственно саму функцию закрытия тут писать не надо.
with open('test.txt', 'wt', encoding='utf-8') as inFile:
    num = int(input())
    line = str('1/ ' + str(num) + ' = ' + str(1 / num))
    print (line)
    inFile.write (line)
