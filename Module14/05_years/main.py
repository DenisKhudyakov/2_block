# TODO здесь писать код

def fatality_year(year_start, year_finish):
    print('Годы от', year_start, 'до', year_finish, 'с тремя одинаковыми цифрами\n')
    for i in range(year_start, year_finish + 1):
        a, b, c, d = i // 1000, i // 100 % 10 , i // 10 % 10, i % 10
        if a == b == c or b == c == d or a == c == d or a == b == d:
             print(i, '\n')

year1 = int(input('Введите первый год: '))
year2 = int(input('Введите второй год: '))

fatality_year(year1, year2)