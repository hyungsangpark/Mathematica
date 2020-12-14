import tkinter as tk

from mathematica.main_menu import welcome


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

        self.show_frame(welcome.Welcome)

    def show_frame(self, frame_to_show):
        if frame_to_show not in self.frames:
            frame = frame_to_show(self.container, self)
            self.frames[frame_to_show.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        frame = self.frames[frame_to_show.__name__]
        frame.tkraise()


app = Mathematica()
app.mainloop()
