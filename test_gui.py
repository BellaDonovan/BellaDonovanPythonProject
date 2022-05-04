from person import *

class Test:
    def setup_method(self):
        self.P1 = Person(name, age, email, position, language)

    def test_gui(self):
        assert self.P1.__str__() == ''

