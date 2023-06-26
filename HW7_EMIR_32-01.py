ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_func = list(filter(lambda list: list % 2 == 0, ten))
map_func = list(map(lambda square: square ** 2, filter_func))
print(filter_func)
print(map_func)


def indexFunc(list=ten):
    while True:
        try:
            requestIndex = input('enter list index or q(exit): ')
            if requestIndex == 'q':
                break
            index = int(requestIndex)
            if 0 <= index < len(list):
                print(list[index])
            else:
                print('Некорректный индекс.')
        except ValueError:
            print('Некорректный индекс.')

                
indexFunc(map_func)



