
skates_list = []
man_list = []
found_a_couple = []

count_skates = int(input('Кол-во коньков: '))
for i in range(count_skates):
    size = int(input('Размер '+str(i + 1)+'-й пары: '))
    skates_list.append(size)

count_man = int(input('Кол-во людей: '))
for j in range(count_man):
    size = int(input('Размер ноги ' + str(j + 1) + '-го человека: '))
    man_list.append(size)

for i in skates_list:
    for j in man_list:
        if i == j:
            found_a_couple.append(i)
            break

print('Наибольшее кол-во людей, которые могут взять ролики:', len(found_a_couple))




