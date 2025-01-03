import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import random
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Создаем граф на основе введенных ребер и весов
def create_graph_from_edges(edges):
    G = nx.Graph()
    for edge in edges:
        u, v, weight = edge
        G.add_edge(u, v, weight=weight)
    return G

# Находим минимальное дерево Штейнера
def steiner_tree(G, terminals):
    # Используем алгоритм Прима для нахождения минимального остовного дерева
    T = nx.minimum_spanning_tree(G)
    
    # Удаляем ребра, которые не соединяют терминалы
    edges_to_remove = []
    for u, v in T.edges():
        if u not in terminals and v not in terminals:
            edges_to_remove.append((u, v))
    T.remove_edges_from(edges_to_remove)
    
    return T

# Визуализация графа и дерева Штейнера
def visualize_graph(G, steiner_tree, terminals, canvas):
    pos = nx.spring_layout(G)
    
    # Рисуем граф
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.set_facecolor('#2c3e50')
    ax.set_title("Задача Штейнера на графах", color="white")
    
    nx.draw(G, pos, with_labels=True, node_color='#3498db', edge_color='#95a5a6', node_size=500, font_color='white', ax=ax)
    nx.draw_networkx_edges(G, pos, edgelist=steiner_tree.edges(), edge_color='#e74c3c', width=2, ax=ax)
    nx.draw_networkx_nodes(G, pos, nodelist=terminals, node_color='#e67e22', node_size=500, ax=ax)
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='white', ax=ax)
    
    # Отображаем график в Tkinter
    canvas.figure = fig
    canvas.draw()

# Вывод таблицы смежности
def print_adjacency_matrix(G, text_widget):
    adj_matrix = nx.to_numpy_array(G)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, "Таблица смежности:\n")
    text_widget.insert(tk.END, str(adj_matrix))

# Основная программа
def main(root):
    def on_calculate():
        try:
            n = int(entry.get())
            if n < 2:
                messagebox.showerror("Ошибка", "Количество вершин должно быть больше 1.")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите целое число.")
            return
        
        # Ввод ребер и их весов пользователем
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                weight = simpledialog.askfloat(f"Вес ребра {i}-{j}", f"Введите вес ребра {i}-{j} (или 0, если ребра нет):")
                if weight:
                    edges.append((i, j, weight))
        
        # Создаем граф на основе введенных ребер и весов
        G = create_graph_from_edges(edges)
        
        # Выбираем случайные терминалы
        terminals = random.sample(list(G.nodes()), 4)
        
        # Находим минимальное дерево Штейнера
        steiner_tree_result = steiner_tree(G, terminals)
        
        # Вычисляем минимальный вес пути
        min_weight = sum(G[u][v]['weight'] for u, v in steiner_tree_result.edges())
        result_label.config(text=f"Минимальный вес пути: {min_weight}")
        
        # Вывод таблицы смежности
        print_adjacency_matrix(G, text_widget)
        
        # Визуализируем граф и дерево Штейнера
        visualize_graph(G, steiner_tree_result, terminals, canvas)
    
    # Создаем главное окно
    root.title("Задача Штейнера на графах")
    root.geometry("800x600")
    root.configure(bg="#2c3e50")
    
    # Создаем виджеты
    frame = tk.Frame(root, bg="#2c3e50")
    frame.pack(pady=20)
    
    label = tk.Label(frame, text="Введите количество вершин:", bg="#2c3e50", fg="white", font=("Helvetica", 12))
    label.pack(side=tk.LEFT, padx=10)
    
    entry = tk.Entry(frame, font=("Helvetica", 12))
    entry.pack(side=tk.LEFT, padx=10)
    
    calculate_button = tk.Button(frame, text="Рассчитать", command=on_calculate, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
    calculate_button.pack(side=tk.LEFT, padx=10)
    
    result_label = tk.Label(root, text="", bg="#2c3e50", fg="white", font=("Helvetica", 12))
    result_label.pack(pady=10)
    
    text_widget = tk.Text(root, height=10, width=50, bg="#34495e", fg="white", font=("Helvetica", 12))
    text_widget.pack(pady=10)
    
    # Создаем холст для отображения графика
    fig, ax = plt.subplots(figsize=(6, 4))
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    main(root)
    root.mainloop()