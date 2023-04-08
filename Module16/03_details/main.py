shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input('Название деталей ')
count = 0
total_price = 0

for details in shop:
    count += details.count(name)
    if details[0] == name:
        total_price += details[1]
print('Количество деталей:', count)
print('Общая стоимость:', total_price)
