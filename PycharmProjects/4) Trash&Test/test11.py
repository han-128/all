s = 15672345
print(len(str(s)))
print(s // (10**(len(str(s)))))

print(s // 10)
print(s // 100)
print(s // 1000)
print(s // 10000)

print("######")

print(s % 10)
print(s % 100)
print(s % 1000)
print(s % 10000)

print(";;;;;;;;")

q = -122212

print(abs(q))

qw = "3233"
qe = int(qw, 4)
print(qe)

print(49**6 * 7**19 - 7**9 - 21)

decimal_number = 157775382034845806574689115
result = "0"

while decimal_number > 0:
    remainder = decimal_number % 7
    result = str(remainder) + result
    decimal_number //= 7

print(result.count("6"))

df = 1234
print(df % 10)
print(df % 100 // 10)
print(df % 1000 // 100)
print(df % 10000 // 1000)