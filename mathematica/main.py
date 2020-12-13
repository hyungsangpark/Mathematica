import tkinter as tk

from mathematica import select_skill
from fonts import *


class Mathematica(tk.Tk):

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

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.show_frame(Welcome)

    def show_frame(self, frame_to_show):
        if frame_to_show not in self.frames:
            frame = frame_to_show(self.container)
            self.frames[frame_to_show.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        frame = self.frames[frame_to_show.__name__]
        frame.tkraise()

    #
    # def add_frame(self, frame_to_add):
    #     frame = frame_to_add(self.container)
    #     self.frames[frame_to_add.__name__] = frame
    #     frame.grid(row=0, column=0, sticky="nsew")


class Welcome(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        welcome_header = tk.Label(self, text="Welcome to Mathematica!", font=HEADER_FONT)
        welcome_header.pack(pady=(15, 10))
        welcome_label = tk.Label(self, text="Let's learn some math skills!", font=LABEL_FONT)
        welcome_label.pack(pady=(5, 5))

        tk.Label(self).pack()

        ok_button = tk.Button(self, width=10, height=2, text="Ok", font=BUTTON_FONT,
                              command=lambda: app.show_frame(select_skill.SelectSkill))
        ok_button.pack()

        # Allows the user to press enter and and open selectSkill module.
        ok_button.bind('<Return>', lambda event=None: ok_button.invoke())


app = Mathematica()
app.mainloop()


def show_frame(frame):
    app.show_frame(frame)