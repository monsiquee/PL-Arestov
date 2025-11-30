n = int(input("Введите размер матрицы: "))

s = []
for i in range(n):
    f = list(map(int, input().split()))
    s.append(f)

print("Наибольшие элементы в строках:")
for i in range(n):
    max_f = max(s[i])
    print(f"Строка {i+1}: {max_f}")

print("Наименьшие элементы в столбиках:")
for j in range(n):
    min_f = min(s[i][j] for i in range(n))
    print(f"Столбик {j+1}: {min_f}")