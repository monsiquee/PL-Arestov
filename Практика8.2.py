n = int(input())

s = []
for i in range(n):
    f = list(map(float, input().split()))
    s.append(f)

max_val = s[0][0]
max_i, max_j = 0, 0

for i in range(n):
    if s[i][i] > max_val:
        max_val = s[i][i]
        max_i, max_j = i, i

    if s[i][n - 1 - i] > max_val:
        max_val = s[i][n - 1 - i]
        max_i, max_j = i, n - 1 - i

center_i = n // 2
center_j = n // 2

s[max_i][max_j], s[center_i][center_j] = s[center_i][center_j], s[max_i][max_j]

print("Результат:")
for f in s:
    print(f)