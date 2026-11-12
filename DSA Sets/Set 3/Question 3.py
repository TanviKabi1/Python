n = int(input())
a = list(map(int, input().split()))

p = 0
for i in range(n):
    if a[i] != 0:
        a[p], a[i] = a[i], a[p]
        p += 1

print(*(a))
