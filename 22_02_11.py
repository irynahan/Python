
# 6

n = int(input("Please enter a number "))
for i in range(n):
    for j in range(n):
        print(i, end='\t')
    print()


# 7

n = int(input("Please enter a number "))
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(0, end='\t')
        else:
            print(1, end='\t')
    print()

# 8

n = int(input("Please enter a number "))
for i in range(n):
    for j in range(n):
        if j %2 == 0:
            print(0, end='\t')
        else:
            print(1, end='\t')
    print()


# 9

n = int(input("Please enter a number "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print(1, end='\t')
        else:
            print(0, end='\t')
    print()


# 1

n = int(input("Please enter a number "))
count = 0
for i in range(n):
    stroka = input("Please enter a text ")
    for letter in stroka:
        if letter == 'a':
            count += 1
print(count)


# 2

for i in range(1,10):
    for j in range(1,10):
        print(i*j, end='\t')
    print()


# 3

for i in range(1,10):
    for j in range (1, 10):
        print(i+j, end='\t')
    print()



# 4

for i in range(1,6):
    for j in range(1,6):
        print(i**j, end='\t')
    print()

# 5

for i in range(1, 6):
    for j in range(1, 6):
        x = i/j
        print(round(x, 2), end='   ')
    print()







