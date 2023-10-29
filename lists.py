l = [] #empty array
lis = [1, 56, 'x', 2.34, ['S','t','r','i','n','g']]
print (lis)


a = [a + b for a in 'list' if a != 's' for b in 'soup' if b != 'u']
print (a) #it will print ['ls', 'lo', 'lp', 'is', 'io', 'ip', 'ts', 'to', 'tp']

l.append (23) #add element to list
l.append (34)
print (l)

b = [24, 67]
l.extend (b) #add elements of b list to l list
print (l) #[23, 34, 24, 67]

l.insert (1, 56) #insert number 56 like the secind element in the list
print (l) #[23, 56, 34, 24, 67]

l.append (34)
l.remove (34) #it will delete only first element with number 34 from list
print (l) #[23, 56, 24, 67, 34]

l.pop (0) #it will delete the first element from list
print (l) #[56, 24, 67, 34]

print (l.index (56)) #it will show the place of number 56 in our list - 0

print (l.count (34)) #it will show the number of elements in the list - 1

l.sort () #it will sort our list [24, 34, 56, 67]
print (l)

l.reverse () #it will reverse the list [67, 56, 34, 24]
print (l)

l.clear ()
print (l)

k = [34, 'sd', 56, 34.34]
print (k[-1]) #it will print the last element of the list

i = 0
while i < 4:
    print (k[i])
    i += 1

#item[START:STOP:STEP] - will show everything in the list from START to STOP with STEP
print (k[:]) #will show all the list - [34, 'sd', 56, 34.34]

print (k[1:]) #will start from the 1-st element, not from 0 - ['sd', 56, 34.34]

print (k[:3]) #will show the first 3 elements - [34, 'sd', 56]

print (k[::2]) #STEP will be 2 - [34, 56]

print (k[::-1]) #it will reverse the list - [34.34, 56, 'sd', 34]

a = (43, 56, 45.23, 'd') #неизменяемый список или кортеж (круглые скобки)
#например a(0) = 12 выдаст ошибку
b = [43, 56, 45.23, 'd'] #изменяемый список (квадратные скобки)
#например b[0] = 12 НЕ выдаст ошибку

print (a.__sizeof__ ()) #выдаст 56, тк кортеж занимает меньше памяти
print (b.__sizeof__ ()) #выдаст 72

c = tuple ("hello world")
print (c) #выведет ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')

c = ("hello world")
print (c) #это уже не кортеж, а просто строка

c = "hello world", "sdf"
print (c) #теперь это снова кортеж, то есть всё решает запятая, а не скобки

#функции у кортежей те же, что и у списков, кроме функций, которые что-то меняют, тк кортеж неизменяем
