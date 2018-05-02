# At the moment, this is just random code to help do the Viterbi algorithm

import math
import numpy as np

def log2(prob):
    if prob == 0:
        return -float('inf')
    return math.log(prob,2)


z = 0 + log2(1)
inf = -float('inf')

emission_probabilities = {'A0':0.8, 'A1':0.2, 'A2':0,
                        'B0':0, 'B1':0.6, 'B2':0.4,
                        'C0':0.2, 'C1':0, 'C2':0.8
                        }
state_transition_probabilities = {'A':[0.2, 0, 0,4],
                                  'B':[0.8, 0.8, 0],
                                  'C':[0, 0.2, 0.6]
                                  }

state_l = 'C'
symbol_x1 = 0
state_symbol_prob = state_l + str(symbol_x1)
a = 0 + log2(state_transition_probabilities[state_l][0])
b = -.206 + log2(state_transition_probabilities[state_l][1])
c = -2.012 + log2(state_transition_probabilities[state_l][2])

p_symbol = emission_probabilities[state_symbol_prob]
print(p_symbol)

pres = [a, b, c]


print(pres)
x = np.amax(pres)
print(x)
v = p_symbol * x
print(v)

