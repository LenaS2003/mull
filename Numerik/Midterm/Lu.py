import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
    
#Methode zum Ausgeben einer Matrix A:
def Ausgabe(A):
    n = len(A)
    for j in range(0,n):
        for i in range(0,n):
            print(A[j][i])
        print('\\n')
        
#Matrix aus Übungsaufgabe zum testen:

def Matrix(n):
    Matrix=[]

    for x in range (0,n):
        Zeile=[]
        for y in range (0,n):
            if x==y:
                Zeile.append(1)
            else:
                Zeile.append(0)
        Matrix.append(Zeile)
    return Matrix

def Vector(n):
    vec = []
    for i in range (0,n):
        vec.append(0)
    return vec


def LU_factorisation(A):
    n=len(A)
    B=Matrix(n)
    for x in range (1,n):
        for y in range (0,x):
            if A[y][y]==0:
                #we have to switch rows
                for q in range (y,n):
                    if A[q][y]!=0:
                        for r in range(0,n):
                            t= A[y][r]
                            A[y][r]=A[x][r]
                            A[x][r]=t
                        break
            q = A[x][y]/A[y][y]
            B[x][y]=q
            for z in range(0,n):
                A[x][z]= A[x][z]-A[y][z]*q
                #B[x][z]=-q


    return B

def solve(A,b):
    n=len(A)
    L = LU_factorisation(A)
    
    # we want to print the matrices:
    #matrix L
    print(L)
    Ausgabe(L)
    #matrix R
    print(A)
    Ausgabe(A)


    #first we solve Lx=b
    x = Vector(len(A))
    for i in range (0, len(A)):
        sum=0
        for j in range(0,i):
            sum+=L[i][j]*x[j]
        x[i] = b[i] - sum
    # then we solve Uy=x
    y=Vector(len(A))
    for i in range(len(A)-1,-1,-1):
        sum=0
        for j in range(len(A)-1,i,-1):
            sum+=A[i][j]*y[j]
        y[i] = (x[i] -sum)/A[i][i]
    return y






A = Matrix(3)
A[0][0] = 6.25
A[0][1] = -1
A[0][2] = 0.5
A[1][0] = -1
A[1][1] = 5
A[1][2] = 2.12
A[2][0] = 0.5
A[2][1] = 2.12
A[2][2] = 3.6
"""
print (len(A))
L= LU_factorisation(A)
print("Print matrix R:")
Ausgabe(A)
print("Print matrix L:")
Ausgabe (L)
"""

print("Solve the linear system:")
b = [7.5,-8.68,-0.24]
x = solve(A,b)
print(x)

"""
A = Matrix(4)
A[0][0] = 2
A[0][1] = 1
A[0][2] = 1
A[0][3] = -2
A[1][0] = 2
A[1][1] = 2
A[1][2] = -2
A[1][3] = -1
A[2][0] = 10
A[2][1] = 4
A[2][2] = 23
A[2][3] = -8
A[3][0] = -6
A[3][1] = -2
A[3][2] = 4
A[3][3] = 6

L= LU_factorisation(A)
print("Print matrix R:")
Ausgabe(A)
print("Print matrix L:")
Ausgabe (L)
"""