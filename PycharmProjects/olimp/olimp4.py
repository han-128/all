n = int(input())
d = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
k = a[0] // d + 1
for i in range(1, len(a)):
    if i + 1 <= k:
        t = a[i] // d + i + 1
        if k < t:
            k = t
    else:
        break
if k > len(a):
    k = len(a)
print(k)
