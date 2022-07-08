# def get_min_ops(s, n, k):
#     len_ = n//2
#     s1 = s[:len_]
#     s2 = (s[::-1])[:len_]
#     print(s1, s2)
#     count = 0
#     for i in range(n//2):
#         if s1[i] != s2[i]:
#             count += 1
#             if count >= k:
#                 return 0
#     return k - count
#
#
# def solution():
#     t = int(input())
#     for i in range(t):
#         n, k = map(int, input().split(' '))
#         s = input()
#         if n != len(s):
#             break
#         print(get_min_ops(s, n, k))
#
#
# solution()

def get_min_ops(s, n, k):
    len_ = n//2
    s1 = s[:len_]
    s2 = (s[::-1])[:len_]
    count = 0
    for i in range(n//2):
        if s1[i] != s2[i]:
            count += 1
            if count >= k:
                return 0
    return k - count


def gmo(S, N, K):
    len_ = N//2
    s1 = S[:len_]
    s2 = (S[::-1])[:len_]
    return abs(sum(int(s1[i] != s2[i]) for i in range(N//2))-K)


def gmo(S, N, K):
    return abs(sum(int(S[i] != S[N-1-i]) for i in range(N//2))-K)


def solution():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split(' '))
        s = input()
        if n != len(s):
            break
        # print(f"Case #{i+1}: {get_min_ops(s, n, k)}")
        print(f"Case #{i+1}: {gmo(s, n, k)}")


solution()
