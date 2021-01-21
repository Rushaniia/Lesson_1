#задание 1
list = [15, 'hello', 8.5, -25, None, True]

for i in list:
    print(type(i))

#задание 2
list = ["q", "w", "e", "r", "t", "y", "u", "i", "o"]

j = 0
for i in range(int(len(list) / 2)):
    list[j], list[j + 1] = list[j + 1], list[j]
    j += 2

print(list)


#задание 3
seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']
seasons_dict = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'Autumn'}
month = int(input("Введите номер месяца: "))
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
    print("Такого месяца не существует")

#задание 4
str1 = input('Введите строку: ')
word = []
n = 1
for i in range (str1.count(' ')+1):
    word = str1.split()
    if len(str(word)) <= 10:
        print(f'{n} {word[i]}')
        n += 1
    else:
        print(f'{n} {word[i] [0:10]}')
        n += 1

#задание 5
list1 = [7, 5, 3, 3, 2]
n = int(input("Введите число: "))
while n != 0:
    for el in range(len(list1)):
        if list1[el] == n:
            list1.insert(el + 1, n)
            break
        elif list1[0] < n:
            list1.insert(0, n)
        elif list1[-1] > n:
            list1.append(n)
    print(f"текущий список - {list1}")
    n = int(input("Введите число "))


