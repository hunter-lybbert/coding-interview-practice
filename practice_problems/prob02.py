"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
import math

def special_product_v1(
    input_list: list[int]
) -> list[int]:
    """
    Given an array of integers, return a new array such that each element at
    index i of the new array is the product of all the numbers in the original
    array except the one at i.
    """
    output_list = []
    for i in range(len(input_list)):
        curr_list = input_list.copy()
        curr_list.pop(i)
        output_list.append(math.prod(curr_list))

    return output_list


def special_product_v2(
    input_list: list[int]
) -> list[int]:
    """
    Given an array of integers, return a new array such that each element at
    index i of the new array is the product of all the numbers in the original
    array except the one at i.
    """
    prev_prod = math.prod(input_list[1:])
    output_list = [prev_prod] * len(input_list)
    for i in range(1, len(input_list)):
        curr_prod = prev_prod * input_list[i - 1] / input_list[i]
        output_list[i] = curr_prod
        prev_prod = curr_prod

    return output_list


def special_product_v3(
    input_list: list[int]
) -> list[int]:
    """
    Given an array of integers, return a new array such that each element at
    index i of the new array is the product of all the numbers in the original
    array except the one at i.
    """
    # This will have a divide by zero error perhaps...
    output_list = [math.prod(input_list)] * len(input_list)
    for i, num in enumerate(output_list):
        output_list[i] /= input_list[i]

    return output_list
