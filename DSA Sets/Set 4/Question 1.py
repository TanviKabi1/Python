class Solution(object):
    def maxTraffic(self, n, k, a):
        w = 0
        for i in range(k):
            w += a[i]
        ans = w
        for i in range(k, n):
            w += a[i] - a[i - k]
            if w > ans:
                ans = w
        return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(Solution().maxTraffic(n, k, a))
