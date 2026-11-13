class Solution(object):
    def floorCeil(self, a, q):
        fl, cl = None, None
        l, r = 0, len(a) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] <= q:
                fl = a[mid]
                l = mid + 1
            else:
                r = mid - 1
        l, r = 0, len(a) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if a[mid] >= q:
                cl = a[mid]
                r = mid - 1
            else:
                l = mid + 1
        return (str(fl) if fl is not None else "None") + " " + (str(cl) if cl is not None else "None")

n = int(input())
a = list(map(int, input().split()))
q = int(input())
print(Solution().floorCeil(a, q))
