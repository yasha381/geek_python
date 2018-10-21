# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

import os

class Worker:
    def __init__(self, first_name, last_name, payment, work, normal_hour):
        self.first_name = first_name
        self.last_name = last_name
        self.payment = payment
        self.work = work
        self.normal_hour = normal_hour

    def calc(self, hours):
        if hours < self.normal_hour:
            a = self.payment / self.normal_hour
            b = self.normal_hour - int(hours)
            pay = self.payment - a + b

            print("Зарплата: ", self.first_name , self.last_name , " ", pay)
        elif hours > self.normal_hour:
            a = self.payment / self.normal_hour
            b = int(hours) - self.normal_hour
            pay = self.payment + a * b * 2

            print("Зарплата: ", self.first_name , self.last_name , " ", pay)

        elif hours == self.normal_hour:
            print("Зарплата: ", self.first_name , self.last_name , " ", self.payment)


path_workers = os.path.join('data', 'workers')
path_hours = os.path.join('data', 'hours_of')

with open(path_workers, 'r', encoding='UTF-8') as f:
    list = f.readlines()

list.pop(0)
list[5] = list[5] + "0"
new_list = []
for i in list:
    i = i[:-1]
    i = i.replace(" ", ",")
    string = ""
    for n in i:
        if string[-1:] == ",":
            if n != string[-1:]:
                string += n
        else:
            string += n
    new_list.append(string.split(","))

list = []
for i in new_list:
    n = 0
    while n <= 4:
        if n == 2:
            i[n] = int(i[n])
        if n == 4:
            i[n] = int(i[n])
        n += 1
    list.append(i)    

print(list)
worker_1 = Worker(list[0][0], list[0][1], list[0][2], list[0][3], list[0][4])
worker_2 = Worker(list[1][0], list[1][1], list[1][2], list[1][3], list[1][4])
worker_3 = Worker(list[2][0], list[2][1], list[2][2], list[2][3], list[2][4])
worker_4 = Worker(list[3][0], list[3][1], list[3][2], list[3][3], list[3][4])
worker_5 = Worker(list[4][0], list[4][1], list[4][2], list[4][3], list[4][4])
worker_6 = Worker(list[5][0], list[5][1], list[5][2], list[5][3], list[5][4])

worker_1.calc(120)
worker_2.calc(160)
worker_3.calc(122)
worker_4.calc(118)
worker_5.calc(180)
worker_6.calc(80)
