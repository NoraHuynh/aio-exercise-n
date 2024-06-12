def fact(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)


def approx_sin(x, n):
    if type(n) != type(1):
        print("n must be an integer")
    elif n <= 0:
        print("n must be greater than zero")
    else:
        result = 0
        for idx in range(n + 1):
            unit = ((-1) ** idx) * (x ** (2 * idx + 1)) / fact(2 * idx + 1)
            result += unit
        return result


def approx_cos(x, n):
    if type(n) != type(1):
        print("n must be an integer")
    elif n <= 0:
        print("n must be greater than zero")
    else:
        result = 0
        for idx in range(n + 1):
            unit = ((-1) ** idx) * (x ** (2 * idx)) / fact(2 * idx)
            result += unit
        return result


def approx_sinh(x, n):
    if type(n) != type(1):
        print("n must be an integer")
    elif n <= 0:
        print("n must be greater than zero")
    else:
        result = 0
        for idx in range(n + 1):
            unit = (x ** (2 * idx + 1)) / fact(2 * idx + 1)
            result += unit
        return result


def approx_cosh(x, n):
    if type(n) != type(1):
        print("n must be an integer")
    elif n <= 0:
        print("n must be greater than zero")
    else:
        result = 0
        for idx in range(n + 1):
            unit = (x ** (2 * idx)) / fact(2 * idx)
            result += unit
        return result
