import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Entry, Button

class Film:
    def __init__(self, title, year, director, genre, country):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.country = country

    def __repr__(self):
        return f"{self.title} ({self.year}) - {self.director}, {self.genre}, {self.country}"

class FilmLibrary:
    def __init__(self):
        self.films = []
        self.genres = set()
        self.countries = set()

    def add_film(self, film):
        self.films.append(film)
        self.genres.add(film.genre)
        self.countries.add(film.country)

    def remove_film(self, title):
        self.films = [film for film in self.films if film.title != title]

    def search_film(self, title=None, year=None, director=None, genre=None, country=None):
        results = self.films
        if title:
            results = [film for film in results if title.lower() in film.title.lower()]
        if year:
            results = [film for film in results if film.year == year]
        if director:
            results = [film for film in results if director.lower() in film.director.lower()]
        if genre:
            results = [film for film in results if genre.lower() in film.genre.lower()]
        if country:
            results = [film for film in results if country.lower() in film.country.lower()]
        return results

    def sort_films(self, by='title'):
        if by == 'title':
            self.films.sort(key=lambda film: film.title)
        elif by == 'year':
            self.films.sort(key=lambda film: film.year)
        elif by == 'director':
            self.films.sort(key=lambda film: film.director)
        elif by == 'genre':
            self.films.sort(key=lambda film: film.genre)
        elif by == 'country':
            self.films.sort(key=lambda film: film.country)

class FilmLibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Домашняя фильмотека")
        self.root.geometry("1000x500")
        self.root.configure(bg="#2c3e50")  # Темно-синий фон главного окна
        self.library = FilmLibrary()

        self.create_widgets()

    def create_widgets(self):
        self.menu_frame = tk.Frame(self.root, bg="#2c3e50")
        self.menu_frame.pack(pady=20)

        self.add_button = tk.Button(self.menu_frame, text="Добавить фильм", command=self.open_add_film_window, bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(self.menu_frame, text="Удалить фильм", command=self.open_remove_film_window, bg="#f44336", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.menu_frame, text="Найти фильм", command=self.open_search_window, bg="#2196F3", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        self.search_button.pack(side=tk.LEFT, padx=10)

        self.sort_button = tk.Button(self.menu_frame, text="Сортировать фильмы", command=self.open_sort_window, bg="#FF9800", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        self.sort_button.pack(side=tk.LEFT, padx=10)

        self.view_button = tk.Button(self.menu_frame, text="Просмотреть фильмы", command=self.view_films, bg="#9C27B0", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        self.view_button.pack(side=tk.LEFT, padx=10)

        self.result_text = tk.Text(self.root, height=20, width=80, bg="#34495e", fg="white", font=("Helvetica", 12))  # Темно-синий фон и белый текст
        self.result_text.pack(pady=20)

    def open_add_film_window(self):
        add_window = Toplevel(self.root)
        add_window.title("Добавить фильм")
        add_window.geometry("400x300")
        add_window.configure(bg="#34495e")  # Темно-синий фон окна добавления фильма

        Label(add_window, text="Название фильма:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5)
        title_entry = Entry(add_window, font=("Helvetica", 12))
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(add_window, text="Год выпуска:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
        year_entry = Entry(add_window, font=("Helvetica", 12))
        year_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(add_window, text="Режиссер:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5)
        director_entry = Entry(add_window, font=("Helvetica", 12))
        director_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(add_window, text="Жанр:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5)
        genre_entry = Entry(add_window, font=("Helvetica", 12))
        genre_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(add_window, text="Страна:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, padx=10, pady=5)
        country_entry = Entry(add_window, font=("Helvetica", 12))
        country_entry.grid(row=4, column=1, padx=10, pady=5)

        add_button = Button(add_window, text="Добавить", command=lambda: self.add_film(title_entry.get(), year_entry.get(), director_entry.get(), genre_entry.get(), country_entry.get()), bg="#4CAF50", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        add_button.grid(row=5, column=0, columnspan=2, pady=20)

    def add_film(self, title, year, director, genre, country):
        try:
            year = int(year) if year else None
        except ValueError:
            messagebox.showwarning("Ошибка", "Год должен быть числом!")
            return

        if title and year and director and genre and country:
            film = Film(title, year, director, genre, country)
            self.library.add_film(film)
            messagebox.showinfo("Успех", "Фильм добавлен!")
        else:
            messagebox.showwarning("Ошибка", "Все поля должны быть заполнены!")

    def open_remove_film_window(self):
        remove_window = Toplevel(self.root)
        remove_window.title("Удалить фильм")
        remove_window.geometry("400x200")
        remove_window.configure(bg="#34495e")  # Темно-синий фон окна удаления фильма

        Label(remove_window, text="Название фильма:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=20)
        title_entry = Entry(remove_window, font=("Helvetica", 12))
        title_entry.grid(row=0, column=1, padx=10, pady=20)

        remove_button = Button(remove_window, text="Удалить", command=lambda: self.remove_film(title_entry.get()), bg="#f44336", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        remove_button.grid(row=1, column=0, columnspan=2, pady=20)

    def remove_film(self, title):
        if title:
            self.library.remove_film(title)
            messagebox.showinfo("Успех", "Фильм удален!")
        else:
            messagebox.showwarning("Ошибка", "Название фильма должно быть заполнено!")

    def open_search_window(self):
        search_window = Toplevel(self.root)
        search_window.title("Найти фильм")
        search_window.geometry("400x300")
        search_window.configure(bg="#34495e")  # Темно-синий фон окна поиска фильма

        Label(search_window, text="Название фильма:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5)
        title_entry = Entry(search_window, font=("Helvetica", 12))
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(search_window, text="Год выпуска:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
        year_entry = Entry(search_window, font=("Helvetica", 12))
        year_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(search_window, text="Режиссер:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5)
        director_entry = Entry(search_window, font=("Helvetica", 12))
        director_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(search_window, text="Жанр:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=3, column=0, padx=10, pady=5)
        genre_entry = Entry(search_window, font=("Helvetica", 12))
        genre_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(search_window, text="Страна:", bg="#34495e", fg="white", font=("Helvetica", 12)).grid(row=4, column=0, padx=10, pady=5)
        country_entry = Entry(search_window, font=("Helvetica", 12))
        country_entry.grid(row=4, column=1, padx=10, pady=5)

        search_button = Button(search_window, text="Поиск", command=lambda: self.search_film(title_entry.get(), year_entry.get(), director_entry.get(), genre_entry.get(), country_entry.get()), bg="#2196F3", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        search_button.grid(row=5, column=0, columnspan=2, pady=20)

    def search_film(self, title=None, year=None, director=None, genre=None, country=None):
        try:
            year = int(year) if year else None
        except ValueError:
            messagebox.showwarning("Ошибка", "Год должен быть числом!")
            return

        results = self.library.search_film(title, year, director, genre, country)
        self.display_results(results)

    def open_sort_window(self):
        sort_window = Toplevel(self.root)
        sort_window.title("Сортировать фильмы")
        sort_window.geometry("300x250")
        sort_window.configure(bg="#34495e")  # Темно-синий фон окна сортировки

        sort_by_title_button = Button(sort_window, text="По названию", command=lambda: self.sort_films('title'), bg="#FF9800", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        sort_by_title_button.pack(pady=10)

        sort_by_year_button = Button(sort_window, text="По году", command=lambda: self.sort_films('year'), bg="#FF9800", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        sort_by_year_button.pack(pady=10)

        sort_by_director_button = Button(sort_window, text="По режиссеру", command=lambda: self.sort_films('director'), bg="#FF9800", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        sort_by_director_button.pack(pady=10)

        sort_by_genre_button = Button(sort_window, text="По жанру", command=lambda: self.sort_films('genre'), bg="#FF9800", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        sort_by_genre_button.pack(pady=10)

        sort_by_country_button = Button(sort_window, text="По стране", command=lambda: self.sort_films('country'), bg="#FF9800", fg="white", font=("Helvetica", 12), padx=10, pady=5)
        sort_by_country_button.pack(pady=10)

    def sort_films(self, by):
        self.library.sort_films(by)
        messagebox.showinfo("Успех", "Фильмы отсортированы!")
        self.view_films()

    def view_films(self):
        self.display_results(self.library.films)

    def display_results(self, results):
        self.result_text.delete(1.0, tk.END)
        if results:
            for film in results:
                self.result_text.insert(tk.END, f"{film}\n")
        else:
            self.result_text.insert(tk.END, "Фильмы не найдены.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FilmLibraryApp(root)
    root.mainloop()