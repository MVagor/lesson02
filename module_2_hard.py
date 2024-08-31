def key(x):
    massiv = []
    for i in range(1, x):
        for j in range(i + 1, x):
            if x % (i + j) == 0:
                massiv.append(i)
                massiv.append(j)
    return massiv

num = int(input('Введите произвольное число от 3 до 20: '))
result = []
if 3 <= num <= 20:
    result = key(num)
    print(*result)
else:
    print('Некорректное число')
