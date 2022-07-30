# Question 1
# Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down
# in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as
# few cards as possible. Write a function to help Bob locate the card.

test_case = {'input': {'cards': [13, 11, 10,
                                 7, 4, 3, 1, 0], 'query': 3}, 'output': 5}

# Linear: O(N)
# def locate_card(cards, query):
#     position = 0
#     while position < len(cards):
#         if cards[position] == query:
#             return position
#         position += 1
#     return -1


# Binary Search O(log(n))
def locate_card(cards, query):
    low, high = 0, len(cards) - 1

    while low <= high:
        mid = (low + high) // 2
        print(f"low: {low}, high: {high}")
        result = check_location(cards, query, mid)

        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1

    return -1


def check_location(cards, query, mid):
    mid_number = cards[mid]
    print(f"mid: {mid}, mid_number: {mid_number}")
    if mid_number == query:
        if mid - 1 >= 0 and cards[mid - 1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'


result = locate_card(**test_case['input'])
print(result)
print(result == test_case['output'])


# General Answer
def binary_search(low, high, condition):
    while low <= high:
        mid = (low + high) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        else:
            low = mid + 1

    return -1


def final_answer(cards, query):

    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)


# Question: Given an array of integers nums sorted in ascending order, find the starting ending and position of a given number
def locate_positions(nums, target):
    first_position = locate_first_position(nums, target)
    last_position = locate_last_position(nums, target)
    return (first_position, last_position)


def locate_first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        return 'left'
    return binary_search(0, len(nums) - 1, condition)


def locate_last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        return 'left'
    return binary_search(0, len(nums) - 1, condition)

# Problem - Rotated Lists

# We'll solve the following problem step-by-step:
# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. You can assume that all the numbers in the list are unique.
# Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.
# We define "rotating a list" as removing the last element of the list and adding it before the first element. E.g. rotating the list `[3, 2, 4, 1]` produces `[1, 3, 2, 4]`.
# "Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.


# Linear => O(N)
def count_rotation_linear(nums):
    if len(nums) <= 1:
        return 0
    position = 1
    while position < len(nums):
        if position > 0 and nums[position] < nums[position - 1]:
            return position

        position += 1

    return 0


def count_rotation(nums):
    if len(nums) <= 1:
        return 0

    low = 0
    high = len(nums) - 1
    length = len(nums)

    if nums[high] > nums[low]:
        return 0

    if nums[high] < nums[high - 1]:
        return high

    if nums[low + 1] < nums[low]:
        return 1

    while low <= high:
        mid = low + (high-low) // 2
        prev = (mid-1+length) % length
        nex = (mid+1) % length
        if nums[mid] < nums[prev] and nums[mid] <= nums[nex]:
            return mid
        elif nums[mid] < nums[low]:
            high = mid-1
        elif nums[mid] > nums[high]:
            low = mid+1
        else:
            return 0

    return 0
