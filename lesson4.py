#уровень easy

#  Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

s = [1, 2, 4, 0]
sp = [i**2 for i in s]
print(sp)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

s_1 = ['яблоко', 'банан', 'груша', 'апельсин']
s_2 = ['киви', 'банан', 'грейпфрут', 'яблоко']
s_3 = [i for i in s_1 if i == i in s_2]
print(s_3)

# Задание-3:
#  Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

s_1 = [-12, 9, -24, -3, -2, 6, 13, 12, 8, 34]
s_2 = [i for i in s_1 if i%3 == 0 if i >= 0  if i%4 != 0]
print(s_2)

#уровень normal

# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random

import random
z = []
for i in range(2500):
    z.append(random.randint(0,9))
my_file = open('tekst.txt', 'w+')
for number in z:
    my_file.write(str(number))
my_file.closed

# найти и вывести самую длинную последовательность одинаковых цифр в файле так и не смогла(