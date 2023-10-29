if 1:
    print ("true\n")
print ("OK")

    
num = input ("Enter your num: ")

if num == "1":
    print ("true")

if num != "1":
    print ("false")


if int (num) < 0:
    if int (num) < -10:
        print ("Less than -10")
    else:
        print ("Less than 0")
elif int (num) > 10:
    print ("More than 10")
else:
    print ("Number from 0 to 10")


name = input()
A = 'Yes' if name != "Test" else 'No'
print (A)
