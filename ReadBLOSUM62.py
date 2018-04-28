""" 
Separate file containing the BLOSUM class to read the BLOSUM62 matrix from BLOSUM62.txt
"""

class BLOSUM:

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

        return lineList