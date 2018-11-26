#уровень easy, задача 1

s = ["яблоко", "банан", "киви", "арбуз"]
for fruit in s:
    print('{}.{:>10}'.format(s.index(fruit)+1,fruit))



#уровень easy, задача 2

s = ['треугольник', 'линейка', 'скамья', 'луг', 'заяц']
l = ['жираф', 'скамья', 'дом', 'заяц', 'зеркало']
for words in s:
    if words in l:
        s.remove(words)
print(s)
print(l)



#уровень easy, задача 3

n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
nn = []
for number in n:
    if number%2==0:
        nn.append(number/4)
    else:
        nn.append(number*2)
print(nn)



#уровень normal, задача 1

n = [2, -5, 8, 9, -25, 25, 4]
import math
nn = []
for number in n:
    if number > 0 and (int(math.sqrt(number)) == math.sqrt(number)):
        nn.append(int(math.sqrt(number)))
print(nn)




