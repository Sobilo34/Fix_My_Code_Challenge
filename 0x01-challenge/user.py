#!/usr/bin/python3
"""
User class
"""


class User():
    """
    Represents a user entity with email attribute.
    """

    def __init__(self):
        """
        Initializes a User object with None email.
        """
        self.__email = None

    @property
    def email(self):
        """
        Getter method to retrieve the email attribute.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """
        Setter method to set the email attribute.

        Parameters:
        - value (str): The email value to be set.

        Raises:
        - TypeError: If the provided value is not a string.
        """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
