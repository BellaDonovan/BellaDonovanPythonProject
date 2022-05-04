from gui import *

class Person:
    def __init__(self, name, age, email, position, language):
        self.name = name
        self.age = age
        self.email = email
        self.position = position
        self.lan = language

    def __str__(self):
        return f'Name = {self.name}, Age = {self.age}, Email = {self.email}, Position = {self.position}, Coding Languages = {self.lan}.'