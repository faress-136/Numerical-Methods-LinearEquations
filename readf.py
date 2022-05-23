from Gaussian import Gaussian
from os import read
import numpy as np
from GaussianJordan import GaussianJordan
from GaussSeidel import GaussSeidel
from LUDecomp import LUDecomp


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def readfromFile(filename , root):
    try:
        inputFile = open(filename, 'r')
        numofEquations = (int)(inputFile.readline().replace('\n', ''))
        Matrix = np.tile(0.0, (numofEquations, numofEquations + 1))
        function = inputFile.readline()
        my_dict = dict()
        index = 0
        lines = ""
        function = function.replace('\n', '')
        for i in range(numofEquations):
            lines += inputFile.readline()

        for c in lines:
            if (not (c.isdigit() or c == '+' or c == '-' or c == '.' or c == '*' or c == ' ' or c == '\n') and (
                    not c in my_dict)):
                my_dict[c] = index
                index += 1

        lines = lines.replace(" ", "")
        tokens = lines.split('\n')
        for i in range(numofEquations):
            tokens[i] = tokens[i].replace("-", "+-")
            each = tokens[i].split('+')
            for j in range(len(each)):
                if (len(each[j]) == 0):
                    continue
                if (isfloat(each[j])):
                    Matrix[i][numofEquations] = float(each[j])
                elif (len(each[j]) == 1):
                    Matrix[i][my_dict[each[j][0]]] = 1
                elif (len(each[j]) == 2):
                    Matrix[i][my_dict[each[j][1]]] = -1
                else:
                    Matrix[i][my_dict[each[j][-1]]] = float(each[j][0:len(each[j]) - 2])
        for i in range(numofEquations):
            Matrix[i][numofEquations] *= -1

        if function == "Gaussian-elimination":
            Gaussian(numofEquations, Matrix, my_dict,root)
        elif function == "Gaussian-Jordan":
            GaussianJordan(numofEquations, Matrix, my_dict,root)
        elif function == "Gauss-Seidel":
            GaussSeidel(numofEquations, Matrix, my_dict, 50, 0.00001,root)
        elif function == "LU-decomposition":
            LUDecomp(numofEquations, Matrix, my_dict,root)
    except:
        print("Error", "Can't read from file")
