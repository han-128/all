# из 10 сс в 7 сс

decimal_number = 157775382034845806574689115
result = "0"

while decimal_number > 0:
    remainder = decimal_number % 7
    result = str(remainder) + result
    decimal_number //= 7

