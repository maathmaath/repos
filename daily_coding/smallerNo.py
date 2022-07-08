# Given an array of integers, return a new array where each element in the new array is the number of smaller elements to the right of that element in the original input array.
#
# For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
#
# There is 1 smaller element to the right of 3
# There is 1 smaller element to the right of 4
# There are 2 smaller elements to the right of 9
# There is 1 smaller element to the right of 6
# There are no smaller elements to the right of 1


import numpy as np


def aotherSolution(a):
    newArr = []
    for index, val in enumerate(a):
        xVal = []
        [xVal.append(i) for i in a[index+1:] if i < val]
        newArr.append(len(xVal))
    return newArr


def Solution(a):
    newArr = []
    for index, val in enumerate(a):
        count = 0
        for i in a[index+1:]:
            if i < val:
                count += 1
        newArr.append(count)
    return newArr


no_of_elements = int(
    input("[*] Enter the no of elements you would want to consider.?\n"))
np.random.seed(0)
highestNo = 999
arr = np.random.choice(highestNo, no_of_elements)
# arr = list(map(int, input().split(' ')))

print(arr)
newArray = Solution(arr)
print(newArray)
