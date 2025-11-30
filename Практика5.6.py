s = input("Введите строку: ")

count = 0
new_s = ""

for i in s:
    if i == 'а':
        count += 1
    else:
        new_s += i

print(f"Новая строка: {new_s}")
print(f"Кол-во удалённых букв 'а': {count}")