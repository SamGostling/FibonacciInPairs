import math


def fibonacci_in_pairs(x, y):
    a = int(x)
    b = int(y)
    count = 0
    if gcd(a, b) != 1:
        return "impossible"

    while a > 1 or b > 1:
        if a > b:
            c = int(math.floor(a / b))
            a -= b * c
            count += c

        else:
            c = int(math.floor(b / a))
            b -= a * c
            count += c

        if a == 0 or b == 0:
            count -= 1

    return str(count)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


print(fibonacci_in_pairs("20", "7"))
