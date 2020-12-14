import tkinter as tk


class Addition(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        header = tk.Label(self, text="Header")
        header.pack(pady=(15, 10))
