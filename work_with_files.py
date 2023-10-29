f = open('text.txt', 'r')
print (f.read(1)) #вычитка конкретного количества символов
for line in f: #вычитка всего файла
    print (line)
f.close()


f1 = open('text1.txt', 'w')
f1.write('It\'s me!') #запись в файл
f1.close()
