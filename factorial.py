"""
This code is for calculating the factorial of a number.
"""


def factorial(num: int):
    """
    This function calculates the factorial of a number.
    :param num: The number whose factorial is to be calculated.
    :return: Factorial of the given number.
    """
    prod = 1
    for i in range(1, num + 1):
        prod *= i
    return prod

print(factorial(3))