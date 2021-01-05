import tkinter as tk

from mathematica.utilities.fonts import *
import mathematica.main_menu.select_skill as select_skill


class Welcome(tk.Frame):
    """
    A frame component class which provides a frame welcoming user when the app is first opened.

    The user can either select from one of the four skills or can quit the program.
    """

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        # Initialize this component as a frame component inside the parent component.
        tk.Frame.__init__(self, parent)

        # ====== Components ======
        welcome_header = tk.Label(self, text="Welcome to Mathematica!", font=HEADER_FONT)
        welcome_header.pack(pady=(15, 10))
        welcome_label = tk.Label(self, text="Let's learn some math skills!", font=LABEL_FONT)
        welcome_label.pack(pady=(5, 5))

        tk.Label(self).pack()

        ok_button = tk.Button(self, width=10, height=2, text="Ok", font=BUTTON_FONT,
                              command=lambda event=None: controller.show_frame(select_skill.SelectSkill))
        ok_button.pack()
        # ====== Components End ======

        # Allows the user to press enter and invoke Ok button.
        controller.bind('<Return>', lambda event=None: ok_button.invoke())
