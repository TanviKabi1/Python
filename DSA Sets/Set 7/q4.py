class Solution(object):
    def searchRange(self, a, x):
        l, r = 0, len(a) - 1
        first = -1
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] == x:
                first = mid
                r = mid - 1
            elif a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        l, r = 0, len(a) - 1
        last = -1
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] == x:
                last = mid
                l = mid + 1
            elif a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return f"{first} {last}"

n = int(input())
a = list(map(int, input().split()))
x = int(input())
print(Solution().searchRange(a, x))
