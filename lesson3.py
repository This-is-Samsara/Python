# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

# сначала решила с помощью встроенной функции, даже это далось мне нелегко - жалко удалять, оставила

# через встроенную функцию
n = float(input('Введите число: '))
k = int(input('Введите количество знаков после запятой: '))
    a = round(n,k)
    print(a)

# через написанную функцию
n = float(input('Введите число: '))
nb = int(input('Введите количество знаков после запятой: '))
def my_round(n,nb):
   n = n*(10**nb)+0.51
   n = n//1
   return n/(10**nb)
print(my_round(n,nb))

#Уровень easy Задача 2
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky (ticket,numbers):
    if sum(numbers[0:2]) == sum(numbers[3:5]):
        return('Номер билета '+(ticket)+' является счастливым!')
    else:
        return('Увы, вы проиграли(')

ticket = input('Введите номер билета из шести цифр: ')
nticket = []
for i in ticket:
    nticket.append(int(i))
print(lucky(ticket,nticket))

#Уровень normal Задача 1
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    a, b = 1, 1
    res = [1, ]

    for i in range(m):
        a, b = b, a + b
        res.append(a)

    return res[n - 1:m]

a = int(input('Введите стартовый элемент: '))
b = int(input('Введите завершающий элемент: '))
print(fibonacci(a, b))



