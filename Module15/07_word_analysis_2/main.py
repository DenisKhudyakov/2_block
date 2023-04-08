def analysis_word(word):
    revers_word = ''
    for i in reversed(word):
        revers_word += i
    if word.__eq__(revers_word):
        print('Слово является палиндромом')
    else:
        print('Слово не является палиндромом')

word = input('Введите слово: ')
analysis_word(word)
