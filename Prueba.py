"""
from PIL import Image
path1 = "C:\\I Semestre 2021\\AA\\Fractales_Proyecto2\\Siluetas\\silueta1.jpg"
path2 = "C:\\Users\\Alejandra G\\OneDrive\\Escritorio\\AleG\\scrennArbolpy.jpeg"
img = Image.open(path1).convert("1")  # convert image to 8-bit grayscale
#img = img.resize((200, 200))
#img.show()
WIDTH, HEIGHT = img.size
data = list(img.getdata()) # convert image data to a list of integers
# convert that to 2D list (list of lists of integers)
data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]

# At this point the image's pixels are all in memory and can be accessed
# individually using data[row][col].

# For example:
for row in data:
    print(' '.join('{:3}'.format(value) for value in row))

# Here's another more compact representation.
"""
import turtle
import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Raw Turtle")
        self.canvas = tk.Canvas(master)
        self.canvas.config(width=600, height=200)
        self.canvas.pack(side=tk.LEFT)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor("cyan")
        self.button = tk.Button(self.master, text="Press me", command=self.press)
        self.button.pack()
        self.my_lovely_turtle = turtle.RawTurtle(self.screen, shape="turtle")
        self.my_lovely_turtle.color("green")

    def do_stuff(self):
        for color in ["red", "yellow", "green"]:
            self.my_lovely_turtle.color(color)
            self.my_lovely_turtle.right(120)

    def press(self):
        self.do_stuff()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()