import os
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
def createDir(path, filename):
    dir_path = os.path.join(path, filename)
    os.mkdir(dir_path)

path = os.getcwd()
n = 1
while n <= 9:
    createDir(path, "dir_" + str(n))
    n += 1

def delDir(path, filename):
    dir_path = os.path.join(path, filename)
    os.remove(dir_path)

path = os.getcwd()
n = 1
while n <= 9:
    delDir(path, "dir_" + str(n))
    n += 1
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def viewDir(path):
    files = os.listdir(path)
    print([ name for name in files if os.path.isdir(os.path.join(path, name)) ])

path = os.getcwd()
viewDir(path)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copyFile(path, filename):
    try:
        with open(os.path.join(path , filename) , 'r', encoding='UTF-8') as f:
            content = f.read()
        filename = "copy-" + filename
        with open(os.path.join(path, filename), 'w', encoding='UTF-8', ) as f:
            f.write(content)
    except FileExistsError:
        print('Такого файла не существует')

path = os.getcwd()
copyFile(path, "del.py")
