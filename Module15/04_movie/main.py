def my_playlist(films, count_films):
    my_films_list = []
    for _ in range(count_films):
        add_films = input('Введите название фильма: ')
        if add_films in films:
            my_films_list.append(add_films)
        else:
            print('Ошибка: фильма', add_films, 'у нас нет :(')

    print(f'Ваш список любимых фильмов: {", ".join(my_films_list)}')


films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
count_films = int(input('Сколько фильмов вы хотите добавить: '))

my_playlist(films, count_films)

