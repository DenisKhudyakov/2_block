

number_list = [1, 2, 3, 4, 5]
new_list = []
K = int(input('Сдвиг: '))

for index, num in enumerate(number_list):
    new_list.append(number_list[index - K])

print('Изначальный список:', number_list)
print('Сдвинутый список:', new_list)

