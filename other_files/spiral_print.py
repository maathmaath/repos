import numpy as np

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
split_arr_limit = 5
size = len(arr)/split_arr_limit
arr = np.array_split(arr, size)


Ti, Bi = 0, int(size)
Lj, Rj = 0, split_arr_limit

i_pos, j_pos = 0, 0
count = 0
while True:
    if count == (size*split_arr_limit):
        break
    if i_pos == Ti:
        if j_pos == Lj:
            for i in arr[Ti][Lj:Rj]:
                print(i)
                j_pos += 1
                count += 1
            Ti += 1
            i_pos = Ti
        elif j_pos == Rj:
            for i in arr[Ti:Bi]:
                print(i[Rj-1])
                i_pos += 1
                count += 1
            Rj -= 1
            j_pos = Rj
    elif i_pos == Bi:
        if j_pos == Rj:
            x = list(reversed(arr[Bi-1][Lj:Rj]))
            for i in x:
                print(i)
                j_pos -= 1
                count += 1
            Bi -= 1
            i_pos = Bi
            # print(f"i pos is {i_pos}")
        elif j_pos == Lj:
            x = list(reversed(arr[Ti:Bi]))
            for i in x:
                print(i[Lj])
                i_pos -= 1
                count += 1
            Lj += 1
            j_pos = Lj
