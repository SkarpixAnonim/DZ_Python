def multi(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multi(43, 9, 22, 5, 11))

def mirror(text):
    text2 = list()
    for letter in text:
         text2.append(letter)
    text2.reverse()
    reverse_text = ''.join(text2)
    if text == reverse_text:
        return True
    else:
        return False
    

print(mirror('NA'))


def calculator(num1, operator, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '**':
        result = num1 ** num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '//':
        result = num1 // num2
    elif operator == '%':
        result = num1 % num2
    else:
        result = "Ошибка, вы не правельно ввели данные или оператор не подерживается"
    return result

print(calculator(5, '*', 55))


# def calculator(num1, operator, num2):
#     data = str(num1) + operator + str(num2)
#     result = eval(data)
#     return result


# print(calculator(45, '*', 9))

# def calculator(*expression):
#     expressionStr = ' '.join(map(str, expression))
#     return eval(expressionStr)


# print(calculator())