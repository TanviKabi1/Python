class Solution(object):
    def maxProfit(self, a):
        if len(a) <= 1:
            return 0
        min_p = a[0]
        ans = 0
        for i in range(1, len(a)):
            diff = a[i] - min_p
            if diff > ans:
                ans = diff
            if a[i] < min_p:
                min_p = a[i]
        return ans

n = int(input())
a = list(map(int, input().split()))
print(Solution().maxProfit(a))
