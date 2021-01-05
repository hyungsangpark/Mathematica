import random
import tkinter as tk

from mathematica.main_menu import select_skill
from mathematica.utilities.fonts import *
from mathematica.skills.skills_list import Skills
import mathematica.utilities.pop_up_window as pop_up

# Global variables used throughout multiple instances of Question class below.
global math_skill, questions_correct
# Initialize questions_solved indicating 0 questions have been solved.
questions_correct = 0


class Question(tk.Frame):
    """
    A frame component class which provides a question frame that asks the user a question of specified math skill.

    The user can enter an answer to the question in the answer field and submit the answer.

    If the answer is correct, a pop up will congratulate the user that the answer is correct,
    if the answer is incorrect, a pop up will notify the user that the answer is incorrect and will tell the correct
    answer,
    and if the answer is not an integer, a pop up will notify the user to enter a correct type of answer.
    (possibly require a teacher assistant if the student can't understand the pop up message.)
    """

    def __init__(self, parent: tk.Frame, controller: tk.Tk):
        # Initialize this component as a frame component inside the parent component.
        tk.Frame.__init__(self, parent)

        self.controller = controller

        # Generate two random integers to generate questions.
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)

        # If current skill type is division, make answer = num1 / num2.
        if math_skill == Skills.DIVISION:
            self.num1 *= self.num2

        self.answer = math_skill.value["function"](self.num1, self.num2)

        self.setup_question_components()

    def setup_question_components(self) -> None:
        """
        sets up components inside the question such as question label or the answer field.
        """
        question_label = tk.Label(self, font=HEADER_FONT,
                                  text="What is {} {} {}?".format(self.num1, math_skill.value["operator"], self.num2))
        question_label.pack(pady=(15, 10))

        # Horizontal area for answer field and submit button.
        answer_frame = tk.Frame(self)

        answer_field = tk.Entry(answer_frame, width=10)
        answer_field.grid(row=0, column=0, padx=(0, 5))
        answer_field.focus_set()

        submit_button = tk.Button(answer_frame, width=13, height=2, text="Submit", font=BUTTON_FONT,
                                  command=lambda event=None: self.check_answer(answer_field))
        submit_button.grid(row=0, column=1, padx=(5, 0))

        answer_frame.pack(pady=(10, 0))

        # Allows the user to press enter and and open selectSkill module.
        self.controller.bind('<Return>', lambda event=None: submit_button.invoke())

    def check_answer(self, answer_field: tk.Entry) -> None:
        """
        Checks the answer in the answer field given, and creates an according pop up.

        If the answer is correct, the pop up will congratulate the user.
        If the answer is incorrect, the pop up will tell the user the correct answer.
        If the answer is not an integer, the pop up will tell the user to enter a valid answer; integer.

        :param answer_field: The answer field that the user types the answer in.
        """
        user_answer = answer_field.get()

        try:
            # Checks if the answer is an integer, if not, ValueError will be raised.
            user_answer = int(user_answer)

            if user_answer == self.answer:
                def increment_question_num() -> None:
                    """
                    Increments counter for number of correct questions.
                    """
                    global questions_correct
                    questions_correct += 1

                pop_up.alert_dialog(title="Correct!",
                                    header="That is correct!",
                                    body="Keep up the good work!",
                                    action=lambda event=None: [pop_up.destroy_dialog(),
                                                               increment_question_num(),
                                                               self.check_ten_questions_correct()])
            else:
                pop_up.alert_dialog(title="Incorrect...",
                                    header="The answer is incorrect",
                                    body="Sorry, {} {} {} = {}.\n"
                                         "Let's keep practicing!"
                                         .format(self.num1, math_skill.value["operator"], self.num2, self.answer),
                                    action=lambda event=None: [pop_up.destroy_dialog(),
                                                               self.check_ten_questions_correct()])
        except ValueError:
            body_text = "An integer is basically a whole number that is either negative or positive.\n" \
                        "eg. numbers like 23, -12, or 0 but not %s" % user_answer

            try:
                float(user_answer)
            except ValueError:
                body_text += "\n\n(Yes, I can see you bashing random keys right there...)"

            pop_up.alert_dialog(title="Warning!",
                                header="Please enter an integer.",
                                body=body_text)

    def check_ten_questions_correct(self) -> None:
        """
        Checks whether 10 questions have been correctly answered, where if so, ends current set of questions.

        If 10 questions has been correctly answered, a pop up will be created congratulating the user,
        then the application window will change to main menu; the select skill frame.
        """
        global questions_correct
        if questions_correct >= 10:
            questions_correct = 0

            pop_up.alert_dialog(title="Congratulation!",
                                header="Congratulations!",
                                body="You have completed current skill.\n"
                                     "You will now be directed to main menu.",
                                action=lambda event=None: [pop_up.destroy_dialog(),
                                                           self.controller.show_frame(select_skill.SelectSkill)])
        else:
            # If not, simply show another question.
            self.controller.show_frame(Question)
