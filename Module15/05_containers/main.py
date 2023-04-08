def add_containers(count):
    containers = []
    for _ in range(count):
        weight = int(input('Введите вес контейнера: '))
        if weight > 200:
            containers.append(weight)
    print()
    new_container = int(input('Введите вес нового контейнера: '))
    containers.append(new_container)
    containers.sort(reverse=True)

    for index, weight in enumerate(containers):
        if weight == new_container:
            print('Номер, который получит новый контейнер:', index + 1)

count = int(input('Количество контейнеров: '))
add_containers(count)

