import tkinter as tk

from mathematica.utilities.fonts import *

global window


def alert_dialog(title: str, header: str, body: str, ok_button_action):
    global window
    window = tk.Tk()
    window.resizable(False, False)
    window.title(title)

    container = tk.Frame(window)
    container.pack(side="top", fill="both", expand=True, padx=(10, 10), pady=(10, 10))

    header = tk.Label(container, font=HEADER_FONT, text=header)
    header.pack(pady=(10, 5))

    label = tk.Label(container, font=LABEL_FONT, text=body)
    label.pack(pady=(0, 10))

    ok_button = tk.Button(container, font=BUTTON_FONT, width=10, height=2, text="Ok",
                          command=ok_button_action)
    ok_button.pack(side="right", padx=(0, 15), pady=(0, 0))

    window.bind('<Return>', lambda event=None: ok_button.invoke())

    # Update window information status
    window.update_idletasks()
    # Make window invisible
    window.withdraw()
    # Calculate start points of the position where the pop-up window should be positioned.
    start_x = int((window.winfo_screenwidth() / 2) - (window.winfo_width() / 2))
    start_y = int((window.winfo_screenheight() / 2) - (window.winfo_height() / 2))
    # Place the window in the center of the screen.
    window.geometry("+{}+{}".format(start_x, start_y))
    # Make window visible
    window.deiconify()

    window.mainloop()


def destroy_dialog():
    window.destroy()
