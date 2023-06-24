countries = {
    'kg': {'red', 'yellow'},
    'ru': {'red', 'white', 'blue'},
    'kz': {'blue', 'yellow'},
    'ua': {'red', 'white', 'blue'},
    'tr': {'red', 'white'},
}

while True:
    colors = input('Введите цвета или введите "q" для выхода: ')
    if colors == 'q':
        break

    found_countries = set() 
    
    for key, value_set in countries.items():
        if all(color in value_set for color in colors.split()):
            found_countries.add(key)

    if found_countries:
        print("Флаги стран, содержащих указанные цвета:", ", ".join(found_countries))
    else:
        print("Нет флагов стран, содержащих указанные цвета.")
