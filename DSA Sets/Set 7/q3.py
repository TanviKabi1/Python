class Solution(object):
    def firstFail(self, a):
        l, r = 0, len(a) - 1
        ans = -1
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] == 1:
                ans = mid + 1
                r = mid - 1
            else:
                l = mid + 1
        return ans

n = int(input())
a = list(map(int, input().split()))
print(Solution().firstFail(a))
