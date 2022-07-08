def ret(char):
    if char == '.':
        return 'nobody'
    elif char == 'B':
        return 'Blue'
    elif char == 'R':
        return 'Red'
    else:
        return 'Impossible'


def check(arr, N):
    count_arr = [j for i in arr for j in i]
    B = count_arr.count('B')
    R = count_arr.count('R')
    dot = count_arr.count('.')
    if not (B+1 == R or B-1 == R or B == R) or dot == 1:
        return 'Impossible'
    blue_win = False
    red_win = False
    for i in arr:
        if not blue_win:
            if all(j == 'B' for j in i):
                blue_win = True
                break
    if blue_win:
        return 'Blue'
    for i in range(1, N-1):
        col = [arr[j][i] for j in range(N)]
        if not red_win:
            if all(j == 'R' for j in col):
                red_win = True
                break
    if red_win:
        return 'Red'
    else:
        return 'Nobody'


def solution():
    T = int(input())
    if T > 100:
        exit()
    for i in range(T):
        N = int(input())
        if N > 10:
            break
        if N == 1:
            print(f"Case #{i+1}: {ret(input())} wins")
        else:
            lis = []
            for j in range(N):
                row = ' '.join(input())
                row = row.split(' ')
                if len(row) > 10:
                    break
                lis.append(row)
            print(f"Case #{i+1}: {check(lis, N)} wins")


solution()
