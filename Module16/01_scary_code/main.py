a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
for i in b:
    a.append(i)
print('Количество цифр 5 при первом объединении:', a.count(5))
for i in a:
    if i == 5:
        a.remove(i)
for i in c:
    a.append(i)
print('Количество цифр 3 при втором объединении:', a.count(3))
print('Итоговый список:', a)

# TODO переписать программу
