import random
chislo = random.randint(1, 20)
for i in range(1, 6):
    z = int(input('Попытка ' + str(i) +': Угадай число от 1 до 20:'))
    if z < chislo:
       print('Загаданное число меньше.')
    elif z > chislo:
        print('Загаданное число больше.')
    elif z == chislo:
       print('Угадал ! МОЛОДЕЦ')
else:
    print('Попытки закончились. Было загадано число', chislo)