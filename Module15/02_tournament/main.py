def tournament(sportsman):
    first_day = []
    print('День первый:', end=' ')
    for index, name in enumerate(sportsman):
        if index % 2 == 0:
            first_day.append(name)
    print(first_day)

sportsman = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
tournament(sportsman)
