import sys
import os
import numpy as np

''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT
# Write code here


def getRoomNo(base, n, a, N):
    while True:
        x = np.arange(base, n)
        xLen = len(x)-1
        for index, val in enumerate(x[::-1]):
            if '14' in str(val) or '2' in str(val):
                x = np.delete(x, xLen-index)
        a = np.append(a, x)
        if len(a) >= N:
            return a[N-1]
        else:
            n += (N-len(a))
            return getRoomNo(int(a[-1]+1), n, a, N)


def Solution():
    try:
        N = int(input())
        val = getRoomNo(1, N, [], N)
        print(int(val))
    except Exception as e:
        print(e)


Solution()
