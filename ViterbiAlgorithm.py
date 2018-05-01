# At the moment, this is just random code to help do the Viterbi algorithm

import math
import numpy as np

def log2(prob):
    if prob == 0:
        return -float('inf')
    return math.log(prob,2)


z = 0 + log2(0)
inf = -float('inf')

a = inf + log2(0.8)
b = inf + log2(0.8)
c = inf + log2(0)

pres = [a, b, c, z]

print(pres)
x = np.amax(pres)
print(x)

