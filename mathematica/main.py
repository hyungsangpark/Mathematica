import os
import sys
import tkinter as tk

# allows local modules to be imported without error.
file_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(file_dir, '..'))

from main_menu import welcome


class Mathematica(tk.Tk):
    """
    A root class for tkinter window.
    It provides a window where the program can be displayed.
    """

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Title of the application; Mathematica
        self.title("Mathematica")

        # Makes app window non-resizable.
        self.resizable(False, False)

        # Defines the size of the window.
        window_width = 600
        window_height = 400

        # Defines the starting point of the window. With following code, the starting point of the window
        # is automatically set so that the window will be at the center of the screen.
        start_x = int((self.winfo_screenwidth() / 2) - (window_width / 2))
        start_y = int((self.winfo_screenheight() / 2) - (window_height / 2))

        # Places the window in the center of the screen.
        self.geometry("{}x{}+{}+{}".format(window_width, window_height, start_x, start_y))

        # The main container (tk.Frame) which will hold every subsequent components in the window.
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # List of frames that will be displayed in this window.
        self.frames = {}

        self.show_frame(welcome.Welcome)

    def show_frame(self, frame_to_show) -> None:
        """
        Receives a frame component to be displayed

        :param frame_to_show: A name of the frame to show.
        """
        if frame_to_show not in self.frames:
            frame = frame_to_show(self.container, self)
            self.frames[frame_to_show.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        frame = self.frames[frame_to_show.__name__]
        frame.tkraise()


# Starting point of the program.
app = Mathematica()
app.mainloop()
