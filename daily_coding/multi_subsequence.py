# Write a program that computes the length of the longest common subsequence
# of three given strings. For example, given "epidemiologist", "refrigeration",
# and "supercalifragilisticexpialodocious", it should return 5, since
# the longest common subsequence is "eieio".

def findSubsequence(i, s):
    boool = [False for k in s]
    sCopy = []
    for indexArr, word in enumerate(s):
        if all(boool[:indexArr]):
            for index, char in enumerate(word):
                if char == i:
                    sCopy.append(word[index+1:])
                    boool[indexArr] = True
                    break
        else:
            break
    if boool and all(boool):
        return True, sCopy
    return False, s


def traverseStrings(s):
    if s[0] == '':
        return 0
    # print(s)
    k = [s[0][1:]] + s[1:]
    maxSubSequence = ''
    baseString = s[0]
    s = s[1:]
    for i in baseString:
        boool, s = findSubsequence(i, s)
        maxSubSequence += i if boool else ''
    print(maxSubSequence)
    return max(len(maxSubSequence), traverseStrings(k))

# def traverseStrings(s):
#     maxSubSequence = ''
#     baseString = s[0]
#     s = s[1:]
#     for i in baseString:
#         boool, s = findSubsequence(i, s)
#         maxSubSequence += i if boool else ''
#     return maxSubSequence


# def solution(s):
#     lists = []
#     baseString = s[0]
#     for i in range(len(s[0])):
#         s[0] = baseString[i:]
#         lists.append(traverseStrings(s))
#     print(lists)


def main():
    noOfStrings = 3
    Strings = ["epidemiologist", "refrigeration",
               "supercalifragilisticexpialodocious"]
    # for i in range(noOfStrings):
    # Strings.append(input())
    # solution(Strings)
    print("\n%d" % traverseStrings(Strings))


main()
