def ret(char):
    if char == '.':
        return 'nobody'
    elif char == 'B':
        return 'Blue'
    elif char == 'Red':
        return 'Red'
    else:
        return 'Impossible'
        
def check(arr, N):
    blue_win = False
    red_win = False
    for i in arr:
        if not blue_win:
            if all(i) == 'B':
                blue_win = True
        if not red_win:
            if all(i) == 'R':
                red_win = True
    for i in range(N):
        col = [arr[j][i] for j in range(N)]
        if not blue_win:
            if all(col) == 'B':
                blue_win = True
        if not red_win:
            if all(col) == 'R':
                red_win = True
    if blue_win and red_win:
        return 'Impossible'
    elif blue_win:
        return 'Blue'
    elif red_win:
        return 'Red'
    else:
        return 'Nobody'
    

def solution():
    T = int(input())
    if T > 100:
        exit()
    for i in range(T):
        N = int(input())
        if N == 1:
            print(f"Case #{i+1}: {ret(input())} wins")
        else:
            lis = []
            for j in range(N):
                row = ' '.join(input())
                row = row.split(' ')
                lis.append(row)
            print(f"Case #{i+1}: {check(lis, N)} wins")
        
solution()
