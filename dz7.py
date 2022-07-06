import os


file = open('prices.txt', 'r')

prices = file.read()
prod = (input('Введите продукт, который необходим: '))

while True:
    if prod in prices:
        x = input('Товар в наличии. Введите необходимое количество: ')
        b = open('bill.txt', 'a')
        b.write(f'{prod} x {x} шт\n')
        b.close()
        fin = input('Желаете продолжить покупки? ')
        if fin == 'yes':
            prod = (input('Введите продукт, который необходим: '))
        else:
            mail = input('Введите свой email-адрес для чека: ')
            os.rename('bill.txt', f'{mail}.txt')
            print('Спасибо за покупки. Чек будет выслан на ваш email-адрес!')
            break
    else:
        c = input('Такого товара нет в наличии. Желаете найти другой товар? ')
        if c == 'yes':
            prod = (input('Введите продукт, который необходим: '))
        else:
            mail = input('Введите свой email-адрес для чека: ')
            os.rename('bill.txt', f'{mail}.txt')
            print('Спасибо за покупки. Чек будет выслан на ваш email-адрес!')
            break
