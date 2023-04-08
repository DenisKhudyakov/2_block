

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']


while True:
    message = input('Гость пришёл или ушёл? ')

    match message:
        case 'пришел':
            guest = input('Имя гостя: ')
            print('Привет', guest)
            print()
            guests.append(guest)
            print('Сейчас на вечеринке', len(guests), 'человек:', guests)
        case 'ушёл':
            guest = input('Имя гостя: ')
            print('Пока', guest)
            print()
            guests.remove(guest)
            print('Сейчас на вечеринке', len(guests), 'человек:', guests)
        case 'Пора спать':
            print()
            print('Вечеринка закончилась, все легли спать.')
            break

