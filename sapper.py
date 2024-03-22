import tkinter as tk
from tkinter import messagebox
import random

# Основной класс игры Сапер
class Game:

    # Конструктор класса
    def __init__(self, root):
        self.root = root
        self.root.title("Сапер")  # Задаем заглавие игры
        # Параметры поля для игры
        self.rows = 10
        self.columns = 10
        self.mines = 8

        # Список для хранения кнопок и позиций для мин
        self.field = []
        self.mine_positions = []

        # генерация позиций для мин и самого игрового поля
        self.generate_mines()

        for i in range(self.rows):
            row = []
            for j in range(self.columns):
                if (i, j) in self.mine_positions:
                    button = self.create_button(self.root, i, j, "*")
                else:
                    count = self.adjacent_mines(i, j)
                    button = self.create_button(self.root, i, j, count)
                row.append(button)
            self.field.append(row)

    # Метод для генерации позиций мин на игровом поле
    def generate_mines(self):
        count = 0
        while count < self.mines:
            x = random.randint(0, self.rows-1)
            y = random.randint(0, self.columns - 1)
            if (x, y) not in self.mine_positions:
                self.mine_positions.append((x, y))
                count += 1

    # создание кнопок для игрового поля
    def create_button(self, parent, x, y, value):
        if value == "*":
            btn = tk.Button(parent, text="", width=3, command=lambda x=x, y=y: self.on_click(x, y))
        else:
            btn = tk.Button(parent, text="", width=3, command=lambda x=x, y=y: self.on_click(x, y))
        btn.grid(row=x, column=y)
        return (btn, value)

    #подсчет мин, находящихся в соседних клетках
    def adjacent_mines(self, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x + i, y + j) in self.mine_positions:
                    count += 1
        return count

    # обработка действий игрока при нажатии на клетку игрового поля
    def on_click(self, x, y):
        if self.field[x][y][1] == "*":
            for mine in self.mine_positions:
                self.field[mine[0]][mine[1]][0].config(text="*", fg="red")
            messagebox.showinfo("Сапер", "Вы проиграли!")
            self.root.destroy()
            return
        else:
            self.field[x][y][0].config(text=self.field[x][y][1])
            self.check_win()

    # выиграл или нет
    def check_win(self):
        for i in range(self.rows):
            for j in range(self.columns):
                if self.field[i][j][0]["text"] == "" and self.field[i][j][1] != "*":
                    return
        messagebox.showinfo("Сапер", "Вы выиграли!")
        self.root.destroy()


root = tk.Tk()
game = Game(root)
root.mainloop()
