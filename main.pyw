#----------------------- Imports globally used functions and variables -----------------------#

from tkinter import *   
import random, sys      

title = "Mathematica"       #The title of every window in the program.

labelFont = ("Arial", 14)               #Defines the fonts of the texts or buttons in a window.
buttonFont = ("Arial", 13, "bold")       

okColor = "aquamarine"      #Defines the color of the buttons in a window.
submitColor = "turquoise"   
mainMenuColor = "bisque2"

questionNumber = 10         #Defines the number of questions the users are asked.

#----- Defines extra function that are globally necessary such as exit() or closeWindow()-----#

def exit():     #Closes the window and exits the program (Used in Skill selection window)
    
    window.destroy()                                                                                                                
    sys.exit()

def closeWindow():      #Closes error box opened during question time.

    global win

    win.destroy()

def enterCloseWindow(event):        #Accepts enter keys and runs closeWindow. 

    closeWindow()

def blankSpace():       #Adds a blank space in the window.

    global window

    Label(window).pack()
    
#---------------------------------------- Main Screen ----------------------------------------#

def greetUser():        #Greets users 

    global window, tkinter

    window = Tk()
    window.title(title)     #Sets the title of the window as predefined value of "title". 
    window.resizable(False, False)

    windowWidth = 400       #Defines the size of the window.
    windowHeight = 160

    startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))      #Defines the starting point of the window. With following code, 
    starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))    #the starting point of the window is automatically set so that the window will be at the center of the screen.
    
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))     #Places the window in the center of the screen.
    
    Label(window, height=2, font=labelFont, text="Welcome to Mathematica!").pack()
    Label(window, font=labelFont, text="Let's learn some math skills!").pack()
    
    blankSpace()
    
    Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=selectSkill).pack()

    window.bind("<Return>", openSelectSkill)        #Allows the user to press enter and and open selectSkill module.

    window.mainloop()

def selectSkill():      #Allows users to choose specific math skills or quit the program. Basically a main menu.

    global window, tkinter, correctQuestion

    window.destroy()        #Closes the previous window to allow the next window to open.
    window = Tk()
    window.title(title)
    window.resizable(False, False)

    windowWidth = 400
    windowHeight = 230

    startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
    starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
    
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

    correctQuestion = 0

    Label(window, height=2, font=labelFont, text="Please select the mathematical skill to learn.").pack()
    
    Button(window, width=13, bg="LightBlue1", text="Addition", font=buttonFont, command=learnAddition).pack()
    Button(window, width=13, bg="salmon", text="Subtraction", font=buttonFont, command=learnSubtraction).pack()
    Button(window, width=13, bg="OliveDrab1", text="Multiplication", font=buttonFont, command=learnMultiplication).pack()

    blankSpace()
    
    Button(window, text="Quit", command=exit, width=10, bg="firebrick2", fg="white", font=buttonFont).pack()

    window.mainloop()

def openSelectSkill(event):     #Accepts the event of enter key press and runs selectSkill module. (Or any module that it corresponds to)

    selectSkill()
    
#------------------------------------------ Addition -----------------------------------------#

def learnAddition():        #Opens learning addition window and teaches students what addition is before they are tested.

    global window, tkinter

    window.destroy()
    window = Tk()
    window.title(title)
    window.resizable(False, False)

    windowWidth = 600
    windowHeight = 290

    startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
    starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
    
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

    Label(window, height=2, font=labelFont, text="Let's learn Addition!").pack()

    Label(window, font=labelFont, text="Addition is when you find the total of the two numbers.").pack()
    Label(window, font=labelFont, text="For example: 3 + 2 = 5 as we are finding total of 3 and 2 together.").pack()
    
    
    Label(window, font=labelFont, text="Let's practice some addition questions!").pack()
    
    blankSpace()
    
    Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=tryAddition).pack()
    
    blankSpace()
    
    Button(window, bg=mainMenuColor, text="Back to Main Menu", font=buttonFont, command=selectSkill).pack()
    
    blankSpace()

    window.bind("<Return>", nextAddition)

    window.mainloop()

