#This is a modification of Lab 10

from tkinter import *

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
        self.frame_name.pack(anchor='w', pady=10) # anchor='w' helps to change the frame position from center to west.

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
        self.status.set(None)
        self.radio_student = Radiobutton(self.frame_status, text = 'Student', variable = self.status, value = 0)
        self.radio_staff = Radiobutton(self.frame_status, text = 'Staff', variable = self.status, value = 1)
        self.radio_both = Radiobutton(self.frame_status, text = 'Both', variable = self.status, value = 2)
        self.label_status.pack(padx=5, side='left')
        self.radio_student.pack (side = 'left')
        self.radio_staff.pack (side = 'left')
        self.radio_both.pack (side = 'left')
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
        name = self.entry_name.get()
        age = int(self.entry_age.get())
        email = self.entry_email.get()

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

        info = [name, age, email, position, language]

        #fieldnames = ['Name', 'Age', 'Email', 'Position', 'Languages']

        with open('records.csv', 'a', newline='') as csvfile:
            #csvfile.writerow(fieldnames)
            records = csv.writer(csvfile)
            records.writerow(info)

        person_1 = Person(name, age, email, position, language)
        person_1.__str__()

        self.entry_name.delete(0, END)
        self.entry_age.delete(0, END)
        self.entry_email.delete(0, END)
        self.status.set(None)
        self.check_python.deselect()
        self.check_c.deselect()
        self.check_java.deselect()
        self.check_pearl.deselect()

class Person:
    '''
    A class used to create an instance (person) everytime the save button is clicked. Used for testing purposes.
    '''
    def __init__(self, name, age, email, position, language) -> None:
        '''
        Constructor assigns attributes to each instance (person) of the class corresponding to the input of the GUI.
        :param name: Name of person
        :param age: Person Age
        :param email: Person Email
        :param position: Person position (student, staff, or both)
        :param language: Languages the person knows
        '''
        self.name = name
        self.age = age
        self.email = email
        self.position = position
        self.language = language

    def __str__(self) -> string:
        '''
        Method to print out the attributes of each person (instance)
        :return: String value of all the atrributes
        '''
        return f'Name : {self.name}, Age : {self.age}, Email : {self.email}, Position : {self.position}, Language(s) : {self.language}'

