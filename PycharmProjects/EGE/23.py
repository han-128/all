def f(x, y):
    if x == y:
        return 1
    if x > y or x == 5 or x == 12:  # без 5 и без 12
        return 0
    return f(x + 1, y) + f(2 * x - 1, y) + f(2 * x + 1, y)  # предыдущий и следующий
print(f(3, 9) * f(9, 15))   # включая 9