def nextAddition(event):        #Accepts the event of enter key press and runs tryAddition module to imitate what Ok button in learnAddition window would do.

    tryAddition()

def tryAddition():      #Questions the users and if they have answered certain number of questions, shows a window that congratulates them.

    global window, tkinter, random, answer, correctQuestion, number1, number2

    while correctQuestion != questionNumber:        #Gives question to users until the number of correct questions are identical to the number of questions defined on the top.

        minNumber = 1        #This is the range of the values the numbers in the question generates. Changing this value will affect the numbers in the question.
        maxNumber = 10

        number1 = random.randint (minNumber, maxNumber)     #This generates random number between the range of minNumber and maxNumber and stores them in a variable of number1 and number2.
        number2 = random.randint (minNumber, maxNumber)
    
        window.destroy()
        window = Tk()
        window.title(title)
        window.resizable(False, False)

        windowWidth = 250
        windowHeight = 146

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        Label(window, height=2, font=labelFont, text="What is " + str(number1) + " + " + str(number2) + " ?").pack()

        answer = Entry(window, width=10)
        answer.pack()
        
        blankSpace()

        Button(window, width=10, bg=submitColor, text="Submit", font=buttonFont, command=checkAddition).pack()
        
        blankSpace()

        window.bind("<Return>", openCheckAddition)
        
        window.mainloop()

    if correctQuestion == questionNumber:       #If the user has got same number of correct questions as number of questions that the user has to get it right.

        window.destroy()
        window = Tk()
        window.title(title)
        window.resizable(False, False)

        windowWidth = 450
        windowHeight = 120

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        blankSpace()
        
        Label(window, font=labelFont, text="Good job! Now you know how to do addition!").pack()
        
        blankSpace()

        Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=selectSkill).pack()
        
        blankSpace()

        window.bind("<Return>", openSelectSkill)

        window.mainloop()

def openCheckAddition(event):        #Accepts the event of enter key press and runs checkAddition module to imitate what Ok button in Addition question window would do.

    checkAddition()

def checkAddition():

    global window, tkinter, correctQuestion, win

    userAnswer = answer.get()       #Stores what the user has inputted in the entry box into a variable of userAnswer.
    actualAnswer = number1 + number2        #Calculates what the answer to the question would be.

    try:                                #This is used to validate the input values to integers.
        userAnswer = int(userAnswer)

    except (TypeError, ValueError):     #If any value that is not an integer is inputted, a ValueError or TypeError would occur which is detected here which triggers following codes.

        win = Tk()
        win.title(title)
        win.resizable(False, False)

        windowWidth = 275
        windowHeight = 130

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        win.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        Label(win).pack()
        Label(win, font=labelFont, text="Please enter a valid NUMBER!").pack()
        Label(win).pack()

        Button(win, width=10, bg=okColor, text="Ok", font=buttonFont, command=closeWindow).pack()
        Label(win).pack()

        win.bind("<Return>", enterCloseWindow)

        win.mainloop()

    else:       #If the value is integer.

        if int(userAnswer) == int(actualAnswer):        #If the answer from the user is same with the correct answer.

            window.destroy()        
            window = Tk()
            window.title(title)
            window.resizable(False, False)

            windowWidth = 250
            windowHeight = 146

            startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
            starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
            window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

            blankSpace()
            Label(window, font=labelFont, text="That is correct!").pack()
            Label(window, font=labelFont, text="Keep up the good work.").pack()
            blankSpace()

            Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=tryAddition).pack()
            blankSpace()

            window.bind("<Return>", nextAddition)

            correctQuestion += 1    #Adds one to number of correct question counter so that the question stops as this reaches 10.

            window.mainloop()

        elif int(userAnswer) != int(actualAnswer):      #If the answer from the user is not same with the correct answer.

            window.destroy()
            window = Tk()
            window.title(title)
            window.resizable(False, False)

            windowWidth = 250
            windowHeight = 146

            startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
            starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
            window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))
        
            blankSpace()
            Label(window, font=labelFont, text="Sorry, " + str(number1) + " + " + str(number2) + " = " + str(number1+number2) + ".").pack()
            Label(window, font=labelFont, text="Keep practicing.").pack()
            blankSpace()
        
            Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=tryAddition).pack()
            blankSpace()

            window.bind("<Return>", nextAddition)
        
            window.mainloop()

