def videoCards_after_sell(count):
    list_video_card = []
    new_list = []
    for _ in range(count):
        video_card = input('Видеокарта: ')
        list_video_card.append(video_card)
    for card in list_video_card:
        if card != '3090':
            new_list.append(card)
    print('Старый список видеокарт:', list_video_card)
    print('Новый список видеокарт:', new_list)


count = int(input('Количество видеокарт: '))
videoCards_after_sell(count)






