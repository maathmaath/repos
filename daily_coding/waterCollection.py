import numpy as np


def Solution():
    pass


# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.


def Solution(a):
    leftWall = a[0]
    count = 0
    total = 0
    for index, i in enumerate(a[1:]):
        if leftWall < i:
            print(f"added count {count}, left wall assigned to {i}")
            leftWall = i
            total += count
            count = 0
        else:
            print(f"adding count {leftWall-i}")
            count += (leftWall-i)
    return total


def get(l, li, i, a, c):
    if i == len(a):
        return 0
    if l > a[i]:
        if a[i] < a[i+1]:
            imp = min(l, a[i+1]) - a[i]
            dup_l = a[i+1]
            c += get(dup_l, i+2, )
        elif a[i] == a[i+1]:
            pass
        else:
            c += get(a[i], i+1, a, c)

# def S(l, li, i, a, c):


def Sol(a):
    leftWall = a[0]
    count = 0
    i = 0
    get(leftWall, count, i, a)


np.random.seed(0)
highestNo = 32
no_of_elements = 9
# arr = np.random.choice(highestNo, no_of_elements)
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution(arr))

# class Solution:
#   def trap(self, height: List[int]) -> int:
#     n = len(height)
#     l = [0] * n  # l[i] := max(height[0..i])
#     r = [0] * n  # r[i] := max(height[i..n))
#
#     for i, h in enumerate(height):
#       l[i] = h if i == 0 else max(h, l[i - 1])
#
#     for i, h in reversed(list(enumerate(height))):
#       r[i] = h if i == n - 1 else max(h, r[i + 1])
#
#     return sum(min(l[i], r[i]) - h
#                for i, h in enumerate(height))


# class Solution:
#   def trap(self, height: List[int]) -> int:
#     if not height:
#       return 0
#
#     ans = 0
#     l = 0
#     r = len(height) - 1
#     maxL = height[l]
#     maxR = height[r]
#
#     while l < r:
#       if maxL < maxR:
#         ans += maxL - height[l]
#         l += 1
#         maxL = max(maxL, height[l])
#       else:
#         ans += maxR - height[r]
#         r -= 1
#         maxR = max(maxR, height[r])
#
#     return ans
