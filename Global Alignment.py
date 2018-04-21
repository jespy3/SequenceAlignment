import numpy as np
from itertools import combinations_with_replacement

# This is a test matrix
# m = np.array([[1, 2, 3], [4, 5, 6]])
# print(m)

f = open('BLOSUM62.txt', 'r')
lineList = f.read().splitlines()    # list of each line of BLOSUM62 matrix

AA = list('ARNDCQEGHILKMFPSTWYV')               # list of amino acids
AAcombos =  list(combinations_with_replacement(AA, 2)) # initialise list for amino acid combos
BLOSUM = {}                                     # initialise dictionary to contain BLOSUM62 values
#print(AAcombos)
#print(len(AAcombos))

# Accessing each permutation of two amino acids and appending to AAcombos
# for i, ival in enumerate(AA):
#     for j, jval in enumerate(AA):
#         AAcombos.append(ival+jval)

count = 0
for line in lineList:
    #print(line)
    # print(line.split('\t'))
    for num in line.split('\t'):
         print(int(num))
         count += 1
         
    
    print('Next row \n')

print(count)