"""
This file contains the code to create a dictionary of numbers containing integer and its square.
"""


def create_dict(num: int):
    """
    Creates a dictionary containing integer and its square as key-pair.
    :param num: number till which the square has to be calculated.
    :return: A dictionary containing integer and square of the integer.
    """
    sq_dict = dict()
    for i in range(1, num + 1):
        sq_dict[i] = i * i
    return sq_dict

print(create_dict(8))