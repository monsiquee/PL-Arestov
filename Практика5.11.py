s = input("Введите строку: ")

s = s.replace('!', '.')

max_l = 0
current_l = 0

for i in s:
    if i == 'н':
        current_l += 1
        if current_l > max_l:
            max_l = current_l
    else:
        current_l = 0

print(f"Конечная строка: {s}")
print(f"Наибольшая последовательность 'н': {max_l}")