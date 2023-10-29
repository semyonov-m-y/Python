int1 = 10
print(int1)

float1 = 12.14
print(float1)


string1 = "123" #равно str(123)
print(string1)


#тут выведет строку, а не число
num1 = input("Enter 1 num: ")
num2 = input("Enter 2 num: ")
res = num1 + num2
print(res)


#а вот тут приводим всё к числу
num1 = input("Enter 1 num: ")
num2 = input("Enter 2 num: ")
res = int (num1) + int (num2)
print(res)
#или так
num1 = int (input("Enter 1 num: "))
num2 = int (input("Enter 2 num: "))
res = num1 + num2
print(res)


#число и строку плюсовать нельзя

#удалить переменную можно так del res


res +=5 #равно res = res + 5


#названия переменных чувствительны к регистру, поэтому res и Res - разные переменные

#несколько раз вывести строку можно так
Res = input ("Enter something: ")
Res *= 5
print (Res)