#---------------------------------------- Subtraction ----------------------------------------#
        
def learnSubtraction():     #Opens learning subtraction window and teaches students what subtraction is before they are tested.

    global window, tkinter

    window.destroy()
    window = Tk()
    window.title(title)
    window.resizable(False, False)

    windowWidth = 600
    windowHeight = 290

    startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
    starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
    
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

    Label(window, height=2, font=labelFont, text="Let's learn subtraction!").pack()

    Label(window, font=labelFont, text="Subtraction is when you takeaway one number from another.").pack()
    Label(window, font=labelFont, text="For example: 6 - 3 = 3 as we are taking away 3 from 6.").pack()
    blankSpace()
    
    Label(window, font=labelFont, text="Let's practice some subtraction questions!").pack()
    blankSpace()
    
    Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=trySubtraction).pack()
    blankSpace()
    Button(window, bg=mainMenuColor, text="Back to Main Menu", font=buttonFont, command=selectSkill).pack()
    blankSpace()

    window.bind("<Return>", nextSubtraction)
    
    window.mainloop()

def nextSubtraction(event):        #Accepts the event of enter key press and runs trySubtraction module to imitate what Ok button in learnSubtraction window would do.

    trySubtraction()

def trySubtraction():      #Questions the users and if they have answered certain number of questions, shows a window that congratulates them.

    global window, tkinter, random, answer, correctQuestion, number1, number2

    while correctQuestion != questionNumber:        #Gives question to users until the number of correct questions are identical to the number of questions defined on the top.

        number1 = 0
        number2 = 0

        while number1 < number2 or number1 == number2:      #This is to reduce difficulty of the calculation as if we leave it as it generates, it can sometimes result a negative number.

            minNumber = 1       #This is the range of the values the numbers in the question generates. Changing this value will affect the numbers in the question.
            maxNumber = 10

            number1 = random.randint (minNumber, maxNumber)     #This generates random number between the range of minNumber and maxNumber and stores them in a variable of number1 and number2.
            number2 = random.randint (minNumber, maxNumber)
    
        window.destroy()
        window = Tk()
        window.title(title)
        window.resizable(False, False)

        windowWidth = 250
        windowHeight = 146

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        Label(window, height=2, font=labelFont, text="What is " + str(number1) + " - " + str(number2) + " ?").pack()

        answer = Entry(window, width=10)
        answer.pack()
        blankSpace()

        Button(window, width=10, bg=submitColor, text="Submit", font=buttonFont, command=checkSubtraction).pack()
        blankSpace()

        window.bind("<Return>", openCheckSubtraction)
        
        window.mainloop()

    if correctQuestion == questionNumber:

        window.destroy()
        window = Tk()
        window.title(title)
        window.resizable(False, False)

        windowWidth = 450
        windowHeight = 120

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        blankSpace()
        Label(window, font=labelFont, text="Good job! Now you know how to do subtraction!").pack()
        blankSpace()

        Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=selectSkill).pack()
        blankSpace()

        window.bind("<Return>", openSelectSkill)

        window.mainloop()

def openCheckSubtraction(event):        #Accepts the event of enter key press and runs checkSubtraction module to imitate what Ok button in Subtraction question window would do.

    checkSubtraction()

