n = int(input())
a = list(map(int, input().split()))

cand, count = None, 0
for x in a:
    if count == 0:
        cand, count = x, 1
    elif x == cand:
        count += 1
    else:
        count -= 1

print(cand)
