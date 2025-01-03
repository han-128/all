import random
import tkinter as tk

def find_longest_sequence(dominoes):
    def helper(sequence, remaining):
        if not remaining:
            return sequence
        
        longest = sequence
        for i, domino in enumerate(remaining):
            if sequence[-1][1] == domino[0]:
                new_sequence = helper(sequence + [domino], remaining[:i] + remaining[i+1:])
                if len(new_sequence) > len(longest):
                    longest = new_sequence
            elif sequence[-1][1] == domino[1]:
                new_sequence = helper(sequence + [(domino[1], domino[0])], remaining[:i] + remaining[i+1:])
                if len(new_sequence) > len(longest):
                    longest = new_sequence
        return longest

    longest_sequence = []
    for i, domino in enumerate(dominoes):
        sequence = helper([domino], dominoes[:i] + dominoes[i+1:])
        if len(sequence) > len(longest_sequence):
            longest_sequence = sequence
    



    return longest_sequence

def generate_domino_sequence():
    try:
        N = int(domino_entry.get())  
        dominoes = [(random.randint(0, 6), random.randint(0, 6)) for _ in range(N)] 

        dominoesSIMVOL = ""

        print(dominoesSIMVOL)

        longest_sequence = find_longest_sequence(dominoes)  
        
        output.delete(1.0, tk.END)

        longest_sequence = SSS(a = longest_sequence)
        dominoes = SSS(dominoes)

        output.insert(tk.END, f"{dominoes}\n{longest_sequence}")
    except ValueError:
        output.delete(1.0, tk.END)
        output.insert(tk.END, "Please enter a valid number for domino count.")

