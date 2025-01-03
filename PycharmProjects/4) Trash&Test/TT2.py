import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_complete_tree(self, values):
        """
        Строит полное бинарное дерево из списка значений.
        """
        if not values:
            return
        self.root = self._build_tree(values, 0)

    def _build_tree(self, values, index):
        """
        Рекурсивно строит дерево из списка значений.
        """
        if index >= len(values) or values[index] is None:
            return None

        node = TreeNode(values[index])
        node.left = self._build_tree(values, 2 * index + 1)
        node.right = self._build_tree(values, 2 * index + 2)
        return node

    def visualize(self):
        """
        Визуализирует дерево с помощью networkx и matplotlib.
        """
        G = nx.Graph()
        self._build_graph(G, self.root)

        # Создаем фигуру для отображения графа
        fig, ax = plt.subplots(figsize=(8, 6))
        pos = self._get_tree_layout(self.root)  # Расположение узлов
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold", ax=ax)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'), font_color='red')

        return fig

    def _build_graph(self, G, node):
        """
        Рекурсивно строит граф из дерева.
        """
        if node is not None:
            G.add_node(node.value)
            if node.left:
                G.add_edge(node.value, node.left.value, label="Left")
                self._build_graph(G, node.left)
            if node.right:
                G.add_edge(node.value, node.right.value, label="Right")
                self._build_graph(G, node.right)

    def _get_tree_layout(self, node, x=0, y=0, layer_height=1, layer_width=2):
        """
        Возвращает словарь с координатами узлов для визуализации.
        """
        if node is None:
            return {}

        pos = {}
        pos.update(self._get_tree_layout(node.left, x - layer_width, y - layer_height, layer_height, layer_width))
        pos[node.value] = (x, y)
        pos.update(self._get_tree_layout(node.right, x + layer_width, y - layer_height, layer_height, layer_width))
        return pos

class BinaryTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Tree Visualizer")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Главное меню
        self.create_menu()

        # Заголовок
        self.title_label = tk.Label(root, text="Binary Tree Visualizer", font=("Arial", 20), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=20)

        # Поле ввода
        self.input_label = tk.Label(root, text="Enter numbers separated by spaces:", font=("Arial", 12), bg="#f0f0f0", fg="#555")
        self.input_label.pack(pady=5)

        self.entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.entry.pack(pady=10)

        # Кнопка для визуализации
        self.button = tk.Button(root, text="Visualize Tree", command=self.visualize_tree, font=("Arial", 12), bg="#0078d7", fg="white")
        self.button.pack(pady=20)

        # Холст для отображения графа
        self.canvas = None

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # Меню "Файл"
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Меню "Справка"
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root.config(menu=menu_bar)

    def show_about(self):
        messagebox.showinfo("About", "Binary Tree Visualizer\n\nCreated by [Your Name]")

    def visualize_tree(self):
        input_text = self.entry.get()
        if not input_text:
            messagebox.showwarning("Input Error", "Please enter numbers.")
            return

        try:
            numbers = list(map(int, input_text.split()))
        except ValueError:
            messagebox.showerror("Input Error", "Invalid input. Please enter numbers only.")
            return

        tree = BinaryTree()
        tree.build_complete_tree(numbers)

        # Визуализация дерева
        fig = tree.visualize()

        # Отображение графика в интерфейсе
        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = BinaryTreeApp(root)
    root.mainloop()