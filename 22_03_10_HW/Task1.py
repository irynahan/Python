
def isFirstEqualLast(text):

    if text[0] == text[-1]:
        return "Yes"
    else:
        return "No"

print(isFirstEqualLast("w"))

def lastalf(a):
    for i in range(len(a)-1):
        if a[i]== a[-1]:
            return 'yes'
    else:
        return 'no'

a=input()
print(lastalf(a))

def slova(a):
    kol=0
    for i in a:
        if i== ' ':
            kol= kol +1
    return kol + 1

n = int(input())
for i in range (n):
    a = input()
    print(slova(a))


def reverse(a):
    if a == a[::-1]:
        return 'yes'
    else:
        return 'no'


y = input()
print(reverse(y))

message = 'python is popular porogramming language'
print( message.count('po'))

def de(a):
    t=''
    for i in a:
        if i !='*':
            t= t+i
    return t

y= input()
print(de(y))

import string
def Upper(a):
    count=0
    for i in a:
        if i in string.ascii_uppercase:
            count+= 1
    return count

y= input()
print(Upper(y))
import string
# Задача №113654. Количество цифр

def dNumber(text):
    count = 0
    for i in text:
        if i in string.digits:
            count += 1
    return count

y= input()
print (dNumber(y))

def addStar (text):
    newList = ''
    for i in text:
        newList+=i+"*"
    return newList[:-1]

y= input()
print(addStar(y))

# Задача №113655. Вставить звёздочки
def addStar (text):
    return '*'.join(text)

y= input()
print(addStar(y))

def addStar (text):
    if len(text)%2==0:
        t= '('.join(text[:len(text)//2])
        m= ')'.join(text[len(text)//2:])
    else:
        t= '('.join(text[:len(text)//2+1])
        m= ')'.join(text[len(text)//2:])[1:]
    return '('+t+m+')'

y= input()
print(y[len(y)//2])
print(addStar(y))
x= input()
print(addStar(x))







