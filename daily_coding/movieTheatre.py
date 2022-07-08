import sys
import os
import numpy as np


def Solution():
    totalSeats, occupied, likedSeats = map(int, input().split(' '))
    assert totalSeats <= 10**9 and occupied <= 10**6 and likedSeats <= 10**6 and likedSeats > 0

    seats = set()
    while occupied > 0:
        try:
            val = int(input())
            seats.add(val)
        except:
            pass
        finally:
            occupied -= 1

    # seats = np.array([])
    # while occupied > 0:
    #     try:
    #         val = int(input())
    #         seats = np.append(seats,val) if val not in seats else seats
    #     except:
    #         pass
    #     finally:
    #         occupied-=1
    # seats = np.unique(seats)

    l = ""
    while likedSeats > 0:
        try:
            val = int(input())
            assert val in seats
            print("N")
        except:
            print("Y")
        finally:
            likedSeats -= 1


Solution()
