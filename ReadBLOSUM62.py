""" 
Separate file containing the BLOSUM class to read the BLOSUM62 matrix from BLOSUM62.txt
"""

from itertools import combinations_with_replacement

class BLOSUM:

    AA = list('ARNDCQEGHILKMFPSTWYV')  # list of amino acids
    AAcombos = list(combinations_with_replacement(AA, 2))  # initialise list for amino acid combos

    def __init__(self):
        """ Initialises the dictionary to read the matrix
        
        """
        self.matrix = {}

    def convert_to_dictionary(self, filename):
        """ Reads matrix .txt file and fills in dictionary
        
        :param filename: .txt file of the BLOSUM matrix
        :return: dictionary to look up values of the BLOSUM matrix
        """

        f = open('BLOSUM62.txt', 'r')
        lineList = f.read().splitlines()

        # Constructs the dictionary for BLOSUM62
        for i, line in enumerate(lineList):
            AAindex = i  # Keeps track of index of AAcombos in how 'BLOSUM62.txt' is read. Acts as sum variable
            for j, num in enumerate(line.split('\t')):
                if j != 0:
                    AAindex += (len(lineList) - j)  # updating to correct AAcombos index
                key = self.AAcombos[AAindex]
                self.matrix[key] = int(num)


        return self.matrix