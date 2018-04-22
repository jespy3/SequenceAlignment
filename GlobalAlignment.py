import numpy as np
from itertools import combinations_with_replacement

# This is a test matrix
# m = np.array([[1, 2, 3], [4, 5, 6]])
# print(m)

f = open('BLOSUM62.txt', 'r')
lineList = f.read().splitlines()    # list of each line of BLOSUM62 matrix

AA = list('ARNDCQEGHILKMFPSTWYV')               # list of amino acids
AAcombos = list(combinations_with_replacement(AA, 2)) # initialise list for amino acid combos
BLOSUM = {}                                     # initialise dictionary to contain BLOSUM62 values



# Constructs the dictionary for BLOSUM62
for i, line in enumerate(lineList):
    AAindex = i     # Keeps track of index of AAcombos in how 'BLOSUM62.txt' is read. Acts as sum variable
    for j, num in enumerate(line.split('\t')):
        if j != 0:
            AAindex += (len(lineList)-j)    # updating to correct AAcombos index
        key = AAcombos[AAindex]
        BLOSUM[key] = int(num)

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

class AminoAcid:


    def __init__(self, AAcombo):
        self.AAcombo = AAcombo

        AAorder = 'ARNDCQEGHILKMFPSTWYV'
        self.orderValue = {}  # to assign each amino acid with an orderValue
        for i, AA in enumerate(AAorder):
            self.orderValue[AAorder[i]] = i

    def OrderAAs(self):
        '''
        Re-arranges the order of the amino acid combination for searching in the BLOSUM62 matrix.

        :param AAcombo: string of two letters according to amino acids, in any order
        :return: string rearranged in the amino acid order 'ARNDCQEGHILKMFPSTWYV'
        '''

        firstAA = self.AAcombo[0]
        secondAA = self.AAcombo[1]
        if self.orderValue[firstAA] > self.orderValue[secondAA]:
            self.AAcombo = self.AAcombo[::-1]
        return self.AAcombo

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
            matrix[i][j] = np.amax(predecessors)

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
    X_line = ""
    Y_line = ""
    (i, j) = (len(X)+1, len(Y)+1)
    # while (i, j) != (0,0):
    #     if traceback(i, j) == (i-1, j-1):





X = 'GRQTAGL'
Y = 'GTAYDL'
d = 8
global_alignment_linear(X, Y, d)
test = 'LL'
x = getBLOSUMscore(test[0], test[1])
#print(x)
#print(6+5-3-3-5-6-2)
