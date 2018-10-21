#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

class Card:
    def __init__(self):
        def generateCard(arg1, arg2):
            list = []

            n = 0
            a = 1
            b = 9

            
            if len(arg1) == 9 and len(arg2) == 9:
                while n <= 8:
                    list.append(random.randint(a, b))
                    while list[n] == arg1[n] or list[n] == arg2[n]:
                        list[n] = random.randint(a, b)
                    if a == 1:
                        a *= 10
                        b += 10
                    elif b == 79:
                        a += 10
                        b += 11
                    else:
                        a += 10
                        b += 10
                    n += 1
            elif len(arg1) == 9 or len(arg2) == 9:
                while n <= 8:
                    list.append(random.randint(a, b))
                    if len(arg1) == 9:
                        while list[n] == arg1[n]:
                            list[n] = random.randint(a, b)
                    elif len(arg2) == 9:
                        while list[n] == arg2[n]:
                            list[n] = random.randint(a, b)

                    if a == 1:
                        a *= 10
                        b += 10
                    elif b == 79:
                        a += 10
                        b += 11
                    else:
                        a += 10
                        b += 10
                    n += 1
            else:
                while n <= 8:
                    list.append(random.randint(a, b))

                    if a == 1:
                        a *= 10
                        b += 10
                    elif b == 79:
                        a += 10
                        b += 11
                    else:
                        a += 10
                        b += 10
                    n += 1


            space1 = random.randint(0, 8)
            
            space2 = random.randint(0, 8)
            while space2 == space1:
                space2 = random.randint(0, 8)
                
            space3 = random.randint(0, 8)
            while space3 == space2 or space3 == space1:
                space3 = random.randint(0, 8)
                
            space4 = random.randint(0, 8)
            while space4 == space3 or space4 == space2 or space4 == space1:
                space4 = random.randint(0, 8)
            
            spaces = [space1, space2, space3, space4]

            for space in spaces:
                list[space] = "  "
            
            return list
            
        self.first = []
        self.second = []
        self.third = []

        self.first = generateCard(self.second, self.third)
        self.second = generateCard(self.first, self.third)
        self.third = generateCard(self.first, self.second)
    
    def show(self):
        
        str1 = "  ".join(str(el) for el in self.first)
        if len(str(self.first[0])) == 1:
            str1 = " " + str1
            
        str2 = "  ".join(str(el) for el in self.second)
        if len(str(self.second[0])) == 1:
            str2 = " " + str2
            
        str3 = "  ".join(str(el) for el in self.third)
        if len(str(self.third[0])) == 1:
            str3 = " " + str3
        return str1 + "\n" + str2 + "\n" + str3

    def check(self, barrel):
        n = 0
        while n <= 8:
            if self.first[n] == barrel:
                self.first[n] = " -"
            if self.second[n] == barrel:
                self.second[n] = " -"
            if self.third[n] == barrel:
                self.third[n] = " -"
            n += 1
        
        checkInf = "Win"
        for el in self.first:
            if type(el) is  int:
                checkInf = "Not yet"
        for el in self.second:
            if type(el) is  int:
                checkInf = "Not yet"
        for el in self.third:
            if type(el) is  int:
                checkInf = "Not yet"
        return checkInf

def start_game():
        
    myCard = Card()
    roboCard = Card()

    bag = []
    n = 0
    while n < 90:
        n += 1
        bag.append(n)
        
    n = 89
    while n >= 0:
        rand = random.randint(0, len(bag) - 1 )
        barrel = bag[rand]
        bag.pop(rand)
        
        resRobo = roboCard.check(barrel)
        if resRobo == "Win":
            n = 0
            print("\n \n \n \n")
            print("Число {}. Компьютер победил :(".format(barrel))
            break
        else:
            print("\n \n \n \n")
            print("Новый бочонок: {} (осталось {})".format(barrel, n))
            print("------ Ваша карточка -----")
            print(myCard.show())
            print("--------------------------")
            print("-- Карточка компьютера ---")
            print(roboCard.show())
            print("--------------------------")
            answer = input("Зачеркнуть цифру? (y/n)")

            if answer == "y":
                resPlayer = myCard.check(barrel) 
                if resPlayer == "Win":
                    n = 0
                    print("Вы победили!")
                    break
                else:
                    n -= 1
            else:
                n -= 1
            
start_game()
