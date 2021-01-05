import tkinter as tk

import mathematica.skills.question as question
from mathematica.main_menu import select_skill
from mathematica.skills.skills_list import Skills
from mathematica.utilities.fonts import *


class Addition(tk.Frame):
    """
    A frame component class which provides an intermediate frame that introduces user to addition and begins addition
    questions.

    The user can either press ok to start answering addition questions, or can press "Back to Main" button
    to return to the main menu.
    """

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        # Initialize this component as a frame component inside the parent component.
        tk.Frame.__init__(self, parent)

        # ====== Components ======
        header = tk.Label(self, font=HEADER_FONT, text="Let's learn Addition!")
        header.pack(pady=(15, 10))

        info_label = tk.Label(self, font=LABEL_FONT,
                              text="Addition is when you find the total of the two numbers.\n"
                                   "For example: 3 + 2 = 5 as we are finding total of 3 and 2 together.\n\n"
                                   
                                   "Let's practice some addition questions!")
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
    Sets current math skill to be addition, and displays an addition question.

    :param controller: The controller of the application window; essentially tkinter.Tk root instance.
    """
    question.math_skill = Skills.ADDITION
    controller.show_frame(question.Question)
