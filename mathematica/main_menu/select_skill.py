import tkinter as tk

from mathematica.utilities.fonts import HEADER_FONT, BUTTON_FONT
from mathematica.skills.addition import Addition
from mathematica.skills.subtraction import Subtraction
from mathematica.skills.multiplication import Multiplication
from mathematica.skills.division import Division


class SelectSkill(tk.Frame):
    """
    A frame component class which provides a frame for user to select maths skill to practice.

    The user can either select from one of the four skills or can quit the program.
    """

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        # Initialize this component as a frame component inside the parent component.
        tk.Frame.__init__(self, parent)

        # Release any enter key bindings to prevent unexpected behaviours.
        controller.unbind('<Return>')

        # ====== Components ======
        header_label = tk.Label(self, font=HEADER_FONT, text="Please select the mathematical skill to learn.")
        header_label.pack(pady=(15, 20))

        addition_button = tk.Button(self, width=13, height=2, text="Addition", font=BUTTON_FONT,
                                    command=lambda event=None: controller.show_frame(Addition))
        addition_button.pack(pady=2)
        subtraction_button = tk.Button(self, width=13, height=2, text="Subtraction", font=BUTTON_FONT,
                                       command=lambda event=None: controller.show_frame(Subtraction))
        subtraction_button.pack(pady=2)
        multiplication_button = tk.Button(self, width=13, height=2, text="Multiplication", font=BUTTON_FONT,
                                          command=lambda event=None: controller.show_frame(Multiplication))
        multiplication_button.pack(pady=2)
        division_button = tk.Button(self, width=13, height=2, text="Division", font=BUTTON_FONT,
                                    command=lambda event=None: controller.show_frame(Division))
        division_button.pack(pady=2)

        quit_button = tk.Button(self, width=10, height=2, text="Quit", font=BUTTON_FONT,
                                command=controller.destroy)
        quit_button.pack(pady=(15, 0))
        # ====== Components End ======
