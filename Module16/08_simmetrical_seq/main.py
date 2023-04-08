

massiv = []
additional_massiv = []
count_number = int(input('Количество чисел: '))

for _ in range(count_number):
    number = int(input('Число: '))
    massiv.append(number)
print('Последовательность:', massiv)


for i in list(massiv):
    massiv.append(i)
    additional_massiv.append(i)
    if massiv == massiv[::-1]:
        break

print('Нужно приписать чисел:', len(additional_massiv))
print('Сами числа:', additional_massiv)
print('Результат', massiv)

