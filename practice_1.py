"""
This file contains the solution to finding out whether the given number is divisible by 7 but is not a multiple of 5.
"""


def check_number(number):
    """
    This method checks whether the give number is divisible by 7 but is not a multiple of 5.
    :param number: The number which is to be tested for above-mentioned condition.
    :return: Returns true or false.
    """

    if (number % 7 == 0) and (number % 5 != 0):
        return True
    else:
        return False


def list_numbers():
    """
    This method appends all the numbers which are divisible by 7 but is not a multiple of 5 in a list.
    :return: num_list containing all numbers that satisfy the condition.
    """
    num_list = []
    start, end = get_range()
    for i in range(start, end):
        if check_number(i):
            num_list.append(i)
    return num_list


def get_range():
    """
    Gets the range if number to be checked for the specified condition.
    :return: start and end of the range.
    """
    print("Enter the starting number and the final number till which the condition is to be checked:")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the final number: "))
    return start, end

result = list_numbers()
print("-----------------------------------------------------------\n", result)
