class Person:
    """
    A class used to create an instance (person) everytime the save button is clicked. Used for testing purposes.
    """
    def __init__(self, name, age, email, position, language) -> None:
        """
        Constructor assigns attributes to each instance (person) of the class corresponding to the input of the GUI.
        param name: Name of person
        :param age: Person Age
        :param email: Person Email
        :param position: Person position (student, staff, or both)
        :param language: Languages the person knows
        """
        self.__name = name
        self.__age = age
        self.set_age(self.__age)
        self.__email = email
        self.__position = position
        self.__language = language

    def get_name(self) -> str:
        """
        Method to get the value of self.__name
        :return: str
        """
        return self.__name

    def get_age(self) -> int:
        """
        Method to get the value of self.__age
        :return: int
        """
        return self.__age

    def get_email(self) -> str:
        """
        Method to get the value of self.__email
        :return: str
        """
        return self.__email

    def get_position(self) -> str:
        """
        Method to get the value of self.__position
        :return: str
        """
        return self.__position

    def get_language(self) -> list:
        """
        Method to get the value of self.__language
        :return: list
        """
        return self.__language

    def set_age(self, age) -> None:
        """
        Method to set the age to 0 if a negative value is entered
        :param age: int
        :return: None
        """
        if age < 0:
            self.__age = 0

    def __str__(self) -> str:
        """
        Method to print out the attributes of each person (instance)
        :return: String value of all the attributes
        """
        return f'Name : {self.__name}, Age : {self.__age}, Email : {self.__email}, Position : {self.__position}, Language(s) : {self.__language}'
