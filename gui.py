# This is a modification of Lab 10

from tkinter import *
from person1 import *
import csv


class GUI:
    """
    A class used to create elements in a GUI using tkinter and sending the data collected to csv file
    """
    def __init__(self, window) -> None:
        """
        Constructor to create labels and entry boxes for the name, age, and email of the user.
        Creates radio buttons for the users position and favorite coding language
        """
        self.window = window

        # Name entry box
        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=11, side='left')
        self.frame_name.pack(anchor='w', pady=10)

        # Age entry box
        self.frame_age = Frame(self.window)
        self.label_age = Label(self.frame_age, text='Age')
        self.entry_age = Entry(self.frame_age)
        self.label_age.pack(padx=5, side='left')
        self.entry_age.pack(padx=22, side='left')
        self.frame_age.pack(anchor='w', pady=10)

        # Email entry box
        self.frame_email = Frame(self.window)
        self.label_email = Label(self.frame_email, text='Email')
        self.entry_email = Entry(self.frame_email)
        self.label_email.pack(padx=5, side='left')
        self.entry_email.pack(padx=15, side='left')
        self.frame_email.pack(anchor='w', pady=10)

        # Position / status radio buttons
        self.frame_status = Frame(self.window)
        self.label_status = Label(self.frame_status, text='Position')
        self.status = IntVar()

        # self.status.set(None)
        self.radio_student = Radiobutton(self.frame_status, text='Student', variable=self.status, value=0)
        self.radio_staff = Radiobutton(self.frame_status, text='Staff', variable=self.status, value=1)
        self.radio_both = Radiobutton(self.frame_status, text='Both', variable=self.status, value=2)
        self.label_status.pack(padx=5, side='left')
        self.radio_student.pack(side='left')
        self.radio_staff.pack(side='left')
        self.radio_both.pack(side='left')
        self.frame_status.pack(anchor='w', pady=10)

        # Coding language check buttons
        self.frame_lan = Frame(self.window)
        self.label_lan = Label(self.frame_lan, text='Coding Languages')
        self.p_var = IntVar()
        self.c_var = IntVar()
        self.j_var = IntVar()
        self.pearl_var = IntVar()
        self.check_python = Checkbutton(self.frame_lan, text='Python', variable=self.p_var)
        self.check_c = Checkbutton(self.frame_lan, text='C++', variable=self.c_var)
        self.check_java = Checkbutton(self.frame_lan, text='Java', variable=self.j_var)
        self.check_pearl = Checkbutton(self.frame_lan, text='Pearl', variable=self.pearl_var)
        self.label_lan.pack(padx=5, side='left')
        self.check_python.pack(side='left')
        self.check_c.pack(side='left')
        self.check_java.pack(side='left')
        self.check_pearl.pack(side='left')
        self.frame_lan.pack(anchor='w', pady=10)

        # Error Label
        self.frame_error = Frame(self.window)
        self.label_error = Label(self.frame_error, text='')
        self.label_error.pack()
        self.frame_error.pack()

        # Save button
        self.frame_button = Frame(self.window)
        self.save_button = Button(self.frame_button, text='SAVE', command=self.clicked)
        self.save_button.pack()
        self.frame_button.pack()

    def clicked(self) -> None:
        """
        Method, when the save button is clicked, to retrieve the name, age, email, position,
        and favorite language of the user. Then, send the data to a csv file. Rests the entry boxes and radio buttons.
        :return: The name, age, email, position, and favorite language
        """
        try:
            name = self.entry_name.get()
            if len(name) <= 0:
                raise TypeError('Name should have a value')

            age = self.entry_age.get()
            if len(age) <= 0:
                raise TypeError('Age should have a value')
            age = int(age)

            email = self.entry_email.get()
            if len(email) <= 0:
                raise TypeError('Email should have a value')

            if self.status.get() == 0:
                position = 'Student'
            elif self.status.get() == 1:
                position = 'Staff'
            else:
                position = 'Both'

            language = []
            if self.p_var.get() == 1:
                language.append('Python')
            if self.j_var.get() == 1:
                language.append('Java')
            if self.c_var.get() == 1:
                language.append('C++')
            if self.pearl_var.get() == 1:
                language.append('Pearl')

            person_1 = Person(name, age, email, position, language)

            info = [person_1.get_name(), person_1.get_age(), person_1.get_email(), person_1.get_position(), person_1.get_language()]

            with open('records.csv', 'a', newline='') as csvfile:
                records = csv.writer(csvfile)
                records.writerow(info)

            self.entry_name.delete(0, END)
            self.entry_age.delete(0, END)
            self.entry_email.delete(0, END)
            self.status.set(0)
            self.check_python.deselect()
            self.check_c.deselect()
            self.check_java.deselect()
            self.check_pearl.deselect()

        except TypeError as e:
            self.label_error.config(text=f'{e}')
        except ValueError:
            self.label_error.config(text='Age should be integer')
            self.entry_age.delete(0, END)
