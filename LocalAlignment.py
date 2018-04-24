##Local Optimal Alignment
import numpy as np

def local_alignment(X, Y):

    # Setting size of matrix
    # setting to zeros also completes initialisation step
    matrix = np.zeros((len(X) + 1, len(Y) + 1))

    print(matrix)

X = 'GRQTAGL'
Y = 'GTAYDL'
local_alignment(X, Y)