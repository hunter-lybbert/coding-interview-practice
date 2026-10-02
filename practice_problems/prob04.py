"""
Problem #4:

Post Completion Reflections:
    - That was hard and I pretty much failed it.
    - Maybe come back to this one in the future sometime.


This is your coding interview problem for today.
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array.
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

Have a great day!
"""

# =========================== Your Solution Below ========================== #

def func(list_of_int: list[int]) -> int:
    """
    """
    # sort? then iterate?
    # linear time means I cannot iterate over the list twice that would be n^2

    # current_min = 1
    # for num in list_of_int:
    #     if num > 0:
    #         if num > current_min:
    #             next
    #         else:
    #             current_min = num
    # shortcut
    sorted_list = sorted(list_of_int)
    pos_val_counter = 1
    for i in sorted_list:
        if i <= 0:
            if i == sorted_list[-1]:
                return pos_val_counter
            next
        elif i == pos_val_counter:
            pos_val_counter += 1
        else:
            if i == sorted_list[-1]:
                return pos_val_counter + 1
            return pos_val_counter
    # return current_min


def func(nums):
    print(f"list at start: {nums}")
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            print(f"list after editing index {i}: {nums}")
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1


# =========================== Your Solution Above ========================== #

def test_case():
    """
    """
    print("================= TEST 1 =================")
    test_1 = [5, 3, 2, 1, 0]
    assert func(test_1) == 4

    print("================= TEST 2 =================")
    test_2 = [-2, -1, -3]
    assert func(test_2) == 1

    print("================= TEST 3 =================")
    test_3 = [3, 4, -1, 1]
    assert func(test_3) == 2

    print("================= TEST 4 =================")
    test_4 = [1, 2, 0]
    assert func(test_4) == 3


if __name__ == "__main__":
    test_case()

"""
Their Solution:

def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

# or

def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i
"""