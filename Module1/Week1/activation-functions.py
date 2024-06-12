import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


class ActivFunction:

    def __init__(self, alph=0.01):
        self.alph = alph

    def calculate_sigmoid(self, x):
        result = 1 / (1 + math.exp(-x))
        return result

    def calculate_relu(self, x):
        return 0 if x <= 0 else x

    def calculate_elu(self, x):
        return x if x > 0 else self.alph * (math.exp(x) - 1)

    def calculate_acti_func(self, x, acti_func):
        acti_func = acti_func.lower()
        if acti_func == "sigmoid":
            return self.calculate_sigmoid(x)
        elif acti_func == "relu":
            return self.calculate_relu(x)
        elif acti_func == "elu":
            return self.calculate_elu(x)


def exercise2():
    x = input("Input x = ")
    result = False
    if is_number(x) == False:
        print("x must be a number")
    else:
        x = float(x)
        acti_func = input("Input activation Function (sigmoid|relu|elu): ")
        acti_lst = ["sigmoid", "relu", "elu"]
        if acti_func.lower() not in acti_lst:
            return f"{acti_func} is not supported"
        else:
            af = ActivFunction()
            result = af.calculate_acti_func(x, acti_func=acti_func)
    return f"{acti_func.lower()}: f({x}) = {result}"