def checkSubtraction():

    global window, tkinter, correctQuestion, win

    userAnswer = answer.get()       #Stores what the user has inputted in the entry box into a variable of userAnswer.
    actualAnswer = number1 - number2        #Calculates what the answer to the question would be.

    try:                                #This is used to validate the input values to integers.
        userAnswer = int(userAnswer)

    except (TypeError, ValueError):     #If any value that is not an integer is inputted, a ValueError or TypeError would occur which is detected here which triggers following codes.

        win = Tk()
        win.title(title)
        win.resizable(False, False)

        windowWidth = 275
        windowHeight = 130

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        win.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        Label(win).pack()
        Label(win, font=labelFont, text="Please enter a valid NUMBER!").pack()
        Label(win).pack()

        Button(win, width=10, bg=okColor, text="Ok", font=buttonFont, command=closeWindow).pack()
        Label(win).pack()

        win.bind("<Return>", enterCloseWindow)

        win.mainloop()

    else:       #If the value is integer.

        if int(userAnswer) == int(actualAnswer):        #If the answer from the user is same with the correct answer.

            window.destroy()        
            window = Tk()
            window.title(title)
            window.resizable(False, False)

            windowWidth = 250
            windowHeight = 146

            startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
            starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
            window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

            blankSpace()
            Label(window, font=labelFont, text="That is correct!").pack()
            Label(window, font=labelFont, text="Keep up the good work.").pack()
            blankSpace()

            Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=trySubtraction).pack()
            blankSpace()

            window.bind("<Return>", nextSubtraction)

            correctQuestion += 1    #Adds one to number of correct question counter so that the question stops as this reaches 10.

            window.mainloop()

        elif int(userAnswer) != int(actualAnswer):      #If the answer from the user is not same with the correct answer.

            window.destroy()
            window = Tk()
            window.title(title)
            window.resizable(False, False)

            windowWidth = 250
            windowHeight = 146

            startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
            starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
            window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))
        
            blankSpace()
            Label(window, font=labelFont, text="Sorry, " + str(number1) + " - " + str(number2) + " = " + str(number1-number2) + ".").pack()
            Label(window, font=labelFont, text="Keep practicing.").pack()
            blankSpace()
        
            Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=trySubtraction).pack()
            blankSpace()

            window.bind("<Return>", nextSubtraction)
        
            window.mainloop()
        
#--------------------------------------- Multiplication --------------------------------------#
        
def learnMultiplication():      #Opens learning multiplication window and teaches students what multiplication is before they are tested.

    global window, tkinter

    window.destroy()
    window = Tk()
    window.title(title)
    window.resizable(False, False)

    windowWidth = 700
    windowHeight = 290

    startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
    starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
    
    window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

    Label(window, height=2, font=labelFont, text="Let's learn multiplication!").pack()

    Label(window, font=labelFont, text="Multiplication is when you repeat adding one number by another number times.").pack()
    Label(window, font=labelFont, text="For example: 3 x 2 = 6 as we are adding 3 twice (2).").pack()
    blankSpace()
    
    Label(window, font=labelFont, text="Let's practice some multiplication questions!").pack()
    blankSpace()
    
    Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=tryMultiplication).pack()
    blankSpace()
    Button(window, bg=mainMenuColor, text="Back to Main Menu", font=buttonFont, command=selectSkill).pack()
    blankSpace()

    window.bind("<Return>", nextMultiplication)

    window.mainloop()

def nextMultiplication(event):        #Accepts the event of enter key press and runs tryMultiplication module to imitate what Ok button in learnMultiplication window would do.

    tryMultiplication()

