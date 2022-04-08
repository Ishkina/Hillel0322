num = input('Пожалуйста, введите год: ')
n1 = int(num)
n1 %= 400
n2 = int(num)
n2 %= 100
n3 = int(num)
n3 %= 4
if n1 == 0:
    print('Год високосный')
elif n2 == 0:
    print('Год не високосный')
elif n3 == 0:
    print('Год  високосный')
else:
    print('Год не високосный')
