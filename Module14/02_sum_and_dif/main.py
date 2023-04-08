# TODO здесь писать код
def summ_number(number):
    summa = 0
    while number != 0:
        last_numm = number % 10
        summa += last_numm
        number //= 10
    return summa


def number_count_and_difference(number):
    print('Сумма чисел равна:', summ_number(number))
    count = len(str(number))
    print('Количество цифр в числе:', count)
    print('Разность суммы и количества цифр:', summ_number(number) - count)


number = int(input('Введит число: '))
number_count_and_difference(number)
