from gui import *


def main():
    """
    - Change the window title to 'Lab 10'.
    - Set its length to 250 and height to 180.
    - Make the window non-resizable.
    """
    window = Tk()
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
