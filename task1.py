'''Вычислить число c заданной точностью d

Пример:

- при d = 3, π = 3.141'''

import sys
import math
from decimal import *
from math import factorial


def chudnovsky(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)
                                                         * (factorial(3*k))) * (13591409+545140134*k)/(640320**(3*k)))
        k += 1
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


d = int(input("введите d:  "))
getcontext().prec = d+1  #+1, потому что у нас всегда есть одна цифра перед запятой, поэтому нужно отдавать на одну цифру больше
num_Pi = chudnovsky(d)
print('при d =', d, ', Pi =', num_Pi)
