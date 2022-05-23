import tkinter as tk


def Gaussian(nofequations, matrix, my_dict, root):
    x = [0] * nofequations
    for k in range(0, nofequations, 1):
        for i in range(k + 1, nofequations, 1):
            ratio = matrix[i][k] / matrix[k][k] * 1.0
            for j in range(0, nofequations + 1, 1):
                matrix[i][j] = matrix[i][j] - ratio * matrix[k][j]
                # print(matrix[i][j])
    # print(matrix)
    x[nofequations - 1] = matrix[nofequations - 1][nofequations] / (matrix[nofequations - 1][nofequations - 1]) * 1.0

    for k in range(nofequations - 2, -1, -1):
        sum = 0

        for j in range(k + 1, nofequations, 1):
            sum += matrix[k][j] * x[j]

        x[k] = 1.0 / matrix[k][k] * (matrix[k][nofequations] - sum)

    sample = open('output.txt', 'w')
    print("Gaussian-Elimination", file=sample)
    fun = tk.Label(root, text="Gauss-Elimination", font=("Times New Roman", 15))
    fun.grid(row=nofequations + 9, columnspan=1, sticky=tk.N + tk.W)
    for i in range(nofequations):
        print("{0} = {1}".format(list(my_dict.keys())[list(my_dict.values()).index(i)], x[i]), file=sample)
        print(list(my_dict.keys())[list(my_dict.values()).index(i)])

        ET = list(my_dict.keys())[list(my_dict.values()).index(i)] + "  =  " + str(x[i])
        ETl = tk.Label(root, text=ET, font=("Arial", 15)).grid(row=nofequations + 10 + i, columnspan=1,
                                                               sticky=tk.N + tk.W, pady=5)
