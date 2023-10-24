from time import strftime
from tkinter import Label, Tk

class Clock_App:
    def __init__(self, root: Tk) -> None:
        """
        Initializes the ClockApp.

        Args:
            root (Tk): The Tkinter root window.
        """
        self.root = root
        self.root.title("")
        self.root.geometry("400x250")
        self.root.configure(bg="black", border=4)
        self.root.resizable(False, False)

        self.clock_label = Label(
            self.root, bg="black", fg="red", font=("Times", 30, 'bold'), relief='flat'
        )
        self.clock_label.place(x=20, y=20)

    def update_label(self) -> None:
        """
        Updates the clock label with the current time.
        """
        current_time = strftime('%H: %M: %S')
        self.clock_label.configure(text=current_time)
        self.clock_label.after(80, self.update_label)

    def run(self) -> None:
        """
        Runs the ClockApp, updating the clock label and starting the mainloop.
        """
        self.update_label()
        self.root.mainloop()