def check_type(value_dct):
    right_type = True
    for val in value_dct:
        if type(value_dct[val]) != type(1):
            right_type = False
            print(f"{val} must be int")
    if right_type == True:
        return 1


def check_value(value_dct):
    right_value = True
    for val in value_dct:
        if value_dct[val] <= 0:
            right_value = False
            print(f"{val} must be greater than zero")
    if right_value == True:
        return 1


def exercise1(tp, fp, fn):
    value_dct = {"tp": tp, "fp": fp, "fn": fn}
    result = False
    if check_type(value_dct) == 1 and check_value(value_dct) == 1:
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1score = 2 * (precision * recall) / (precision + recall)
        result = (
            f"""precision is {precision} \nrecall is {recall} \nf1-score is {f1score}"""
        )
    return result
