import math

f = open("1.txt")
a = [int(x) for x in f]
f.close()
n = len(a)

rr = 0
sum1 = 0
sum2 = 0

for i in range(n-1):
    num1 = abs(a[i])
    num2 = abs(a[i + 1])
    sum1 = 0
    sum2 = 0
    print(1)
    while (num1 != 0):
        print(2)
        sum1 = sum1 + abs(num1) % 10
        num1 = num1 // 10
    while (num2 != 0):
        sum2 = sum2 + abs(num2) % 10
        num2 = num2 // 10
    sumA = sum1 + sum2
    if ((sum1 % 10 == 0) and (sum2 % 10 == 0)):
        rr += 1
    print(a[i], sum1)
    print(a[i + 1], sum2)


print(rr)