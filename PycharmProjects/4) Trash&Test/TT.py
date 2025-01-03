import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

# Пример данных о ходе приема абитуриентов
applicants_data = {
    "Иванов Иван": {"баллы": 250, "статус": "Принят"},
    "Петров Петр": {"баллы": 230, "статус": "На рассмотрении"},
    "Сидоров Сидор": {"баллы": 200, "статус": "Отклонен"},
    "Кузнецова Анна": {"баллы": 260, "статус": "Принят"},
    "Смирнов Алексей": {"баллы": 240, "статус": "На рассмотрении"},
}

# Функция для отображения информации об абитуриенте
def show_applicant_info():
    selected_applicant = applicant_var.get()
    if selected_applicant in applicants_data:
        info = applicants_data[selected_applicant]
        info_text.set(f"ФИО: {selected_applicant}\nБаллы: {info['баллы']}\nСтатус: {info['статус']}")
    else:
        info_text.set("Абитуриент не найден")

# Функция для добавления нового абитуриента
def add_applicant():
    new_name = name_entry.get().strip()
    new_points = points_entry.get().strip()
    new_status = status_combobox.get()

    if not new_name or not new_points:
        info_text.set("Ошибка: Заполните все поля!")
        return

    try:
        new_points = int(new_points)
    except ValueError:
        info_text.set("Ошибка: Баллы должны быть числом!")
        return

    applicants_data[new_name] = {"баллы": new_points, "статус": new_status}
    update_applicant_list()
    update_treeview()
    info_text.set(f"Абитуриент {new_name} добавлен!")

# Функция для редактирования данных абитуриента
def edit_applicant():
    selected_applicant = applicant_var.get()
    if selected_applicant in applicants_data:
        new_points = points_entry.get().strip()
        new_status = status_combobox.get()

        if not new_points:
            info_text.set("Ошибка: Заполните поле 'Баллы'!")
            return

        try:
            new_points = int(new_points)
        except ValueError:
            info_text.set("Ошибка: Баллы должны быть числом!")
            return

        applicants_data[selected_applicant] = {"баллы": new_points, "статус": new_status}
        update_applicant_list()
        update_treeview()
        info_text.set(f"Данные абитуриента {selected_applicant} обновлены!")
    else:
        info_text.set("Ошибка: Абитуриент не выбран!")

# Функция для удаления абитуриента
def delete_applicant():
    selected_applicant = applicant_var.get()
    if selected_applicant in applicants_data:
        del applicants_data[selected_applicant]
        update_applicant_list()
        update_treeview()
        info_text.set(f"Абитуриент {selected_applicant} удален!")
    else:
        info_text.set("Ошибка: Абитуриент не выбран!")

# Функция для обновления списка абитуриентов
def update_applicant_list():
    applicant_var.set("Выберите абитуриента")
    applicant_menu['menu'].delete(0, 'end')
    for applicant in applicants_data:
        applicant_menu['menu'].add_command(label=applicant, command=tk._setit(applicant_var, applicant))

# Функция для обновления Treeview
def update_treeview():
    tree.delete(*tree.get_children())  # Очищаем текущие данные
    for name, data in applicants_data.items():
        tree.insert("", "end", values=(name, data["баллы"], data["статус"]))

# Создание главного окна
root = tb.Window(themename="flatly")  # Используем тему "flatly" для современного дизайна
root.title("Ход приема абитуриентов")
root.geometry("1000x800")
root.resizable(False, False)  # Запрещаем изменение размеров окна

# Заголовок
title_label = ttk.Label(root, text="Текущая информация о ходе приема абитуриентов", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

# Основной фрейм
main_frame = ttk.Frame(root)
main_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Список абитуриентов
applicant_var = tk.StringVar(root)
applicant_var.set("Выберите абитуриента")  # Значение по умолчанию

applicant_label = ttk.Label(main_frame, text="Абитуриенты:", font=("Arial", 12))
applicant_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

applicant_menu = ttk.OptionMenu(main_frame, applicant_var, "Выберите абитуриента", *applicants_data.keys())
applicant_menu.config(width=30)  # Фиксированная ширина выпадающего списка
applicant_menu.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

# Кнопка для просмотра информации
info_button = ttk.Button(main_frame, text="Показать информацию", command=show_applicant_info, style="success.TButton")
info_button.config(width=20)  # Фиксированная ширина кнопки
info_button.grid(row=1, column=0, columnspan=2, pady=10, sticky="ew")

# Добавление нового абитуриента
add_frame = ttk.Frame(main_frame)
add_frame.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="w")

name_label = ttk.Label(add_frame, text="ФИО:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(add_frame)
name_entry.config(width=30)  # Фиксированная ширина поля ввода
name_entry.grid(row=0, column=1, padx=5, pady=5)

points_label = ttk.Label(add_frame, text="Баллы:")
points_label.grid(row=1, column=0, padx=5, pady=5)
points_entry = ttk.Entry(add_frame)
points_entry.config(width=30)  # Фиксированная ширина поля ввода
points_entry.grid(row=1, column=1, padx=5, pady=5)

# Выпадающий список для статуса с использованием Combobox
status_label = ttk.Label(add_frame, text="Статус:")
status_label.grid(row=2, column=0, padx=5, pady=5)
status_combobox = ttk.Combobox(add_frame, values=["На рассмотрении", "Принят", "Отклонен"], state="readonly")
status_combobox.set("На рассмотрении")  # Значение по умолчанию
status_combobox.config(width=30)  # Фиксированная ширина выпадающего списка
status_combobox.grid(row=2, column=1, padx=5, pady=5)

add_button = ttk.Button(add_frame, text="Добавить абитуриента", command=add_applicant, style="primary.TButton")
add_button.config(width=20)  # Фиксированная ширина кнопки
add_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

# Кнопки для редактирования и удаления
edit_button = ttk.Button(main_frame, text="Редактировать", command=edit_applicant, style="warning.TButton")
edit_button.config(width=20)  # Фиксированная ширина кнопки
edit_button.grid(row=3, column=0, pady=10, sticky="ew")

delete_button = ttk.Button(main_frame, text="Удалить", command=delete_applicant, style="danger.TButton")
delete_button.config(width=20)  # Фиксированная ширина кнопки
delete_button.grid(row=3, column=1, pady=10, sticky="ew")

# Метка для вывода информации
info_text = tk.StringVar()
info_text.set("Выберите абитуриента для просмотра информации")
info_label = ttk.Label(main_frame, textvariable=info_text, font=("Arial", 12), wraplength=500)
info_label.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

# Treeview для отображения списка абитуриентов
tree_frame = ttk.Frame(main_frame)
tree_frame.grid(row=1, column=6, columnspan=2, pady=10, padx=10, sticky="nsew")

tree = ttk.Treeview(tree_frame, columns=("ФИО", "Баллы", "Статус"), show="headings")
tree.heading("ФИО", text="ФИО")
tree.heading("Баллы", text="Баллы")
tree.heading("Статус", text="Статус")
tree.column("ФИО", width=200, anchor="center")
tree.column("Баллы", width=100, anchor="center")
tree.column("Статус", width=150, anchor="center")
tree.pack(fill="both", expand=True)

# Обновление Treeview при запуске
update_treeview()

# Запуск приложения
update_applicant_list()
root.mainloop()