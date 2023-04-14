#!/usr/bin/python3
"""
User class Module
"""


class User():
    """User Class Definition"""

    def __init__(self):
        """Initializatin function"""
        self.__email = None

    @property
    def email(self):
        """email getter"""
        return self.__email

    @email.setter
    def email(self, value):
        """email setter"""
        if type(value) is not str or '@' not in value:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
    a = User()
    try:
        a.email = 'mustapha'
        print(a.email)
    except TypeError:
        print('TypeError is raise')
