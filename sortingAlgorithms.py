# author Tian Cheng Liu
# date October 31 2022

# Sorting Algorithms to code: Selection sort, bubble sort, insertion sort, 
# merge sort, quick sort, heap sort, counting sort, radix sort, bucket sort
# bogo sort

# function is_sorted determines whether list is sorted or not. Returns boolean.

def is_sorted(list):
    n = len(list)
    for i in range(n-1):
        if list[i] > list[i + 1]:
            return False                # return will break the for loop
    return True

# a couple lists for testing
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [4, 3, 1, 5, 2, 6, 9, 8, 7, 0]
c = [5, 4, 2, 1, 8, 0, 0, 0, 0, 0]
d = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

assert is_sorted(a) is True
assert is_sorted(b) is False
assert is_sorted(c) is False
assert is_sorted(d) is True

# bogo sort is a joke about randomly sorting all elements of the list and
# seeing if it is sorted. If it is not, try again.
# O(inf)

import random

def shuffle(list):
    n = len(list)
    for i in range(n):
        rand = random.randint(0, n - 1)
        list[i], list[rand] = list[rand], list[i]

def bogo_sort(list):
    while not is_sorted(list):
        shuffle(list)
    print(f'{list=}')


# selection sort: loop through the list and find the smallest value then swap
#                 with first list item. Repeat

def select_sort(list):
    n = len(list)

    # this function iterates over all indexes and replaces with smallest value
    # among the rest of the list. A check is verified if the list is sorted at
    # the start of each iteration
    for i in range(n-1):
        if is_sorted(list):
            return list      # breaks out of loop as soon as the list is sorted
        x = i
        for j in range(i + 1, n):
            if list[j] < list[x]:
                x = j
        list[i], list[x] = list[x], list[i]

assert is_sorted(select_sort(a))
assert is_sorted(select_sort(b))
assert is_sorted(select_sort(c))
assert is_sorted(select_sort(d))


# bubble sort: 