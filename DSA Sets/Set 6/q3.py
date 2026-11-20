lass Solution(object):
    def mergeUnion(self, a, b):
        i, j = 0, 0
        res = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                res.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
        while i < len(a):
            res.append(a[i])
            i += 1
        while j < len(b):
            res.append(b[j])
            j += 1
        return " ".join(map(str, res))
m, n = map(int, input().split())
a = list(map(int, input().split())) if m > 0 else []
b = list(map(int, input().split())) if n > 0 else []
print(Solution().mergeUnion(a, b))
