from tkinter import Tk
from clock_app import Clock_App

def main() -> None:
    root = Tk()
    app = Clock_App(root)
    app.run()

if __name__ == "__main__":
    main()