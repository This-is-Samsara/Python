#EASY

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
path_dir = [('dir_' + str(i + 1)) for i in range(9)]
for i in path_dir:
    os.mkdir(i)
for i in path_dir:
    os.rmdir(i)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os
for i in os.getcwd():
    os.listdir()
print(os.listdir())

# не уверена, что выполнила задачу верно, т.к. получаю также файлы текущей директории, а как вывести только папки, придумать не смогла


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

import shutil
shutil.copyfile(r'C:\Projects\Python_true\lesson5.py', r'C:\Projects\Python_true\lesson5555.py')

