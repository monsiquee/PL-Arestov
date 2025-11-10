n = int(input("Введите число n: "))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print(f"{n}! = {factorial}")

# input = запрос числа
# int = превращение числа в целое
# for i in range(1, n + 1) = перебор чисел от 1 до n (включительно)
# factorial *= i = упрощённая запись строки factorial = factorial * i

# в принте f указывает на то, что строка форматированная, а в {} подставляется значение переменной сразу в строку