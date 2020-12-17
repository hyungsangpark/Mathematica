import tkinter as tk

import mathematica.skills.question as question
from mathematica.main_menu import select_skill
from mathematica.skills.skills_list import Skills
from mathematica.utilities.fonts import *


class Addition(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        header = tk.Label(self, font=HEADER_FONT, text="Let's learn addition!")
        header.pack(pady=(15, 10))

        info_label = tk.Label(self, font=LABEL_FONT,
                              text="""Addition is when you find the total of the two numbers.
        For example: 3 + 2 = 5 as we are finding total of 3 and 2 together.
        Let's practice some addition questions!""")
        info_label.pack(pady=(5, 10))

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
    question.operator = Skills.ADDITION
    controller.show_frame(question.Question)
