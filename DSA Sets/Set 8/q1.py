class Solution(object):
    def floorSqrt(self, x):
        if x < 2:
            return x
        l, r = 1, x
        ans = 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

x = int(input())
print(Solution().floorSqrt(x))
