class Solution(object):
    def repeatedLogin(self, n, k, a):
        last = {}
        for i in range(n):
            x = a[i]
            if x in last and i - last[x] <= k:
                return "YES"
            last[x] = i
        return "NO"

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(Solution().repeatedLogin(n, k, a))
