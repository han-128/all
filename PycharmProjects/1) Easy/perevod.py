number = 101001
base = 10
result = " "
while number > 0:
    result += str(number % base)
    number //= base
print(result[::-1])