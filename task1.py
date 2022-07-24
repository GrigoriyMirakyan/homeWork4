'''Вычислить число c заданной точностью d

Пример:

- при d = 3, π = 3.141'''

import math
from decimal import *


def bbp(n):
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(1)/(16**k))*((Decimal(4)/(8*k+1)) -
                                    (Decimal(2)/(8*k+4))-(Decimal(1)/(8*k+5))-(Decimal(1)/(8*k+6)))
        k += 1
    return pi


d = int(input("введите d:  "))
# d+1, потому что у нас всегда есть одна цифра перед запятой, поэтому нужно отдавать на одну цифру больше
getcontext().prec = d+1
num_Pi = bbp(d)
print('при d =', d, ', Pi =', num_Pi)
