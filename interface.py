import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.setWindowConfig()
    def setWindowConfig(self):
        self.root.title("TO-DO LIST")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.minsize(width=500, height=400)