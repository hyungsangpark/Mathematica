from tkinter import Button, Label

from mathematica import learn
from mathematica.main import LABEL_FONT, BUTTON_FONT, blank_space, empty_window
# from mathematica.main import OK_COLOR


# Greets users
def greet_user(window):
    Label(window, height=2, font=LABEL_FONT, text="Welcome to Mathematica!").pack()
    Label(window, font=LABEL_FONT, text="Let's learn some math skills!").pack()

    blank_space(window)

    Button(window, width=10, text="Ok", font=BUTTON_FONT, command=select_skill).pack()

    # Allows the user to press enter and and open selectSkill module.
    window.bind("<Return>", open_select_skill(window))

    window.mainloop()


# Allows users to choose specific math skills or quit the program. Basically a main menu.
def select_skill(window):
    empty_window(window.frame)

    Label(window, height=2, font=LABEL_FONT, text="Please select the mathematical skill to learn.").pack()

    Button(window, width=13, bg="LightBlue1", text="Addition", font=BUTTON_FONT, command=learn.addition()).pack()
    Button(window, width=13, bg="salmon", text="Subtraction", font=BUTTON_FONT, command=learn.subtraction()).pack()
    Button(window, width=13, bg="OliveDrab1", text="Multiplication", font=BUTTON_FONT, command=learn.multiplication()).pack()

    blank_space(window)

    Button(window, text="Quit", command=exit, width=10, bg="firebrick2", fg="white", font=BUTTON_FONT).pack()


# Accepts the event of enter key press and runs selectSkill module. (Or any module that it corresponds to)
def open_select_skill(event, window):
    select_skill(window)