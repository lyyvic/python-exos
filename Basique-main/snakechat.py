import tkinter as tk
import random

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.body = [(100, 100)]
        self.direction = "Right"
        self.directions = {"Up": (0, -20), "Down": (0, 20), "Left": (-20, 0), "Right": (20, 0)}
        self.canvas.bind_all("<Key>", self.change_direction)

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + self.directions[self.direction][0], head_y + self.directions[self.direction][1])

        # Vérifier si le serpent atteint les bords du jeu
        if not (0 <= new_head[0] < 800 and 0 <= new_head[1] < 600):
            # Choisir une direction aléatoire entre le haut et le bas
            self.direction = random.choice(["Up", "Down"])
            new_head = (head_x + self.directions[self.direction][0], head_y + self.directions[self.direction][1])

        self.body = [new_head] + self.body[:-1]
        self.draw()

    def draw(self):
        self.canvas.delete("snake")
        for segment in self.body:
            x, y = segment
            self.canvas.create_rectangle(x, y, x+20, y+20, fill="green", tag="snake")

    def change_direction(self, event):
        if event.keysym in self.directions:
            opposite_directions = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
            if self.direction != opposite_directions[event.keysym]:
                self.direction = event.keysym

    def check_collision(self, apple):
        head_x, head_y = self.body[0]
        apple_x, apple_y = apple.position
        if (head_x, head_y) == (apple_x, apple_y):
            self.body.append(self.body[-1])
            apple.spawn()

class Apple:
    def __init__(self, canvas):
        self.canvas = canvas
        self.spawn()

    def spawn(self):
        x = random.randrange(0, 40) * 20
        y = random.randrange(0, 30) * 20
        self.position = (x, y)
        self.canvas.create_rectangle(x, y, x+20, y+20, fill="red", tag="apple")

    def remove(self):
        self.canvas.delete("apple")

class Game:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=800, height=600, bg="black")
        self.canvas.pack()
        self.snake = Snake(self.canvas)
        self.apple = Apple(self.canvas)
        self.master.after(100, self.update)

    def update(self):
        self.snake.move()
        self.snake.check_collision(self.apple)
        self.master.after(100, self.update)

def main():
    root = tk.Tk()
    root.title("Snake Game")
    game = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()