import requests
import json
import tkinter as tk
from tkinter import messagebox

def get_data():
    name = entry.get()
    url = f"https://api.github.com/users/{name}"
    response = requests.get(url)
    data = response.json()

    result = {
        'company': data.get('company'),
        'created_at': data.get('created_at'),
        'email': data.get('email'),
        'id': data.get('id'),
        'name': data.get('name'),
        'url': data.get('url')
    }

    with open(f"{name}_info.json", "w") as f:
        json.dump(result, f, indent=2)

    messagebox.showinfo("Готово", f"Данные сохранены в {name}_info.json")

window = tk.Tk()
window.title("GitHub")

entry = tk.Entry(window)
entry.pack()


button = tk.Button(window, text="Получить данные", command=get_data)
button.pack()

window.mainloop()