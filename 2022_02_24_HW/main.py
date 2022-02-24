
# Задача №112471. Все различные цифры

a = input("Input a string")
res_set = set();
for i in a:
    if i in ('0','1','2','3','4','5','6','7','8','9'):
        res_set.add(i)
if len(res_set)==0:
    print("NO")
else:
    print(sorted(res_set))

# Задача №112472. Повторяющиеся цифры

a = input("Input a string")
uniq_values = set();
for i in a:
    if i in ('0','1','2','3','4','5','6','7','8','9'):
        uniq_values.add(i)
if len(res_set)==0:
    print("NO")
else:
    for i in sorted(uniq_values):
        count = 0
        for j in a:
            if i == j:
                count +=1
        if count>1:
            print(i, end='')


# Задача №112477. Сколько различных символов

a = input("Input a string")
res = a.lower()
uniq_set = set(res)
print(len(uniq_set))






