class Solution(object):
    def insertPoint(self, a, t):
        l, r = 0, len(a) - 1
        ans = len(a)
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] >= t:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

n = int(input())
a = list(map(int, input().split()))
t = int(input())
print(Solution().insertPoint(a, t))
