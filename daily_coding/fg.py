# class D:
#     def __init__(self):
#         self.x = 'sss'
#
#     def dis(self):
#         print(self.x)
#
#
# class j(D):
#     def __init__(self):
#         super().__init__()
#         self.x = 'yyy'
#
#
# d = j()
# j.dis()


# class D(object):
#     def __init__(self, s):
#         self.s = s
#
#     def __add__(self, o):
#         print("here")
#         return D("jhg")
#
#     def __str__(self):
#         print("wee")
#         return "adva"
#
#
# A = D("x")
# B = D("l")
# print(A+B)

import random
import re
import copy

# S = 'j-Ih-gfE=dCba'
# output to be 'a-bC-dEf=ghIj' (reversed but symbol pos constant)


def solution(S: str) -> str:
    symbols = list(set(re.findall("[^a-zA-Z]", S)))
    copyS = copy.deepcopy(S)
    for i in symbols:
        copyS = copyS.replace(i, "")
    reversedStr = copyS[::-1]
    for index, val in enumerate(S):
        if val in symbols:
            reversedStr = reversedStr[:index] + val + reversedStr[index:]
    return reversedStr


def generateTokenString(_len: int) -> str:
    no_of_sym = random.randint(3, _len-2)
    no_letters = _len - no_of_sym
    alpha = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    symbols = "-=+!@#$%^&*()~`\\.;:"
    s = ""
    while True:
        place = random.choice(range(no_letters))
        no_letters -= place
        ss = "".join(random.choice(alpha) for i in range(place+1))
        s += (ss + random.choice(symbols))
        if len(s) >= _len:
            break
    return s


for i in range(200):
    S = generateTokenString(15)
    print(S)
    print(solution(S))
    print("\n")
