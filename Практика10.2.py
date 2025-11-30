Fio_Group = "AKL_UB52"

matrix_txt = open(Fio_Group + "_vvod.txt")
n = int(matrix_txt.readline())
s = []
for i in range(n):
    s.append(list(map(float, matrix_txt.readline().split())))
matrix_txt.close()

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

txt_out = open(Fio_Group + "_vivod.txt", "w")
txt_out.write("Результат:\n")
for row in s:
    txt_out.write(str(row) + "\n")
txt_out.close()