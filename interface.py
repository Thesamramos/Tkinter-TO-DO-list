import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.setWindowConfig()
        self.setFrames()
    def setWindowConfig(self):
        self.root.title("TO-DO LIST")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.minsize(width=500, height=400)
    def setFrames(self):
        self.topFrame = tk.Frame(self.root, bd=4, bg="black")
        self.topFrame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.bottomFrame = tk.Frame(self.root, bd=4, bg="black")
        self.bottomFrame.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
