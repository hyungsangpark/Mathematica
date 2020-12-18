import tkinter as tk

import mathematica.skills.question as question
from mathematica.main_menu import select_skill
from mathematica.skills.skills_list import Skills
from mathematica.utilities.fonts import *


class Division(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        header = tk.Label(self, font=HEADER_FONT, text="Let's learn division!")
        header.pack(pady=(15, 10))

        info_label = tk.Label(self, font=LABEL_FONT,
                              text="""Division is when you break up a number into equal number of parts.
For example: 12 ÷ 4 = 3 as we are breaking up 12 into 4 equal number of parts
which gives 3 per each part.

Let's practice some division questions!""")
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
    question.operator = Skills.DIVISION
    controller.show_frame(question.Question)
