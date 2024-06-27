from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("My Awesome Window")
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.isrunning = False