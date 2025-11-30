import tkinter as tk
from tkinter import ttk, messagebox, filedialog

window = tk.Tk()
window.title('Арестов Константин Леонидович')
window.geometry('450x450')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Калькулятор')
tab_control.add(tab2, text='Чекбоксы')
tab_control.add(tab3, text='Текст')
tab_control.pack(expand=1, fill="both", padx=20, pady=20)

entry1 = tk.Entry(tab1)
entry1.pack(pady=10)
operation_var = tk.StringVar(value='+')
operation_menu = ttk.Combobox(tab1, textvariable=operation_var, values=['+', '-', '*', '/'], state='readonly')
operation_menu.pack(pady=5)
entry2 = tk.Entry(tab1)
entry2.pack(pady=10)

def calc():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation_var.get()
        result = eval(f"{num1} {op} {num2}")
        messagebox.showinfo("Результат", f"{num1} {op} {num2} = {result}")
    except:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

tk.Button(tab1, text="Вычислить", command=calc).pack(pady=10)

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()

tk.Checkbutton(tab2, text="Первый", variable=var1).pack()
tk.Checkbutton(tab2, text="Второй", variable=var2).pack()
tk.Checkbutton(tab2, text="Третий", variable=var3).pack()

def show_selection():
    if var1.get(): messagebox.showinfo("Выбор", "Вы выбрали первый вариант")
    elif var2.get(): messagebox.showinfo("Выбор", "Вы выбрали второй вариант")
    elif var3.get(): messagebox.showinfo("Выбор", "Вы выбрали третий вариант")
    else: messagebox.showwarning("Внимание", "Вы ничего не выбрали!")

tk.Button(tab2, text="Показать выбор", command=show_selection).pack(pady=10)

text_widget = tk.Text(tab3)
text_widget.pack(expand=True, fill="both", padx=10, pady=10)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(1.0, file.read())

tk.Button(tab3, text="Открыть файл", command=open_file).pack(pady=5)

window.mainloop()