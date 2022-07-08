# Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.
#
# For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].


def Solution(a):
    tupleList = []
    for index, val in enumerate(a):
        for nextIndex, val_ in enumerate(a[index+1:]):
            keyStr = val + val_
            if keyStr == keyStr[::-1]:
                tupleList.append((index, nextIndex+index+1))
                if len(val) == len(val_):
                    tupleList.append((nextIndex+index+1, index))
                else:
                    if val_ + val == (val_ + val)[::-1]:
                        tupleList.append((nextIndex, index))
    return tupleList


stringArr = ["code", "edoc", "da", "d"]
print(Solution(stringArr))
