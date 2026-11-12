m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split())) if n > 0 else []

i = m - 1
j = n - 1
k = m + n - 1

while j >= 0:
    if i >= 0 and a[i] > b[j]:
        a[k] = a[i]
        i -= 1
    else:
        a[k] = b[j]
        j -= 1
    k -= 1

print(*(a))
