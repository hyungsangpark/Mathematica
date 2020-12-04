# This class initiates the quiz application window and passes it to different applications.
import sys
from tkinter import Tk
from mathematica import main_menu

# Global constants related to game window.
WINDOW_TITLE = "Mathematica"
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 160

# Generate window to be used with this program.
# global window
window = Tk()
window.title(WINDOW_TITLE)  # Sets the title of the window as predefined value of "title".
window.resizable(False, False)

# Defines the starting point of the window. With following code,
start_x = int((window.winfo_screenwidth() / 2) - (WINDOW_WIDTH / 2))
# the starting point of the window is automatically set so that the window will be at the center of the screen.
start_y = int((window.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2))

# Places the window in the center of the screen.
window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, start_x, start_y))

# Start Point of the program.
main_menu.greetUser(window)


# Functions related to window
def close_window():
    window.destroy()
    sys.exit()


def blankSpace():       #Adds a blank space in the window.
    Label(window).pack()