def SSS(a):
    dominoesSIMVOL = ""
    for i in range(len(a)):
        if a[i] == (0,0): dominoesSIMVOL = dominoesSIMVOL + "🁣"
        elif a[i] == (0,1): dominoesSIMVOL = dominoesSIMVOL + "🀲 "
        elif a[i] == (0,2): dominoesSIMVOL = dominoesSIMVOL + "🀳 "
        elif a[i] == (0,3): dominoesSIMVOL = dominoesSIMVOL + "🀴 "
        elif a[i] == (0,4): dominoesSIMVOL = dominoesSIMVOL + "🀵 "
        elif a[i] == (0,5): dominoesSIMVOL = dominoesSIMVOL + "🀶 "
        elif a[i] == (0,6): dominoesSIMVOL = dominoesSIMVOL + "🀷 "

        elif a[i] == (1,0): dominoesSIMVOL = dominoesSIMVOL + "🀸 "
        elif a[i] == (1,1): dominoesSIMVOL = dominoesSIMVOL + "🁫"
        elif a[i] == (1,2): dominoesSIMVOL = dominoesSIMVOL + "🀺 "
        elif a[i] == (1,3): dominoesSIMVOL = dominoesSIMVOL + "🀻 "
        elif a[i] == (1,4): dominoesSIMVOL = dominoesSIMVOL + "🀼 "
        elif a[i] == (1,5): dominoesSIMVOL = dominoesSIMVOL + "🀽 "
        elif a[i] == (1,6): dominoesSIMVOL = dominoesSIMVOL + "🀾 "

        elif a[i] == (2,0): dominoesSIMVOL = dominoesSIMVOL + "🀿 "
        elif a[i] == (2,1): dominoesSIMVOL = dominoesSIMVOL + "🁀 "
        elif a[i] == (2,2): dominoesSIMVOL = dominoesSIMVOL + "🁳"
        elif a[i] == (2,3): dominoesSIMVOL = dominoesSIMVOL + "🁂 "
        elif a[i] == (2,4): dominoesSIMVOL = dominoesSIMVOL + "🁃 "
        elif a[i] == (2,5): dominoesSIMVOL = dominoesSIMVOL + "🁄 "
        elif a[i] == (2,6): dominoesSIMVOL = dominoesSIMVOL + "🁅 "

        elif a[i] == (3,0): dominoesSIMVOL = dominoesSIMVOL + "🁆 "
        elif a[i] == (3,1): dominoesSIMVOL = dominoesSIMVOL + "🁇 "
        elif a[i] == (3,2): dominoesSIMVOL = dominoesSIMVOL + "🁈 "
        elif a[i] == (3,3): dominoesSIMVOL = dominoesSIMVOL + "🁻"
        elif a[i] == (3,4): dominoesSIMVOL = dominoesSIMVOL + "🁊 "
        elif a[i] == (3,5): dominoesSIMVOL = dominoesSIMVOL + "🁋 " 
        elif a[i] == (3,6): dominoesSIMVOL = dominoesSIMVOL + "🁌 "

        elif a[i] == (4,0): dominoesSIMVOL = dominoesSIMVOL + "🁍 "
        elif a[i] == (4,1): dominoesSIMVOL = dominoesSIMVOL + "🁎 "
        elif a[i] == (4,2): dominoesSIMVOL = dominoesSIMVOL + "🁏 "
        elif a[i] == (4,3): dominoesSIMVOL = dominoesSIMVOL + "🁐 "
        elif a[i] == (4,4): dominoesSIMVOL = dominoesSIMVOL + "🂃"
        elif a[i] == (4,5): dominoesSIMVOL = dominoesSIMVOL + "🁒 "
        elif a[i] == (4,6): dominoesSIMVOL = dominoesSIMVOL + "🁓 "
        
        elif a[i] == (5,0): dominoesSIMVOL = dominoesSIMVOL + "🁔 "
        elif a[i] == (5,1): dominoesSIMVOL = dominoesSIMVOL + "🁕 "
        elif a[i] == (5,2): dominoesSIMVOL = dominoesSIMVOL + "🁖 "
        elif a[i] == (5,3): dominoesSIMVOL = dominoesSIMVOL + "🁗 "
        elif a[i] == (5,4): dominoesSIMVOL = dominoesSIMVOL + "🁘 "
        elif a[i] == (5,5): dominoesSIMVOL = dominoesSIMVOL + "🂋"
        elif a[i] == (5,6): dominoesSIMVOL = dominoesSIMVOL + "🁚 "

        elif a[i] == (6,0): dominoesSIMVOL = dominoesSIMVOL + "🁛 "
        elif a[i] == (6,1): dominoesSIMVOL = dominoesSIMVOL + "🁜 "
        elif a[i] == (6,2): dominoesSIMVOL = dominoesSIMVOL + "🁝 "
        elif a[i] == (6,3): dominoesSIMVOL = dominoesSIMVOL + "🁞 "
        elif a[i] == (6,4): dominoesSIMVOL = dominoesSIMVOL + "🁟 "
        elif a[i] == (6,5): dominoesSIMVOL = dominoesSIMVOL + "🁠 "
        elif a[i] == (6,6): dominoesSIMVOL = dominoesSIMVOL + "🂓"
    return dominoesSIMVOL



root = tk.Tk()
root.title("Domino Sequence Finder")
root.geometry("1600x400")
root.config(bg='lightblue')


domino_label = tk.Label(root, text="Введите количество домино:", font=("Arial", 16))
domino_label.pack(pady=10)
domino_entry = tk.Entry(root, font=("Arial", 16))
domino_entry.pack(pady=5)

button = tk.Button(root, text="Найти самую длинную последовательность", command=generate_domino_sequence, bg="lightgrey", font=("Arial", 12))
button.pack(pady=10)


output = tk.Text(root, height=10, width=40, font=("Arial",60))
output.place(x = 300, y = 150, width = 1200, height = 200)

TEXT = tk.Text(root, height=10, width=40, font=("Arial",18))
TEXT.place(x = 50, y = 150, width = 250, height = 200)
TEXT.insert(tk.END, "\n" + "\n" + "Случайные домино" + "\n" + "\n" +"Масимальная" + "\n" + "последовательность")

root.mainloop()
