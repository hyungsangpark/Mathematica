import tkinter as tk

from mathematica.utilities.fonts import *
import select_skill


class Welcome(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        welcome_header = tk.Label(self, text="Welcome to Mathematica!", font=HEADER_FONT)
        welcome_header.pack(pady=(15, 10))
        welcome_label = tk.Label(self, text="Let's learn some math skills!", font=LABEL_FONT)
        welcome_label.pack(pady=(5, 5))

        tk.Label(self).pack()

        ok_button = tk.Button(self, width=10, height=2, text="Ok", font=BUTTON_FONT,
                              command=lambda event=None: controller.show_frame(select_skill.SelectSkill))
        ok_button.pack()

        # Allows the user to press enter and and open selectSkill module.
        controller.bind('<Return>', lambda event=None: ok_button.invoke())
