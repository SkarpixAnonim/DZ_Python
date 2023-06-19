eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
rus = 'йцукенгшщзхъфывапролджэячсмитьбю'

while True:
    text = input('\nвведите англское слово (для выхода напишите "exit", "выход"): ').lower()
    if text == "exit" or text == "выход":
        break
    str = text.replace(' ', '')
    for i in str:
        if i in eng:
            print(rus[eng.index(i)], end='')
        elif i in rus:
            print(eng[rus.index(i)], end='')
        else:
            print("ты случайно не полеглот?")