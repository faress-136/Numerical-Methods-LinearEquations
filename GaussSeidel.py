import string

import numpy as np
import tkinter as tk


def diagonalyDominant(A):
    diagonal = np.diag(np.abs(A))  # Find diagonal coefficients
    sum = np.sum(np.abs(A), axis=1) - diagonal  # Find row sum without diagonal
    if np.all(diagonal > sum):
        return True
    else:
        print("NOT CONVERGING")
        return False


def GaussSeidel(numofEquations, Matrix, my_dict, iterations, epsilon, root):
    sample = open('output.txt', 'w')
    print("Gauss-Seidel", file=sample)
    A = Matrix[:, 0:numofEquations]
    if not diagonalyDominant(A):
        return "Not Diagonally Dominant"

    b = Matrix[:, numofEquations]
    x_old = np.zeros_like(b)
    for i in range(1, iterations):
        x_new = np.zeros_like(x_old)
        print("Iteration {0}: {1}".format(i, x_old), file=sample)
        for j in range(numofEquations):
            s1 = np.dot(A[j, :j], x_new[:j])
            s2 = np.dot(A[j, j + 1:], x_old[j + 1:])
            x_new[j] = (b[j] - s1 - s2) / A[j, j]
        if np.allclose(x_old, x_new, epsilon):
            break
        x_old = x_new

    print("Solution: {0}".format(x_old), file=sample)
    error = np.dot(A, x_old) - b
    print("Error: {0}".format(error), file=sample)

    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

    fun = tk.Label(root, text="Gauss-Seidel", font=("Times New Roman", 15))
    fun.grid(row=numofEquations + 9, columnspan=1, sticky=tk.N + tk.W)
    for i in range(numofEquations):
        ET = char[i] + "  =  " + str(x_old[i]);
        ETl = tk.Label(root, text=ET, font=("Arial", 15)).grid(row=numofEquations + 10 + (i * 2), columnspan=1,
                                                               sticky=tk.N + tk.W, pady=5)
        ER = "Error " + char[i] + "  =  " + str(error[i]);
        ERL = tk.Label(root, text=ER, font=("Arial", 15)).grid(row=numofEquations + 11 + (i * 2), columnspan=4,
                                                               sticky=tk.N + tk.W, pady=5)
