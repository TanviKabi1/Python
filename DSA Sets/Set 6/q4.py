lass Solution(object):
    def sortItems(self, a):
        freq = {}
        for x in a:
            freq[x] = freq.get(x, 0) + 1
        items = list(freq.keys())
        def qsort(arr):
            if len(arr) <= 1:
                return arr
            p = arr[len(arr) // 2]
            pf, pv = freq[p], p
            l = [x for x in arr if (freq[x] < pf) or (freq[x] == pf and x > pv)]
            m = [x for x in arr if freq[x] == pf and x == pv]
            r = [x for x in arr if (freq[x] > pf) or (freq[x] == pf and x < pv)]
            return qsort(l) + m + qsort(r)
        sorted_keys = qsort(items)
        res = []
        for k in sorted_keys:
            res.extend([k] * freq[k])
        return " ".join(map(str, res))
n = int(input())
a = list(map(int, input().split()))
print(Solution().sortItems(a))
