import tkinter as tk

import mathematica.skills.question as question
from mathematica.main_menu import select_skill
from mathematica.skills.skills_list import Skills
from mathematica.utilities.fonts import *


class Subtraction(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        header = tk.Label(self, font=HEADER_FONT, text="Let's learn Subtraction!")
        header.pack(pady=(15, 10))

        info_label = tk.Label(self, font=LABEL_FONT,
                              text="""Subtraction is when you takeaway one number from another.
For example: 6 - 3 = 3 as we are taking away 3 from 6.

Remember: Subtraction can result in NEGATIVE numbers!
For example: 2 - 7 = -5 as we are taking away 7 from 2.

Let's practice some subtraction questions!""")
        info_label.pack(pady=(5, 20))

        button_frame = tk.Frame(self)
        back_to_main_button = tk.Button(button_frame, width=13, height=2, text="Back to Main", font=BUTTON_FONT,
                                        command=lambda event=None: controller.show_frame(select_skill.SelectSkill))
        back_to_main_button.grid(row=0, column=0, padx=(0, 5))
        ok_button = tk.Button(button_frame, width=13, height=2, text="Ok", font=BUTTON_FONT,
                              command=lambda event=None: ask_question(controller))
        ok_button.grid(row=0, column=1, padx=(5, 0))
        button_frame.pack()

        # Allows the user to press enter and and open selectSkill module.
        controller.bind('<Return>', lambda event=None: ok_button.invoke())


def ask_question(controller):
    question.operator = Skills.SUBTRACTION
    controller.show_frame(question.Question)
