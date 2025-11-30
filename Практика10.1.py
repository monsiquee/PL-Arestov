Fio_Group = "AKL_UB_52"

matrix_txt = open(Fio_Group + "_vvod.txt")
n = int(matrix_txt.readline())
s = []
for i in range(n):
    s.append(list(map(int, matrix_txt.readline().split())))
matrix_txt.close()

txt_out = open(Fio_Group + "_vivod.txt", "w")

txt_out.write("Наибольшие элементы в строках:\n")
for i in range(n):
    txt_out.write(f"Строка {i+1}: {max(s[i])}\n")

txt_out.write("\nНаименьшие элементы в столбиках:\n")
for j in range(n):
    min_val = s[0][j]
    for i in range(1, n):
        if s[i][j] < min_val:
            min_val = s[i][j]
    txt_out.write(f"Столбик {j+1}: {min_val}\n")

txt_out.close()