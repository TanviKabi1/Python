n = int(input())
a = list(map(int, input().split()))
t = int(input())

d = {}
for i in range(n):
    diff = t - a[i]
    if diff in d:
        print(d[diff], i)
        break
    d[a[i]] = i
