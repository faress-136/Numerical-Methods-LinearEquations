from tkinter import *
import tkinter as tk
from Gaussian import Gaussian
from os import read
import numpy as np
from GaussianJordan import GaussianJordan
from GaussSeidel import GaussSeidel
from LUDecomp import LUDecomp
from readf import isfloat
import readf as rf

root = tk.Tk()
root.geometry("800x600")


def draw(NumberOfEquations, FileEntry):
    if chosen.get() == "Read File":
        rf.readfromFile(FileEntry.get(), root)
        return
    Equations = []
    NoEQ = int(NumberOfEquations.get())
    function = chosen.get()
    Label(root, text=chosen.get(), font=("Times New Roman", 15)).grid(row=3, column=0, sticky=tk.N + tk.W, pady=3)

    for i in range(NoEQ):
        text = " Equation " + str(i + 1)
        Eq = Label(root, text=text)
        Eq.grid(row=4 + i, column=0, sticky=tk.N + tk.W, pady=3)
        Equations.append(Entry(root, bd=5, width=30))
        Equations[i].grid(row=4 + i, column=1, sticky=tk.N + tk.W, pady=3)

    Initial = Label(root, text="Initial Condition ").grid(row=5 + NoEQ, column=0, sticky=tk.N + tk.W, pady=3)
    Initial = Entry(root, bd=5, width=30)
    Initial.grid(row=5 + NoEQ, column=1, sticky=tk.N + tk.W, pady=3)
    Equations.append(Initial.get())

    MIL = Label(root, text="MAX Iterations: ").grid(row=7 + NoEQ, column=0, sticky=tk.N + tk.W, pady=3)
    MIE = Entry(root, bd=5, width=30)
    MIE.grid(row=7 + NoEQ, column=1, sticky=tk.N + tk.W, pady=3)
    MIE.insert(0, "50")

    EL = Label(root, text="Epsilon: ").grid(row=7 + NoEQ, column=2, sticky=tk.N + tk.W, pady=3)
    EE = Entry(root, bd=5, width=30)
    EE.grid(row=7 + NoEQ, column=3, sticky=tk.N + tk.W, pady=3)
    EE.insert(0, 0.00001)
    Go = Button(root, text="Choose", command=lambda: run(NoEQ, function, Equations, MIE, EE))
    Go.grid(row=8 + NoEQ, column=2, sticky=tk.N + tk.W, pady=3)


def run(NoEQ, function, Equations, MIE, EE):
    Matrix = np.tile(0.0, (NoEQ, NoEQ + 1))
    my_dict = dict()
    index = 0
    lines = ""
    for i in range(NoEQ):
        lines += Equations[i].get()

    for c in lines:
        if (not (c.isdigit() or c == '+' or c == '-' or c == '.' or c == '*' or c == ' ' or c == '\n') and (
                not c in my_dict)):
            my_dict[c] = index
            index += 1

    lines = lines.replace(" ", "")
    tokens = lines.split('\n')
    for i in range(NoEQ):
        tokens[i] = tokens[i].replace("-", "+-")
        each = tokens[i].split('+')
        for j in range(len(each)):
            if len(each[j]) == 0:
                continue
            if isfloat(each[j]):
                Matrix[i][NoEQ] = float(each[j])
            elif len(each[j]) == 1:
                Matrix[i][my_dict[each[j][0]]] = 1
            elif len(each[j]) == 2:
                Matrix[i][my_dict[each[j][1]]] = -1
            else:
                Matrix[i][my_dict[each[j][-1]]] = float(each[j][0:len(each[j]) - 2])
    for i in range(NoEQ):
        Matrix[i][NoEQ] *= -1

    if function == "Gaussian-elimination":
        Gaussian(NoEQ, Matrix, my_dict, root)
    elif function == "Gaussian-jordan":
        GaussianJordan(NoEQ, Matrix, my_dict, root)
    elif function == "Gauss-Seidel":
        GaussSeidel(NoEQ, Matrix, my_dict, MIE.get(), EE.get(), root)
    elif function == "LU-decomposition":
        LUDecomp(NoEQ, Matrix, my_dict, root)


options = [
    "Gaussian-elimination",
    "Gaussian-jordan",
    "Gauss-Seidel",
    "LU-decomposition",
    "Read File",
]

chosen = StringVar()

chosen.set("Choose Method")

methodLabel = Label(root, text="Method        :", font=("Times New Roman", 15)).grid(row=0, column=0,
                                                                                     sticky=tk.N + tk.W, pady=5)
drop = OptionMenu(root, chosen, *options)
drop.grid(row=0, column=1, sticky=tk.N + tk.W, pady=5)
EquationsLabel = Label(root, text="# Equations :", font=("Times New Roman", 15)).grid(row=1, column=0,
                                                                                      sticky=tk.N + tk.W, pady=5)
EquationsEntry = Entry(root, bd=2, width=10, font=("Arial", 15))
EquationsEntry.grid(row=1, column=1, sticky=tk.N + tk.W, pady=5)
FileLabel = Label(root, text="File Name   :", font=("Times New Roman", 15)).grid(row=2, column=0, sticky=tk.N + tk.W,
                                                                                 pady=5)
FileEntry = Entry(root, bd=2, width=30, font=("Arial", 15))
FileEntry.grid(row=2, column=1, sticky=tk.N + tk.W, pady=5)

button = Button(root, text="Select", font=("Arial", 10), command=lambda: draw(EquationsEntry, FileEntry))
button.grid(row=3, column=3, sticky=tk.N + tk.W)

root.mainloop()
