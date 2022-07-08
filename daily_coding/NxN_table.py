class Solution(object):
    def __init__(self, N):
        self.N = N

    def solution(self, x):
        _list = []
        for i in range(2, self.N+1):
            _list.extend(i*j for j in range(1, i))
        diag = [i**2 for i in range(1, N+1)]
        return 2*_list.count(x) + diag.count(x)


N = int(input())
X = int(input())
print(Solution(N).solution(X))

# takes a no and find fz of the no in NxN table.
