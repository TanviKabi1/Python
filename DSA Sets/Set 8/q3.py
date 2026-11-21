class Solution(object):
    def findMin(self, a):
        l, r = 0, len(a) - 1
        while l < r:
            mid = l + (r - l) // 2
            if a[mid] > a[r]:
                l = mid + 1
            else:
                r = mid
        return a[l]

n = int(input())
a = list(map(int, input().split()))
print(Solution().findMin(a))
