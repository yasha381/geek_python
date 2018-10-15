# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
import re
import os
import sys
print('sys.argv = ', sys.argv)
path = os.path.abspath(os.getcwd())

def copyFile(path, filename):
    try:
        with open(os.path.join(path , filename) , 'r', encoding='UTF-8') as f:
            content = f.read()
        filename = "copy-" + filename
        with open(os.path.join(path, filename), 'w', encoding='UTF-8', ) as f:
            f.write(content)
    except FileExistsError:
        print('Такого файла не существует')
        
def createDir(path, filename):
    dir_path = os.path.join(path, filename)
    os.mkdir(dir_path)
    
def delDir(path, filename):
    dir_path = os.path.join(path, filename)
    os.remove(dir_path)

def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

def del_file():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return

    try:
        copyFile(path, file_name)
        print('Файл {} успешно удален'.format(file_name))
    except FileExistsError:
        print('Файла {} не существует'.format(file_name))

def make_copy():
    if not file_name:
        print("Необходимо указать имя файла вторым параметром")
        return

    try:
        copyFile(path, file_name)
        print('Копия файла {} создана'.format(file_name))
    except FileExistsError:
        print('Копия файла {} уже существует'.format(file_name))

def change_dir():
    if not user_path:
        print("Необходимо указать полный путь или относительный вторым параметром")
        return
    global path
    if re.findall(r"\\", user_path) == []:
        print(1)
        files = os.listdir(path)
        files_str = ', '.join(files)
        if re.findall(user_path, files_str) == []:
            print('Такой директории не существует {}'.format(user_path))
        else:
            path = os.path.join(path, user_path)
            print('Вы перешли в директорию {}'.format(user_path))
    else:
        path = user_path
        print('Вы перешли по пути {}'.format(user_path))
        

def view_path():
    print(path)
    
def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": make_copy,
    "rm": del_file,
    "cd": change_dir,
    "ls": view_path 
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    file_name = sys.argv[2]
except IndexError:
    file_name = None

try:
    user_path = sys.argv[2]
except IndexError:
    user_path = None



try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")


