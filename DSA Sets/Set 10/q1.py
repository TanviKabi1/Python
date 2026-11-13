class Solution(object):
    def sortedSquares(self, a):
        n = len(a)
        res = [0] * n
        l, r = 0, n - 1
        p = n - 1
        while l <= r:
            sl = a[l] * a[l]
            sr = a[r] * a[r]
            if sl > sr:
                res[p] = sl
                l += 1
            else:
                res[p] = sr
                r -= 1
            p -= 1
        return res

n = int(input())
a = list(map(int, input().split()))
print(*(Solution().sortedSquares(a)))
