#задание 1

a = 1
b = 2

print('переменная а - ', a, 'и', 'переменная b - ', b)

str1 = input('Введите первую строку ')
numb1 = int(input('Введите первое число '))
str2 = input('Введите вторую строку ')
numb2 = int(input('Введите второе число '))

print('Введенные значения -', (str1, numb1, str2, numb2))

#задание 2

time = int(input('Введите время в секундах '))
hours = time // 3600
min = (time - (hours * 3600)) // 60
sec = (time - (hours * 3600) - (min * 60))
print(f"Время в формате чч:мм:сс {hours}:{min}:{sec}")


#задание 3

numb = int(input('Введите число '))
n1 = int(str(numb) + str(numb))
n2 = int(str(numb) + str(numb) + str(numb))
print('Сумма чисел n + nn + nnn =', numb+n1+n2)


#задание 4

a = abs(int(input('Введите целое число ')))
n = a % 10
a = a // 10
while a >= 1:
    if a % 10 > n:
        n = a % 10
    a = a // 10
print ('Самая большая цифра в числе - ', n)


#задание 5

gain = float(input('Введите выручку фирмы '))
charge = float(input('Введите издержки фирмы '))

if gain > charge:
    rent = (gain-charge) / gain
    print('Фирма работает с прибылью. Рентабельность выручки составила ', rent)
    count = int(input('Введите количество работников '))
    m = (gain-charge) / count
    print('Прибыль в расчете на одного сотрудника ', m)
elif gain == charge:
    print('Прибыль равна 0')
else:
    print('Фирма работает в убыток')


#задание 6

a = int(input('Введите результат пробежки в км в первый день '))
b = int(input('Введите желаемый результат пробежки в км  '))
days = 1
while a < b:
   a = a + (a * 0.1)
   days = days + 1
print(days)