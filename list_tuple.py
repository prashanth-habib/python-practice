"""
This file contains code to create a list and tuple containing numbers which are given as input from console
which are separated by commas.
"""


def create_list(numbers):
    """
    Takes the numbers separated by commas and creates a list.
    :param numbers: numbers to be converted into a list of numbers
    :return: list of numbers
    """

    num_list = numbers.split(",")
    return num_list


def create_tuple(numbers):
    """
    Creates a tuple of given numbers which are separated by commas
    :param numbers: numbers to be converted into a tuple.
    :return: tuple of numbers
    """
    num_list = numbers.split(",")
    num_tuple = tuple(num_list)
    return num_tuple


nums = input("Enter the numbers separated by commas: ")
print(create_list(nums))
print(create_tuple(nums))
