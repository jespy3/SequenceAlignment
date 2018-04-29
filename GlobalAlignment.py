import numpy as np
import ReadBLOSUM62
from itertools import combinations_with_replacement

# Sheen was here
# Josh was here too
# This is a test matrix
# m = np.array([[1, 2, 3], [4, 5, 6]])
# print(m)

test = ReadBLOSUM62.BLOSUM()
BLOSUM = test.convert_to_dictionary('BLOSUM62.txt')


print(BLOSUM)

# Establishing amino acid order
AAorder = 'ARNDCQEGHILKMFPSTWYV'
orderValue = {}                         # to assign each amino acid with an orderValue
for i, AA in enumerate(AAorder):
    orderValue[AAorder[i]] = i          # constructing orderValue dictionary

def orderAAs(AAcombo):
    '''
    Re-arranges the order of the amino acid combination for searching in the BLOSUM62 matrix.

    :param AAcombo: string of two letters according to amino acids, in any order
    :return: string rearranged in the amino acid order 'ARNDCQEGHILKMFPSTWYV'
    '''

    firstAA = AAcombo[0]
    secondAA = AAcombo[1]
    if orderValue[firstAA] > orderValue[secondAA]:
        AAcombo = AAcombo[::-1]               # Reverses AAcombo order if not in order
    return AAcombo

def getBLOSUMscore(firstAA, secondAA):
    """
    Returns the similarity score of two amino acids.

    :param firstAA: string of one letter according to an amino acid, usually from the first AA sequence.
    :param secondAA: string of one letter according to an amino acid, usually from the second AA sequence.
    :return: returns BLOSUM62 score of the amino acid similarity.
    """
    AAcombo = firstAA + secondAA
    AAcombo = orderAAs(AAcombo)
    tuple = (AAcombo[0],AAcombo[1])
    return BLOSUM[tuple]





def global_alignment_linear(X, Y, d):
    """
    Builds an optimal alignment from two strings of amino acids X and Y with a linear gap penalty

    Implementation of the Needleman-Wunsch algorithm.
    :param X: 1st string of amino acids
    :param Y: 2nd string of amino acids
    :param d: linear gap penalty
    :return: prints optimal alignment, and returns a similarity score of X and Y
    """

    # Setting size of matrix
    matrix = np.zeros((len(X)+1, len(Y)+1))

    longerString = X if len(X) >= len(Y) else Y
    # initialising first row and first column
    for i in range(len(longerString)+1):
        try:
            matrix[0][i] = -i * d   # fill row value if index exists
        except IndexError:
            pass                    # pass if index not exists
        try:
            matrix[i][0] = -i * d   # fill row value if index exists
        except IndexError:
            pass                    # pass if index not exists

    traceback = {}  # Tracks which cell (i', j') was the maximising pair of (i, j)
    # scoring each possible letter alignment
    for i, row in enumerate(matrix):
        if i == 0:      # skip first row
            continue
        for j, score in enumerate(row):
            if j == 0:  # skip first column
                continue
            predecessors = np.array([
                                        -float('inf'),
                                        matrix[i][j - 1] - d,
                                        matrix[i - 1][j] - d,
                                        matrix[i-1][j-1] + getBLOSUMscore(X[i-1], Y[j-1])
                                    ]
            )
            max_predecessor = np.amax(predecessors)
            matrix[i][j] = max_predecessor

            # accessing each predecessor that gives the maximum score per cell
            print(np.argwhere(predecessors == max_predecessor).flatten().tolist())

            # The following finds a location tuple relative to the current cell tuple (i, j) to find
            #   the maximising pair from the predecessors.
            maximisingPairLocation = np.unravel_index(np.argmax(predecessors), (2, 2))
            traceback[(i, j)] = tuple(
                np.subtract(
                    (i, j),
                    maximisingPairLocation
                )
            )

    print(matrix)

    # Printing the optimal alignment of X and Y
    change_line = ""
    X_line = ""
    Y_line = ""
    (i, j) = (len(X), len(Y))
    while (i, j) != (0,0):
        if traceback[(i, j)] == (i-1, j-1):     # if a match/replacement
            X_line += X[i-1]
            Y_line += Y[j-1]
            change_line += 'M' if X[i-1] == Y[j-1] else 'R'
        elif traceback[(i,j)] == (i-1, j):      # if a gap in Y
            X_line += X[i-1]
            Y_line += '-'
            change_line += 'D'
        else:                                   # if a gap in X
            X_line += '-'
            Y_line += Y[j-1]
            change_line += 'I'
        (i, j) = traceback[(i, j)]
    X_line = X_line[::-1]   # X_line and Y_line reversed because they were
    Y_line = Y_line[::-1]   #   constructed in reverse order.
    change_line = change_line[::-1]


    optimalAlignment = f"{'Change = ':>9}{change_line}\n" \
                       f"{'X = ':>9}{X_line}\n" \
                       f"{'Y = ':>9}{Y_line}"
    print(optimalAlignment)






X = 'GRQTAGL'
Y = 'GTAYDL'
d = 8
global_alignment_linear(X, Y, d)
test = 'ME'
x = getBLOSUMscore(test[0], test[1])
print(x)
#print(6+5-3-3-5-6-2)
