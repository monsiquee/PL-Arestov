def NOD(a, b):
    while b:
        a, b = b, a % b
    return a

def NOK(a, b):
    return (a * b) // NOD(a, b)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

nd = NOD(a, b)
nk = NOK(a, b)

print(f"НОД({a}, {b}) = {nd}")
print(f"НОК({a}, {b}) = {nk}")