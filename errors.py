#print (10/0) - ZeroDivisionError
#print (int ('qwe')) - ValueError
#print ('2' + 1) - TypeError
try:
    x = int (input())
except ValueError:
    print ("Вы ввели не число")
else:
    print ("Вы ввели число")
try:
    y = int (input())
except ValueError:
    print ("Вы ввели не число")
else:
    print ("Вы ввели число")
finally:
    print ("Выполнится всегда!")
try:
    res = x / y
except ZeroDivisionError:
    print ("Вы ввели ноль. Так нельзя")
    res = 0
print (res)
