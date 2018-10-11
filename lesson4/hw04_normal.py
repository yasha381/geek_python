# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
print("Задание-1 (normal)")
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
import re
def func(line): # 1 способ
    x = []
    y = ""
    for i in line:
        if re.match('^[a-z]', i):
            y += i
        elif re.match('^[A-Z]', i):
            if y != "":
                x.append(y)
                y = ""
    return x
newLine = func(line)
print("1 способ")
print(newLine)


def func1(line): # 2 способ
    x = []
    y = ""
    alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ALP = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in line:
        for el in alp:
            if i == el:
                y += i
        for el in ALP:
            if i == el:
                if y != "":
                    x.append(y)
                    y = ""
    return x
newLine1 = func1(line)
print("2 способ")
print(newLine1)
print("\n")


# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
print("Задание-2 (normal)")
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
import re
print("1 способ")
def func2(line): # 1 способ
    a = ''
    d = []
    for i in line:
        if len(a) < 5:
            a += i
        else:
            y = 1
            c = "0"
            

            if re.match('^[a-z]', a[0]):
                c = '1'
            if c == '1':
                if re.match('^[a-z]', a[1]):
                    c = '2'
                if c == '2': 
                    if re.match('^[A-Z]', a[2]):
                        c = '3'
                    if c == '3':
                        if re.match('^[A-Z]', a[3]):
                            c = '4'
                        if c == '4':
                            if re.match('^[A-Z]', a[4]):
                                c = '5'

            if c != '5':
                a = a[1:]
                a += i
            elif c == '5':
                if len(a) >= 5:
                    c = a[:]
                    if re.match('^[A-Z]', i):
                        a += i
                        y += 1
                    if a == c:
                        
                        d.append(a[2:-2])
                        while y > 0:
                            a = a[-1:]
                            y -= 1
                        y = 1
                        a += i
    return d
newLine_2 = func2(line_2)
print(newLine_2)




print("2 способ")
def key(a, alp, ALP):  # 2 способ
    c = "0"
    for r in alp:
        if a[0] == r:
            c = '1'
    if c == '1':
        for n in alp:
            if a[1] == n:
                c = '2'
        if c == '2': 
            for l in ALP:
                if a[2] == l:
                    c = '3'
            if c == '3':
                for m in ALP:
                    if a[3] == m:
                        c = '4'
                if c == '4':
                    for s in ALP:
                        if a[4] == s:
                            c = '5'
    return c

def func3(line):
    a = ''
    d = []
    alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ALP = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for i in line:
        if len(a) < 5:
            a += i
        else:
            y = 1
            c = key(a, alp, ALP)

            if c != '5':
                a = a[1:]
                a += i
            elif c == '5':
                if len(a) >= 5:
                    c = a[:]
                    for h in ALP:
                        if i == h:
                            a += i
                            y += 1
                    if a == c:
                        
                        d.append(a[2:-2])
                        while y > 0:
                            a = a[-1:]
                            y -= 1
                        y = 1
                        a += i
    return d
newLine_3 = func3(line_2)
print(newLine_3)
print("\n")

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
print("Задание-3 (normal)")
import os
import random

a = ""
for el in range(2500):
    if a == "":
        a += str(random.randint(1, 9))
    else:
        a += str(random.randint(0, 9))
path = os.path.join('files', 'file.txt')
with open(path , 'w', encoding='UTF-8') as f:
    f.write(a)

with open(path , 'r', encoding='UTF-8') as f:
    num = f.readlines()

p = ""
list = []
for i in num[0]:
    if len(p) > 0:
        if i == p[-1]:
            p += i
        else:
            if len(p) > 1:
                list.append(p)
                p = ""
                p += i
            else:
                p = ""
                p += i
    else:
        p += i
d = []
for i in list:
    if len(d) == 0:
        d.append(i)
    else:     
        if len(i) > len(d[0]):
            d = []
            d.append(i)
        elif len(i) == len(d[0]):
            d.append(i)
print("самые длинные последовательности цифр")
print(d)
