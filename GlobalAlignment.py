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
    AAcombo = firstAA + secondAA
    AAcombo = orderAAs(AAcombo)
    tuple = (AAcombo[0],AAcombo[1])
    return BLOSUM[tuple]

test = 'CD'
x = getBLOSUMscore(test[0], test[1])
print(x)