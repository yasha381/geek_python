# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    dot = str(number).find(".")
    num_str_tmp = ""
    
    num_str = str(number)[:dot + ndigits + 1]
    num_last = int(str(number)[dot + ndigits + 1])
    
    if num_last >= 5:
        length = len(num_str)
        extra = True
        
        while length > 0:
            if num_str[length - 1] != ".":
                num_tmp = str(int(num_str[length - 1]) + extra)
                if len(num_tmp) > 1:
                    extra = True
                else:
                    extra = False
                num_str_tmp = num_tmp[-1] + num_str_tmp
            else:
                num_str_tmp = "." + num_str_tmp
            length = length - 1
            
    return float(num_str_tmp)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    a = int(str(ticket_number)[0]) + int(str(ticket_number)[1]) + int(str(ticket_number)[2])
    b = int(str(ticket_number)[3]) + int(str(ticket_number)[4]) + int(str(ticket_number)[5])
    if a == b:
        return "Билет счастливый!"
    else:
        return "Вам не повезло. Билет не счастливый."

print(lucky_ticket(123006))
print(lucky_ticket(436751))
