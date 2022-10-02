import math

# Calculates the arithmetic mean of a list of scores with a given weight


def arithmeticMean(items):
    return sum(item[0] * item[1] for item in items) / sum(item[1] for item in items) if items else 0


SQRT2 = 1.4142135623730951


def internalErf_(x):
    # erf(-x) = -erf(x);
    sign = -1 if x < 0 else 1
    x = abs(x)
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429
    p = 0.3275911
    t = 1 / (1 + p * x)
    y = t * (a1 + t * (a2 + t * (a3 + t * (a4 + t * a5))))
    return sign * (1 - y * math.exp(-x * x))


def QUANTILE_AT_VALUE(curve, value):
    median = curve['median']
    podr = curve['podr'] if 'podr' in curve else derivePodrFromP10(
        median, curve['p10'])
    location = math.log(median)
    logRatio = math.log(podr / median)
    shape = math.sqrt(1 - 3 * logRatio -
                      math.sqrt((logRatio - 3) * (logRatio - 3) - 8)) / 2
    standardizedX = (math.log(value) - location) / (SQRT2 * shape)
    return (1 - internalErf_(standardizedX)) / 2


def internalErfInv_(x):
    # erfinv(-x) = -erfinv(x);
    sign = -1 if x < 0 else 1
    a = 0.147
    log1x = math.log(1 - x*x)
    p1 = 2 / (math.pi * a) + log1x / 2
    sqrtP1Log = math.sqrt(p1 * p1 - (log1x / a))
    return sign * math.sqrt(sqrtP1Log - p1)


def VALUE_AT_QUANTILE(curve, quantile):
    median = curve['median']
    podr = curve['podr'] if 'podr' in curve else derivePodrFromP10(
        median, curve['p10'])
    location = math.log(median)
    logRatio = math.log(podr / median)
    shape = math.sqrt(1 - 3 * logRatio -
                      math.sqrt((logRatio - 3) * (logRatio - 3) - 8)) / 2
    return math.exp(location + shape * SQRT2 * internalErfInv_(1 - 2 * quantile))


def derivePodrFromP10(median, p10):
    u = math.log(median)
    shape = abs(math.log(p10) - u) / (SQRT2 * 0.9061938024368232)
    inner1 = -3 * shape - math.sqrt(4 + shape * shape)
    podr = math.exp(u + shape/2 * inner1)
    return podr
