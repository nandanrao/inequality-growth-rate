import math

def cast(n):
    return 0 if (math.isnan(n) or math.isinf(n)) else n

def growth(y_t, y_prev):
    try:
        return (y_t**2)/float(y_prev) if y_t else 0 # 0 if y_t is 0
    except ZeroDivisionError:
        return y_t**2/.1 # infinite growth, how do we handle it????

def reducer(a, b):
    curr, prev = b
    running_growth, total = a
    return (running_growth + growth(cast(curr), cast(prev)), total + cast(curr))

def collector(l):
    return reduce(reducer, l, (0,0))

def average_growth(l):
    summed_growth, total = collector(l)
    try:
        return math.log(summed_growth / total)
    except ZeroDivisionError:
        return 0

# test wtih nan's and realistic data
# look into what's going on with the nan's -- how to asses the accuracy of that data???
