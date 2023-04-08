
first_class = []
second_class = []

for i in range(160, 176+1, 2):
    first_class.append(i)

for j in  range(162, 180+1, 3):
    second_class.append(j)

first_class.extend(second_class)
print('Отсортированный список учеников:', sorted(first_class))