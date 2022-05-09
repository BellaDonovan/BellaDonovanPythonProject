from gui import *


class Test:
    """
    Class used to test the GUI in gui.py
    """
    def setup_method(self) -> None:
        """
        Method used to create a new instance of the class Person.
        :return: None
        """
        self.person_1 = Person('Jane', 16, 'jane@gmail.com', 'Both', '[Python]')
        self.person_2 = Person('Jane', -16, 'jane@gmail.com', 'Both', '[Python]')
        self.person_3 = Person('Jane', 16, 'jane@gmail.com', 'Both', '[]')
        self.person_4 = Person('Jane', 16, 'jane@gmail.com', 'Both', '[Python, Java]')

    def test_gui(self) -> None:
        """
        Test used to check the __str__() method in class Person. Used to test the set_age() function.
        :return: None
        """
        assert self.person_1.__str__() == 'Name : Jane, Age : 16, Email : jane@gmail.com, Position : Both, Language(s) : [Python]'
        assert self.person_2.__str__() == 'Name : Jane, Age : 0, Email : jane@gmail.com, Position : Both, Language(s) : [Python]'
        assert self.person_3.__str__() == 'Name : Jane, Age : 16, Email : jane@gmail.com, Position : Both, Language(s) : []'
        assert self.person_4.__str__() == 'Name : Jane, Age : 16, Email : jane@gmail.com, Position : Both, Language(s) : [Python, Java]'
