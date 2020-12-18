import sys
import tkinter as tk

from mathematica.utilities.fonts import HEADER_FONT, BUTTON_FONT
from mathematica.skills.addition import Addition
from mathematica.skills.subtraction import Subtraction
from mathematica.skills.multiplication import Multiplication
from mathematica.skills.division import Division


class SelectSkill(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        controller.unbind('<Return>')

        header_label = tk.Label(self, height=2, font=HEADER_FONT,
                                text="Please select the mathematical skill to learn.")
        header_label.pack(pady=(15, 10))

        addition_button = tk.Button(self, width=13, height=2, text="Addition", font=BUTTON_FONT,
                                    command=lambda event=None: controller.show_frame(Addition))
        addition_button.pack()
        subtraction_button = tk.Button(self, width=13, height=2, text="Subtraction", font=BUTTON_FONT,
                                       command=lambda event=None: controller.show_frame(Subtraction))
        subtraction_button.pack()
        multiplication_button = tk.Button(self, width=13, height=2, text="Multiplication", font=BUTTON_FONT,
                                          command=lambda event=None: controller.show_frame(Multiplication))
        multiplication_button.pack()
        division_button = tk.Button(self, width=13, height=2, text="Division", font=BUTTON_FONT,
                                    command=lambda event=None: controller.show_frame(Division))
        division_button.pack()

        quit_button = tk.Button(self, width=10, height=2, text="Quit", font=BUTTON_FONT,
                                command=lambda event=None: [controller.destroy(),
                                                            sys.exit()])
        quit_button.pack(pady=(15, 0))
