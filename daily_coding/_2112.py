# Q: initialize ele = 1, for every ith iter print the previos no's fz and its no.

a = 1
range_ = 50
i = 0


def makeValue(val, _dic):
    _dic[val] = _dic[val]+1 if val in _dic.keys() else 1
    return _dic


def getDict(val):
    # from integer type splitting
    arr = {}
    while True:
        if val < 10:
            arr = makeValue(val, arr)
            return arr
        rem = val % 10
        val = val//10
        arr = makeValue(rem, arr)


def constructNumber(arr):
    # direct interger formation
    _sum = 0
    for index, val in enumerate(arr):
        _sum = (((_sum*10)+arr[val])*10)+val
    return _sum

    # from str to int conversion
    # _str = ""
    # for index, val in enumerate(arr):
    #     _str += (str(arr[val]) + str(val))
    # return int(_str)


iN = 1
print("\nThe following is the output for the program.\n")
print(iN)

# for loop
for i in range(range_):
    iN = constructNumber(getDict(iN))
    print(iN)
