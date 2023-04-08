# TODO здесь писать код

def smallest_common_divisor(number):
    i = 1
    while i <= number:
        i += 1
        if number % i == 0:
            return i

number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', smallest_common_divisor(number))