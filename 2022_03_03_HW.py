
# Задача №112471. Все различные цифры

a = input("Input a string ")
res_set = set()
for i in a:
    if i.isdigit():
        res_set.add(i)
if len(res_set)==0:
    print("NO")
else:
    print(' '.join(map(str, sorted(res_set))))

# Задача №112472. Повторяющиеся цифры

a = input("Input a string")
uniq_values = set();
for i in a:
    if i.isdigit():
        uniq_values.add(i)
if len(uniq_values)==0:
    print("NO")
else:
    for i in sorted(uniq_values):
        count = 0
        for j in a:
            if i == j:
                count +=1
        if count>1:
            print(i, end=' ')


# Задача №112475. Правильное имя переменной

a = input("Input a string ")
if a[0].isdigit():
    print('NO')
elif a.isalpha() or a.isdigit() or a.__contains__('_'):
    print('YES')
else:
    print('NO')


# Задача №112476. Удалить повторы

a = input("Input a string ")
unique_list = []
unique_list.append(a[0])
for i in a:
    if i not in unique_list:
        unique_list.append(i)
print(''.join(map(str, unique_list)))


# Задача №112477. Сколько различных символов

a = input("Input a string")
res = a.lower()
uniq_set = set(res)
print(len(uniq_set))



# Задача №112478. Символы-одиночки

a = input("Input a string ")
one_in_list = []
one_in_list.append(a[0])
for i in a[1:len(a)]:
    if i in one_in_list:
        one_in_list.remove(i)
    else:
        one_in_list.append(i)
if len(one_in_list) == 0:
    print("NO")
else:
    for i in one_in_list:
        print('1' + i, end='')

# Задача №112479. Цифры, которых нет

a = input("Input a string ")
digit_set = set()
all_digits = [0,1,2,3,4,5,6,7,8,9]
for i in a:
    if i.isdigit():
        digit_set.add(i)
for j in digit_set:
    if j in all_digits:
        all_digits = all_digits.remove(j)
print(all_digits)












