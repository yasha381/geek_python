# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    n = int(n)
    m = int(m)
    a = 1
    b = 1
    c = 0
    while b < n:
        c = a + b
        a = b
        b = c
    while b <= m:
        print(b)
        c = a + b
        a = b
        b = c
n = input("Введите число n: ")
m = input("Введите число m: ")
fibonacci(n, m)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    n = 1 
    while n < len(origin_list):
         for i in range(len(origin_list)-n):
              if origin_list[i] > origin_list[i+1]:
                   origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
         n += 1

list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
sort_to_max(list)
print(list)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
ages = [5, 12, 17, 18, 24, 32]

def filFunc(function, iterable):
    a = []
    for i in iterable:
        if function(i) == True:
            a.append(i)
    return a
    

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filFunc(myFunc, ages)

for x in adults:
  print(x)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def parall(x1, y1, x2, y2):
    
    if x1 - x2 == 0:
        slope = float(inf)
    else:
        slope = (y1 - y2) / (x1 - x2)
    return slope

    
list = [[-5, 1], [-4, 4], [-1, 5], [-2, 2]]
slope_ab = parall(list[0][0], list[0][1], list[1][0], list[1][1])
slope_ac = parall(list[0][0], list[0][1], list[2][0], list[2][1])
slope_ad = parall(list[0][0], list[0][1], list[3][0], list[3][1])
slope_bc = parall(list[1][0], list[1][1], list[2][0], list[2][1])
slope_bd = parall(list[1][0], list[1][1], list[3][0], list[3][1])
slope_cd = parall(list[2][0], list[2][1], list[3][0], list[3][1])
if (slope_ab == slope_cd) or (slope_ac == slope_bd) or (slope_ad == slope_bc):
    print("Это вершины параллелограмма")
else:
    print("Это не вершины параллелограмма")

    