import math

# Task №2937
number = int(input("Please enter a number "))
print ("The next number for the number %d is %d. \nThe next number for the number %d is %d. " % (number, (number +1), number, (number -1)))


# Task №3467

pupils_class1 = int(input("Please enter a number of pupils in the 1st class "))
pupils_class2 = int(input("Please enter a number of pupils in the 2nd class "))
pupils_class3 = int(input("Please enter a number of pupils in the 3rd class "))
desk_number = math.ceil(pupils_class1/2) + math.ceil(pupils_class2/2) + math.ceil(pupils_class3/2)
print(desk_number)


# TASK №112161

month_number = int(input("Please enter a number of month "))
if(month_number>= 3 and month_number<=5):
    print("spring")
elif(month_number>5 and month_number<=8):
    print("summer")
elif(month_number>8 and month_number<=11):
    print("autum")
elif(month_number in (12,1,2)):
    print("winter")
else:
    print("No")


# TASK №112162

month_number = int(input("Please enter a number of month "))
if(month_number==2):
    print(28)
elif(month_number in (4,6,9,11)):
    print(30)
elif(month_number in (1,3,5,7,8,10,12)):
    print(31)
else:
    print("0")


# Task №112160

(a,b,c) = input("Введите 3 числа через пробел ").split()
if (a == b and b == c):
    print(3)
elif (a == b or b==c or c==a):
    print(2)
else:
    print(0)
    
# Task №112147
number = float(input("Please enter a number "))
print("%.3f" % (number**10))


# Task №295

a = int(input())
b = int(input())
c = int(input())
if (a + b > c and b + c > a or a + c > b):
    print('YES')
else:
    print('NO')




