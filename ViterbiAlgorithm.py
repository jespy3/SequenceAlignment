# At the moment, this is just random code to help do the Viterbi algorithm

import math
import numpy as np

base = 2
z = 0 + math.log(1, base)

a = -4.644 + -float('inf')
b = -0.644 + math.log(0.2, base)
c = -2.644 + math.log(0.6, base)
pres = [a, b, c]

print(pres)
x = np.amax(pres)
print(x)