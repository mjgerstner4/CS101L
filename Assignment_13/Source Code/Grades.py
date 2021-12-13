import math

def total(values:list):
    total = 0
    for item in values:
        total = total + item
    return total

def average(values:list):
    if len(values) == 0:
        return math.nan
    return total(values) / len(values)


def median(values:list):
    values = sorted(values)
    length = len(values)
    if values == []:
        raise ValueError
    elif length % 2 == 0:
        mid1 = int((length/2) - 1)
        mid2 = int(length/2)
        median = float(values[mid1] + values[mid2])/2
        return median
    else:
        median = values[int((length-1)/2)]
        return median

        