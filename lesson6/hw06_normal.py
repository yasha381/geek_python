# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class Student:
    def __init__(self, full_name, father_name, mother_name, class_r):
        self.full_name = full_name
        self.father_name = father_name
        self.mother_name = mother_name
        self.class_r = class_r
    def getparents(self):
        print("Отец : ", self.father_name, ", \nМать: ", self.mother_name )

    def getsubjects(self):
        list_sub = []
        for teacher in teachers:
            if teacher.start_teach >= int(self.class_r[:-1]):
                list_sub.append(teacher.teach_subject)
        return list_sub
class Class:
    def __init__(self, class_r):
        self.class_r = class_r

    def getteachers(self):
        list_t = []
        for teacher in teachers:
            if teacher.start_teach >= int(self.class_r[:-1]):
                list_t.append(teacher.full_name)
        return list_t
                

    def allclasses(self):
        list_c = []
        for student in students:
            if student.class_r not in list_c:
                list_c.append(student.class_r)

        return list_c

    def getstudents(self):
        list_s = []
        for student in students:
            if student.class_r == self.class_r:
                list_s.append(student.full_name)

        return list_s

class Teacher:
    def __init__(self, full_name, teach_subject, start_teach):
        self.full_name = full_name
        self.teach_subject = teach_subject
        self.start_teach = start_teach
        

class_1 = Class("5A")
class_2 = Class("5B")
class_3 = Class("6A")
class_4 = Class("7A")


student_1 = Student("Барышев Якуб Родионович", "Барышев Родион Мартьянович", "Барышева Анастасия Серафимовна", "5A")
student_2 = Student("Кардапольцев Мстислав Феликсович", "Кардапольцев Барышев Святославович", "Кардапольцева Маргарита Сократовна", "5A")
student_3 = Student("Набережный Петр Панкратиевич", "Набережный Панкрат Ульянович", "Набережная Лидия Эрнестовна", "5A")
student_4 = Student("Зобов Лев Эрнестович", "Зобов Эрнест Казимирович", "Зобова Антонина Никаровна", "5A")

student_5 = Student("Гайденко Даниил Олегович", "Гайденко Олег Евлампиевич", "Гайденко Наталия Валентиновна", "5B")
student_6 = Student("Ясев Ростислав Иосифович", "Ясев Иосиф Серафимович", "Ясева Нина Евдокимовна", "5B")
student_7 = Student("Абрамович Леондий Эрнстович", "Абрамович Эрнст Панкратиевич", "Абрамович Надежда Богдановна", "5B")
student_8 = Student("Кручинин Виктор Кириллович", "Кручинин Кирилл Ипатович", "Кручинина Аза Сидоровна", "5B")

student_9 = Student("Янович Викентий Ипатович", "Янович Архип Наумович", "Янович Вероника Ипполитовна", "6A")
student_10 = Student("Белибердиев Елизар Ильевич", "Белибердиев Илья Трофимович", "Белибердиева Светлана Кондратьевна", "6A")
student_11 = Student("Летавин Андрон Зиновиевич", "Летавин Зиновий Федотович", "Летавин Кира Артемовна", "6A")
student_12 = Student("Толбугин Владлен Ильевич", "Толбугин Илья Севастьянович", "Толбугин Владлена Денисовна", "6A")

student_13 = Student("Коломийцев Валентин Александрович", "Коломийцев Тит Эмилевич", "Коломийцева Агафья Константиновна", "7A")
student_14 = Student("Шадрин Роман Наумович", "Шадрин Наумов Титович", "Шадрина Милена Кондратьевна", "7A")
student_15 = Student("Лидин Святослав Еремеевич", "Лидин Еремей Андроникович", "Лидина Софья Брониславовна", "7A")
student_16 = Student("Шурдук Серафим Аникитевич", "Шурдук Аникит Мартьянович", " Шурдук Юнона Ростиславовна", "7A")

students = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9, student_10, student_11, student_12, student_13, student_14, student_15, student_16]

teacher_1 = Teacher("Иван Иванов Иванович", "Математика", 1)
teacher_2 = Teacher("Букирь Измаил Валериевич", "Русский язык", 1)
teacher_3 = Teacher("Егоров Рубен Никанорович", "Физика", 6)
teacher_4 = Teacher("Ядов Тихон Сократович", "Химия", 7)

teachers = [teacher_1, teacher_2, teacher_3, teacher_4]
print("\nЗадания нормального уровня сложности\n")

print("Все классы :", class_1.allclasses())
print("Ученики 5A :", class_1.getstudents())
print("Предметы ученика Барышева Якуба Родионовича :", student_1.getsubjects())
print("Родители ученика Барышева Якуба Родионовича :")
student_1.getparents()
print("Учителя 5A :", class_1.getteachers())