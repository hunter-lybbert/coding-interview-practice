"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import math

def find_summands_to_value(
    input_list: list[int],
    k: int,
) -> bool:
    """
    Return true if any two numbers from the list add up to k.
    """
    for i, num_1 in enumerate(input_list):
        for j, num_2 in enumerate(input_list):
            if i != j and  num_1 + num_2 == k:
                return True

    return False


def find_summands_to_value_v2(
    input_list: list[int],
    k: int,
) -> bool:
    """
    Return true if any two numbers from the list add up to k.
    """
    seen = set()
    for num_1 in input_list:
        if k - num_1 in seen:
            return True
        else:
            seen.add(num_1)
    return False


def find_summands_via_conv(
    input_list: list[int],
    k: int,
) -> bool:
    """
    Return true if any two numbers from the list add up to k.
    """
    math
