# ~~~~ Задача 1 ~~~~

print("Введите 10 целых чисел:")

n = []
for i in range(10):
    num = int(input(f'Число {i + 1}: '))
    n.append(num)

max_num = max(n)

count_l = 0
count_m = 0

for num in n:
    if num < max_num:
        count_l += 1
    elif num > max_num:
        count_m += 1

print("~~~~ Задача 1 ~~~~")
print(f'Максимальный элемент: {max_num}')
print(f'Кол-во элементов меньше максимального: {count_l}')
print(f'Кол-во больше максимального: {count_m}')


# ~~~~ Задача 2 ~~~~

total = 0

for num in n:
    if num > 5:
        total += num

print("~~~~ Задача 2 ~~~~")
print(f"Сумма чисел, больших 5: {total}")