import copy


def get_citation(arr):
    values = []
    if arr[0] > 0:
        values.append(str(1))
    for index, val in enumerate(arr[1:]):
        # x_index = copy.deepcopy(index) + 2
        x_index = index + 2
        while True:
            lk = [x_index for j in arr[:index+2] if j >= x_index]
            if x_index <= len(lk):
                values.append(str(x_index))
                break
            else:
                x_index -= 1
    str_val = ' '.join(values)
    return str_val


def solution():
    t = int(input())
    if t > 100:
        exit()
    for i in range(t):
        N = int(input())
        lis = list(map(int, input().split(' ')))
        print(lis)
        if not N == len(lis):
            break
        print(f"Case #{i+1}: {get_citation(lis)}")


solution()
