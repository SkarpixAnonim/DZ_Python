data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

letters.extend([i for i in data_tuple if type(i) in [str, bool]])
numbers.extend([i for i in data_tuple if type(i) in [int, float]])

del numbers[0]
del_true = letters.pop(4)
letters.append(del_true)
numbers.insert(1, 2)

numbers.sort()
letters.reverse()
letters[1], letters[-2] = 'G', 'c'

numbers = [i**2 for i in numbers]

letters, numbers = tuple(letters), tuple(numbers)

print(letters)
print(numbers)