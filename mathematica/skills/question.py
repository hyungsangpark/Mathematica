import random
import tkinter as tk

from mathematica.main_menu import select_skill
from mathematica.utilities.fonts import *
from mathematica.skills.skills_list import Skills
import mathematica.utilities.pop_up_window as pop_up

global operator, question_num
question_num = 0


class Question(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller

        self.num1 = random.randint(1, 11)
        self.num2 = random.randint(1, 11)

        if operator == Skills.DIVISION:
            self.num1 *= self.num2

        self.answer = operator.value[1](self.num1, self.num2)

        self.answer_field = None
        self.ask_question(parent)

    def ask_question(self, parent):
        tk.Frame.__init__(self, parent)

        info_label = tk.Label(self, font=HEADER_FONT,
                              text="What is {} {} {}?".format(self.num1, operator.value[0], self.num2))
        info_label.pack(pady=(15, 10))

        answer_frame = tk.Frame(self)

        self.answer_field = tk.Entry(answer_frame, width=10)
        self.answer_field.grid(row=0, column=0, padx=(0, 5))
        self.answer_field.focus_set()
        submit_button = tk.Button(answer_frame, width=13, height=2, text="Submit", font=BUTTON_FONT,
                                  command=lambda event=None: self.check_answer())
        submit_button.grid(row=0, column=1, padx=(5, 0))
        answer_frame.pack(pady=(10, 0))

        # Allows the user to press enter and and open selectSkill module.
        self.controller.bind('<Return>', lambda event=None: submit_button.invoke())

    def check_answer(self):
        user_answer = self.answer_field.get()

        try:
            user_answer = int(user_answer)
        except (TypeError, ValueError):
            pop_up.alert_dialog("Warning!",
                                "Please enter a whole number.",
                                "A whole number is a number without any special math thing in it.\n"
                                "(eg. numbers like 23, 1, 83 Not 82.2)",
                                lambda event=None: pop_up.destroy_dialog())
        else:
            if user_answer == self.answer:
                def increment_question_num():
                    global question_num
                    question_num += 1

                pop_up.alert_dialog("Correct!",
                                    "That is correct!",
                                    "Keep up the good work!",
                                    lambda event=None: [increment_question_num(),
                                                        pop_up.destroy_dialog(),
                                                        self.check_ten_questions_answered()])
            else:
                pop_up.alert_dialog("Incorrect...",
                                    "The answer is incorrect",
                                    "Sorry, {} {} {} = {}.\n"
                                    "Let's keep practicing!"
                                    .format(self.num1, operator.value[0], self.num2, self.answer),
                                    lambda event=None: [pop_up.destroy_dialog(),
                                                        self.check_ten_questions_answered()])

    def check_ten_questions_answered(self):
        global question_num
        if question_num >= 10:
            question_num = 0

            pop_up.alert_dialog("Congratulation!",
                                "Congratulations!",
                                "You have completed current skill.\n"
                                "You will now be directed to main menu.",
                                lambda event=None: [pop_up.destroy_dialog(),
                                                    self.controller.show_frame(select_skill.SelectSkill)])
        else:
            self.controller.show_frame(Question)
