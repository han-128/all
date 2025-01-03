import tkinter as tk 
import random 
import re 

def generate_sequence(): 
    words = [] 
    for _ in range(random.randint(30, 90)): 
        word = ''.join(random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') for _ in range(random.randint(1, 10))) 
        if re.match("^[а-яА-Я]+$", word):  # проверяем, что слово состоит только из кириллических символов 
            words.append(word) 
    return ' '.join(words) + '.' 
 
def sort_sequence(sequence): 
    words = sequence.split() 
    words.sort() 
    sorted_sequence = ' '.join(words) 
    return sorted_sequence 
 
def display_sorted_sequence(): 
    sequence = entry.get() 
     
    if not re.match("^[а-яА-Я\s.]+$", sequence): 
        result_label.config(text="Введены неправильные значения. Для ввода доступна только кириллица.") 
    else: 
        sorted_sequence = sort_sequence(sequence) 
        result_label.config(text=sorted_sequence) 
 
 
root = tk.Tk() 
root.title('Сортировка последовательности слов по алфавиту') 
root.geometry('500x300') 
 
label = tk.Label(root, text='Введите последовательность слов:', font=('Arial', 12)) 
label.pack() 
 
entry = tk.Entry(root, font=('Arial', 12)) 
entry.pack() 
 
generate_button = tk.Button(root, text='Сгенерировать последовательность', command=lambda: entry.insert(0, generate_sequence()), font=('Arial', 12)) 
generate_button.pack() 
 
sort_button = tk.Button(root, text='Отсортировать', command=display_sorted_sequence, font=('Arial', 12)) 
sort_button.pack() 
 
result_label = tk.Label(root, text='', font=('Arial', 12)) 
result_label.pack() 
 
root.mainloop()