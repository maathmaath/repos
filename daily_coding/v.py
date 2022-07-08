def get_remaining_candy(l, m):
    s = sum(l)
    val = s%m
    return val

t = int(input())

for i in range(t):
    N, M = map(int, input().split(' '))
    list_ = list(map(int, input().split(' ')))
    if len(list_) != N:
        break
    output = get_remaining_candy(list_, M)
    print(f"Case #{i+1}: {output}")
