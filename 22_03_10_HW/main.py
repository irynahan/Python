# Задача №113654. Количество цифр

def dNumber(text):
    count = 0
    for i in text:
        if i.isdigit():
            count += 1
    return count

print (dNumber("AbsdFej123yLxsjdy1"))

# Задача №113655. Вставить звёздочки
def addStar (text):
    newList = []
    for i in text[:len(text)-1]:
        newList.append(i)
        newList.append("*")
    newList.append(text[len(text)-1])
    return ''.join(newList)

print(addStar("Aahjk"))


# Задача №113656. Расставить скобки

def brackets (text):
    newList = []
    if len(text) % 2 == 0:
        for i in text[:len(text)//2]:
            newList.append("(")
            newList.append(i)
        for i in text[len(text)//2:]:
            newList.append(i)
            newList.append(")")
    else:
        for i in text[:len(text)//2+1]:
            newList.append("(")
            newList.append(i)
        for i in text[len(text)//2+1:]:
            newList.append(")")
            newList.append(i)
        newList.append(")")
    return ''.join(newList)

print(brackets("qqqqq"))
print(brackets("q"))
print(brackets("qq"))
print(brackets("qqqqqq"))









