from gui import *


def main() -> None:
    """
    Creates the GUI window, sets its size, disables window resizing, and changed the title of the window.
    :return: tkinter window
    """
    window = Tk()
    window.title('Project 1')
    window.geometry('400x300')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
