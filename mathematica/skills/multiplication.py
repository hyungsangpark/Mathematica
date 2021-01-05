import tkinter as tk

import mathematica.skills.question as question
from mathematica.main_menu import select_skill
from mathematica.skills.skills_list import Skills
from mathematica.utilities.fonts import *


class Multiplication(tk.Frame):
    """
    A frame component class which provides an intermediate frame that introduces user to multiplication and begins
    multiplication questions.

    The user can either press ok to start answering multiplication questions, or can press "Back to Main" button
    to return to the main menu.
    """

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        # Initialize this component as a frame component inside the parent component.
        tk.Frame.__init__(self, parent)

        # ====== Components ======
        header = tk.Label(self, font=HEADER_FONT, text="Let's learn Multiplication!")
        header.pack(pady=(15, 10))

        info_label = tk.Label(self, font=LABEL_FONT,
                              text='Multiplication is when you repeat adding one number by "another number" times.\n'
                                   "For example: 3 × 2 = 6 as we are adding 3 twice (2 times)\n\n"
                                   
                                   "Let's practice some multiplication questions!")
        info_label.pack(pady=(5, 20))

        # Horizontal area for two buttons.
        button_frame = tk.Frame(self)

        back_to_main_button = tk.Button(button_frame, width=13, height=2, text="Back to Main", font=BUTTON_FONT,
                                        command=lambda event=None: controller.show_frame(select_skill.SelectSkill))
        back_to_main_button.grid(row=0, column=0, padx=(0, 5))

        ok_button = tk.Button(button_frame, width=13, height=2, text="Ok", font=BUTTON_FONT,
                              command=lambda event=None: show_question(controller))
        ok_button.grid(row=0, column=1, padx=(5, 0))

        button_frame.pack()
        # ====== Components End ======

        # Allows the user to press enter and and open selectSkill module.
        controller.bind('<Return>', lambda event=None: ok_button.invoke())


def show_question(controller: tk.Tk) -> None:
    """
    Sets current math skill to be multiplication, and displays a multiplication question.

    :param controller: The controller of the application window; essentially tkinter.Tk root instance.
    """
    question.math_skill = Skills.MULTIPLICATION
    controller.show_frame(question.Question)
