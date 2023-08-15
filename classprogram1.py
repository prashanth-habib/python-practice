"""
This program contains a class that accepts a string and returns the uppercase of the string.
"""


class InputOutString:
    """
    This class consists of a constructor, two functions one of which reads a string and other prints it in uppercase.
    """
    def __init__(self, inp_string):
        """
        This is the constructor for the class.
        :param inp_string: The string to be converted to uppercase and printed.
        """
        self.string = inp_string

    def get_string(self):
        """
        This function can be used to read the string from a user.
        :return: none
        """
        self.string = input("Enter the string: ")

    def print_string(self):
        """
        This function prints the uppercase version of the string
        :return: none
        """
        print(self.string.upper())


my_object = InputOutString("bruh")
my_object.print_string()
