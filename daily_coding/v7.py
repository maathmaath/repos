def get_citation(arr):
    values = []
    if arr[0] > 0:
        values.append(str(1))
    else:
        values.append(str(0))
    for index, val in enumerate(arr[1:]):
        x_index = index+2
        k = reversed(range(1, x_index+1))
        for i in k:
            lk = [i for j in arr[:index+2] if j >= i]
            if i <= len(lk):
                values.append(str(i))
                break
    str_val = ' '.join(values)
    return str_val


def solution():
    t = int(input())
    if t > 100:
        exit()
    for i in range(t):
        N = int(input())
        if N <= 10**5:
            lis = list(map(int, input().split(' ')))
            if not N == len(lis):
                break
            print(f"Case #{i+1}: {get_citation(lis)}")


solution()
