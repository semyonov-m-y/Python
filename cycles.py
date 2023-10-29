i = 1000
while i > 100:
    print (i)
    i /= 2


for j in 'hello world':
    print (j * 2, end = '')

print ('\n')

for j in 'hello world':
    print (j * 2)

print ('\n')

for j in 'hello world':
    if j == 'w':
        continue
    print (j * 2, end = '')

print ('\n')

for j in 'hello world':
    if j != 'w':
        continue
    print (j * 2, end = '')

print ('\n')

for j in 'hello world':
    if j == 'w':
        break
    print (j * 2, end = '')

print ('\n')

for j in 'hello world':
    if j == 'a':
        break
    print (j * 2, end = '')
else:
    print ('\n')
    print ("Letter a is absent")
