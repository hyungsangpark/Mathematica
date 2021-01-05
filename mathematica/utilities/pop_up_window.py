import tkinter as tk

from mathematica.utilities.fonts import *

global window


def alert_dialog(title: str, header: str, body: str, action=lambda event=None: destroy_dialog()) -> None:
    """
    A utility window that displays an alert dialog with the given texts.

    :param title: The title of the alert dialog. (In the top bar of the window)
    :param header: The header of the alert dialog. (Inside the content area of the window, above other contents)
    :param body: The body of the alert dialog. (Inside the content area of the window, below header and above OK button)
    :param action: The action the OK button result in. Default is set to close the alert dialog, but when adding
                   custom actions, make sure to follow the format of `lambda event=None: [*actions to be taken*]`, and
                   add internal function destroy_dialog() in the very first element of the list of actions to be taken.
    """
    global window
    window = tk.Tk()
    window.resizable(False, False)
    window.title(title)

    # ====== Components ======
    container = tk.Frame(window)
    container.pack(side="top", fill="both", expand=True, padx=(10, 10), pady=(10, 10))

    header = tk.Label(container, font=HEADER_FONT, text=header)
    header.pack(pady=(10, 5))

    label = tk.Label(container, font=LABEL_FONT, text=body)
    label.pack(pady=(0, 10))

    ok_button = tk.Button(container, font=BUTTON_FONT, width=10, height=2, text="Ok",
                          command=action)
    ok_button.pack(side="right", padx=(0, 15), pady=(0, 0))

    # Bind enter key to trigger OK button.
    window.bind('<Return>', lambda event=None: ok_button.invoke())

    # Update information of the current window, such as window dimensions.
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
    # Disable any other windows from being selected(highlighted).
    window.grab_set()

    window.mainloop()


def destroy_dialog() -> None:
    """
    Destroys the alert dialog created.
    """
    # Re-enable other windows to be selectable.
    window.grab_release()
    # Destroy the window.
    window.destroy()
