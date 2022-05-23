import tkinter as tk

import numpy as np
from Gaussian import Gaussian


def LUDecomp(numofequations, matrix, my_dict , root):
    A = matrix[:, 0:numofequations]
    B = matrix[:, numofequations]
    L, U = LU(numofequations, A)
    Y = np.zeros(numofequations)
    X = np.zeros(numofequations)
    Y[0] = B[0] / L[0][0] * 1.0

    for k in range(1, numofequations):
        sum = 0
        for j in range(0, k):
            sum += L[k][j] * Y[j]
        Y[k] = 1.0 / L[k][k] * (B[k] - sum)

    X[numofequations - 1] = Y[numofequations - 1] / (U[numofequations - 1][numofequations - 1]) * 1.0

    for k in range(numofequations - 2, -1, -1):
        sum = 0
        for j in range(k + 1, numofequations, 1):
            sum += U[k][j] * X[j]
        X[k] = 1.0 / U[k][k] * (Y[k] - sum)

    sample = open('output.txt', 'w')
    print("LU decomposition", file=sample)
    fun = tk.Label(root, text="LU decomposition", font=("Times New Roman", 15))
    fun.grid(row=numofequations + 9, columnspan=1, sticky=tk.N + tk.W)
    for i in range(numofequations):
        print("{0} = {1}".format(list(my_dict.keys())[list(my_dict.values()).index(i)], X[i]), file=sample)
        ET = list(my_dict.keys())[list(my_dict.values()).index(i)] + "  =  " + str(X[i])
        ETl = tk.Label(root, text=ET, font=("Arial", 15)).grid(row=numofequations + 10 + i, columnspan=1,
                                                               sticky=tk.N + tk.W, pady=5)

    return X


def LU(numofequations, A):
    lower = np.identity(numofequations)
    for k in range(0, numofequations, 1):
        for i in range(k + 1, numofequations, 1):
            ratio = A[i][k] / A[k][k] * 1.0
            lower[i][k] = ratio
            for j in range(0, numofequations, 1):
                A[i][j] = A[i][j] - ratio * A[k][j]
    return lower, A