def tryMultiplication():      #Questions the users and if they have answered certain number of questions, shows a window that congratulates them.

    global window, tkinter, random, answer, correctQuestion, number1, number2

    while correctQuestion != questionNumber:        #Gives question to users until the number of correct questions are identical to the number of questions defined on the top.

        minNumber = 1       #This is the range of the values the numbers in the question generates. Changing this value will affect the numbers in the question.
        maxNumber = 10

        number1 = random.randint (minNumber, maxNumber)     #This generates random number between the range of minNumber and maxNumber and stores them in a variable of number1 and number2.
        number2 = random.randint (minNumber, maxNumber)
    
        window.destroy()
        window = Tk()
        window.title(title)
        window.resizable(False, False)

        windowWidth = 250
        windowHeight = 146

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        Label(window, height=2, font=labelFont, text="What is " + str(number1) + " x " + str(number2) + " ?").pack()

        answer = Entry(window, width=10)
        answer.pack()
        blankSpace()

        Button(window, width=10, bg=submitColor, font=buttonFont, text="Submit", command=checkMultiplication).pack()
        blankSpace()

        window.bind("<Return>", openCheckMultiplication)
        
        window.mainloop()

    if correctQuestion == questionNumber:

        window.destroy()
        window = Tk()
        window.title(title)
        window.resizable(False, False)

        windowWidth = 450
        windowHeight = 120

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        blankSpace()
        Label(window, font=labelFont, text="Good job! Now you know how to do multiplication!").pack()
        blankSpace()

        Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=selectSkill).pack()
        blankSpace()

        window.bind("<Return>", openSelectSkill)

        window.mainloop()

def openCheckMultiplication(event):        #Accepts the event of enter key press and runs checkMultiplication module to imitate what Ok button in Multiplication question window would do.

    checkMultiplication()

def checkMultiplication():      #Stores what the user has inputted in the entry box into a variable of userAnswer.

    global window, tkinter, correctQuestion, win

    userAnswer = answer.get()       #Stores what the user has inputted in the entry box into a variable of userAnswer.
    actualAnswer = number1 * number2        #Calculates what the answer to the question would be.

    try:                                #This is used to validate the input values to integers.
        userAnswer = int(userAnswer)

    except (TypeError, ValueError):     #If any value that is not an integer is inputted, a ValueError or TypeError would occur which is detected here which triggers following codes.

        win = Tk()
        win.title(title)
        win.resizable(False, False)

        windowWidth = 275
        windowHeight = 130

        startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
        starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
        win.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

        Label(win).pack()
        Label(win, font=labelFont, text="Please enter a valid NUMBER!").pack()
        Label(win).pack()

        Button(win, width=10, bg=okColor, text="Ok", font=buttonFont, command=closeWindow).pack()
        Label(win).pack()

        win.bind("<Return>", enterCloseWindow)

        win.mainloop()

    else:       #If the value is integer.

        if int(userAnswer) == int(actualAnswer):        #If the answer from the user is same with the correct answer.

            window.destroy()        
            window = Tk()
            window.title(title)
            window.resizable(False, False)

            windowWidth = 250
            windowHeight = 146

            startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
            starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
            window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))

            blankSpace()
            Label(window, font=labelFont, text="That is correct!").pack()
            Label(window, font=labelFont, text="Keep up the good work.").pack()
            blankSpace()

            Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=tryMultiplication).pack()
            blankSpace()

            window.bind("<Return>", nextMultiplication)

            correctQuestion += 1    #Adds one to number of correct question counter so that the question stops as this reaches 10.

            window.mainloop()

        elif int(userAnswer) != int(actualAnswer):      #If the answer from the user is not same with the correct answer.

            window.destroy()
            window = Tk()
            window.title(title)
            window.resizable(False, False)

            windowWidth = 250
            windowHeight = 146

            startx = int((window.winfo_screenwidth() / 2) - (windowWidth / 2))
            starty = int((window.winfo_screenheight() / 2) - (windowHeight / 2))
        
            window.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, startx, starty))
        
            blankSpace()
            Label(window, font=labelFont, text="Sorry, " + str(number1) + " x " + str(number2) + " = " + str(number1*number2) + ".").pack()
            Label(window, font=labelFont, text="Keep practicing.").pack()
            blankSpace()
        
            Button(window, width=10, bg=okColor, text="Ok", font=buttonFont, command=tryMultiplication).pack()
            blankSpace()

            window.bind("<Return>", nextMultiplication)
        
            window.mainloop()
 
#------------------------------------------- Start -------------------------------------------#

greetUser()     #Start of the program.
