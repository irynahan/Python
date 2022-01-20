import math

# A

a = int(input("Enter a triangle side 'A':"))
b = int(input("Enter a triangle side 'B':"))
hypotenuse = math.sqrt(a**2 + b**2)
print(hypotenuse)

# B
name = str(input("Enter your name: "))
print("Hello," + " " + name + "!")

# C
number = int(input("Enter a number "))
print("The next number for the number " + str(number) + " is " + str(number + 1))
print("The previous number for the number " + str(number) + " is " + str(number - 1))

# D and E
pupils = int(input("Enter a number of pupils "))
apple_total = int(input("Enter a number of apples "))
appl_pro_person = apple_total // pupils
print("Every pupil becomes " + str(appl_pro_person) + " apple(s)")

apple_in_basket = apple_total % pupils
print("The rest apples in basket equal to " + str(apple_in_basket))

# G
number = int(input("Enter a number "))
last_number = number%10
print("The last number of number is " + str(last_number))






