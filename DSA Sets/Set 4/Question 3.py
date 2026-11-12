class Solution(object):
    def strongAverageDays(self, n, k, t, a):
        target = k * t
        w = 0
        for i in range(k):
            w += a[i]
        ans = 1 if w >= target else 0
        for i in range(k, n):
            w += a[i] - a[i - k]
            if w >= target:
                ans += 1
        return ans

n, k, t = map(int, input().split())
a = list(map(int, input().split()))
print(Solution().strongAverageDays(n, k, t, a))
