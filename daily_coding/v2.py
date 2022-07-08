def get_remaining_candy(l, m):
    s = sum(l)
    val = s%m
    return val

def solution():
    t = int(input())
    if t <= 100:
        for i in range(t):
            N, M = map(int, input().split(' '))
            if (N <= 10**5 and M <= 10**4):
                list_ = list(map(int, input().split(' ')))
                if len(list_) != N:
                    break
            #output = get_remaining_candy(list_, N, M)
            bool_ = True
            for j in list_:
                if j>1000:
                    bool_ = False
            if bool_ == False:
                break
            output = sum(list_)%M
            print(f"Case #{i+1}: {output}")
    
solution()
