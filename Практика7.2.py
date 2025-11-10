import math

def Treugolnik(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def Chetirehugolnik(a, b, c, d, diag):
    area1 = Treugolnik(a, b, diag)
    area2 = Treugolnik(c, d, diag)
    return area1 + area2

print("Введите стороны и диагональ выпуклого четырехугольника:")
a = int(input("Сторона a: "))
b = int(input("Сторона b: "))
c = int(input("Сторона c: "))
d = int(input("Сторона d: "))
diag = int(input("Диагональ: "))

area = Chetirehugolnik(a, b, c, d, diag)
print(f"Площадь четырехугольника = {area:.2f}")