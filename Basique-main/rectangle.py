import tkinter as tk

class Rectangle:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=200, height=100)
        self.canvas.pack()
        self.x = 50
        self.y = 150
        self.rect = self.canvas.create_rectangle(self.x, self.x + 20, self.y, self.y + 20, fill="blue")

