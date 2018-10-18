# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.






import math

class Trapezium:
    def __init__(self, A1, A2, B1, B2, C1, C2, D1, D2):
        self.A1 = A1
        self.A2 = A2
        self.B1 = B1
        self.B2 = B2
        self.C1 = C1
        self.C2 = C2
        self.D1 = D1
        self.D2 = D2

    def check(self):
        a = math.sqrt((self.B1 - self.A1)**2 + (self.B2 - self.A2)**2)
        b = math.sqrt((self.C1 - self.B1)**2 + (self.C2 - self.B2)**2)
        c = math.sqrt((self.D1 - self.C1)**2 + (self.D2 - self.C2)**2)
        d = math.sqrt((self.D1 - self.A1)**2 + (self.D2 - self.A2)**2)

        if a == c or b == d:
            print("Трапеция является равнобедренной")
        else:
            print("Трапеция не является равнобедренной!")

    def square(self):
        a = math.sqrt((self.B1 - self.A1)**2 + (self.B2 - self.A2)**2)
        b = math.sqrt((self.C1 - self.B1)**2 + (self.C2 - self.B2)**2)
        c = math.sqrt((self.D1 - self.C1)**2 + (self.D2 - self.C2)**2)
        d = math.sqrt((self.D1 - self.A1)**2 + (self.D2 - self.A2)**2)

        
        if a == c:
            if b > d:
                h = math.sqrt(a**2 - ((b-d)**2/4))
            else:
                h = math.sqrt(a**2 - ((d-b)**2/4))
            s = (b + d)/2*h
        elif b == d:
            if a > c:
                h = math.sqrt(b**2 - ((a-c)**2/4))
            else:
                h = math.sqrt(b**2 - ((c-a)**2/4))
            s = (a + c)/2*h
        return s

        
    def perimeter(self):
        a = math.sqrt((self.B1 - self.A1)**2 + (self.B2 - self.A2)**2)
        b = math.sqrt((self.C1 - self.B1)**2 + (self.C2 - self.B2)**2)
        c = math.sqrt((self.D1 - self.C1)**2 + (self.D2 - self.C2)**2)
        d = math.sqrt((self.D1 - self.A1)**2 + (self.D2 - self.A2)**2)

        p = a + b + c + d

        return p
        
    def sides(self):
        a = math.sqrt((self.B1 - self.A1)**2 + (self.B2 - self.A2)**2)
        b = math.sqrt((self.C1 - self.B1)**2 + (self.C2 - self.B2)**2)
        c = math.sqrt((self.D1 - self.C1)**2 + (self.D2 - self.C2)**2)
        d = math.sqrt((self.D1 - self.A1)**2 + (self.D2 - self.A2)**2)

        return [a, b, c, d]

trapezium_1 = Trapezium(2, 1, 4, 9, 7, 9, 9, 1)
print("Трапеция с координатами (2, 1) (4, 9) (9, 10) (10, 1)")
trapezium_1.check()
print("Площадь равняется ", trapezium_1.square())
print("Периметр равняется ", trapezium_1.perimeter())
print("Стороны периметра ", trapezium_1.sides())

trapezium_2 = Trapezium(2, 1, 4, 9, 7, 5, 10, 1)
print("\nТрапеция с координатами (2, 1) (4, 9) (9, 10) (10, 1)")
trapezium_2.check()


class Triangle:
    def __init__(self, A1, A2, B1, B2, C1, C2):
        self.A1 = A1
        self.A2 = A2
        self.B1 = B1
        self.B2 = B2
        self.C1 = C1
        self.C2 = C2
        
    def square(self):
        a = math.sqrt((self.B1 - self.A1)**2 + (self.B2 - self.A2)**2)
        b = math.sqrt((self.C1 - self.A1)**2 + (self.C2 - self.A2)**2)
        c = math.sqrt((self.C1 - self.B1)**2 + (self.C2 - self.B2)**2)
        if a**2 + b**2 == c**2:
            s = (a*b)/2
        elif b**2 + c**2 == a**2:
            s = (b*c)/2
        elif c**2 + a**2 == b**2:
            s = (c*a)/2
        else:
            if a == b and a == c:
                h = math.sqrt(a**2 - (a**2/4))
                s = (a*h)/2
            if a == b or a == c or b == c:
                if a == b:
                    h = math.sqrt(a**2 - (c**2/4))
                    s = (c*h)/2
                elif a == c:
                    h = math.sqrt(a**2 - (b**2/4))
                    s = (b*h)/2
                elif b == c:
                    h = math.sqrt(b**2 - (a**2/4))
                    s = (a*h)/2
            else:
                p = (a + b + c)/ 2
                h = ( 2 *(math.sqrt(p*(p - a)*(p - b)*(p - c)) ) ) / a
                s = (a*h)/2  
        return s
    
    def height(self):
        a = math.sqrt((self.B1 - self.A1)**2 + (self.B2 - self.A2)**2)
        b = math.sqrt((self.C1 - self.A1)**2 + (self.C2 - self.A2)**2)
        c = math.sqrt((self.C1 - self.B1)**2 + (self.C2 - self.B2)**2)
        if a**2 + b**2 == c**2:
            h = a*b/c
        elif b**2 + c**2 == a**2:
            h = b*c/a
        elif c**2 + a**2 == b**2:
            h = c*a/b
        else:
            if a == b and a == c:
                h = math.sqrt(a**2 - (a**2/4))
            if a == b or a == c or b == c:
                if a == b:
                    h = math.sqrt(a**2 - (c**2/4))
                elif a == c:
                    h = math.sqrt(a**2 - (b**2/4))
                elif b == c:
                    h = math.sqrt(b**2 - (a**2/4))
            else:
                p = (a + b + c)/ 2
                h = ( 2 *(math.sqrt(p*(p - a)*(p - b)*(p - c)) ) ) / a
        return h
    
    def perimeter(self):
        a = math.sqrt((self.B1 - self.A1)**2 + (self.B2 - self.A2)**2)
        b = math.sqrt((self.C1 - self.A1)**2 + (self.C2 - self.A2)**2)
        c = math.sqrt((self.C1 - self.B1)**2 + (self.C2 - self.B2)**2)
        p = a + b + c
        return p

triangle_1 = Triangle(2, 1, 4, 9, 4, 1)
print("\nПлощадь треугольника", triangle_1.square())    
print("Высота треугольника", triangle_1.height())    
print("Периметр треугольника", triangle_1.perimeter())
