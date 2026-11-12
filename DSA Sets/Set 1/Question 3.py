n = int(input())
a = list(map(int, input().split()))

m1, m2 = None, None
for x in a:
    if m1 is None or x > m1:
        m2 = m1
        m1 = x
    elif x != m1 and (m2 is None or x > m2):
        m2 = x

print(m2 if m2 is not None else "None")
