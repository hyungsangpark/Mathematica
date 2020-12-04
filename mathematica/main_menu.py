from tkinter import Label
from tkinter import Button

labelFont = ("Arial", 14)


def greetUser(window):  # Greets users

    Label(window, height=2, font=labelFont, text="Welcome to Mathematica!").pack()
    Label(window, font=labelFont, text="Let's learn some math skills!").pack()

    blankSpace()

    Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=selectSkill).pack()

    window.bind("<Return>", openSelectSkill)  # Allows the user to press enter and and open selectSkill module.

    window.mainloop()
