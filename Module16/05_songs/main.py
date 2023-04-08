violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
playlist_Ivan = []

count_songs = int(input('Введите количество песен'))
duration_of_time = 0

for track in range(count_songs):
    add_track = input('Введите название песни ')
    for choice in violator_songs:
        if choice[0].__eq__(add_track):
            playlist_Ivan.append(choice)
            duration_of_time += choice[1]

print('Плайлист Ивана', playlist_Ivan)
print('Продолжительность плэйлиста', round(duration_of_time, 2))


