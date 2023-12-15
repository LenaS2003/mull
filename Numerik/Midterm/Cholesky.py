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
            Zeile.append(0)
        Matrix.append(Zeile)
    return Matrix

def Vector(n):
    vec = []
    for i in range (0,n):
        vec.append(0)
    return vec


def cholesky(A):
    n = len(A)

    L=Matrix(n)
    for k in range (0,n):
        # first we calculate the element on the diagonal
        sum = 0
        for s in range(0,k):
            sum=sum+(L[k][s]*L[k][s])
        L[k][k]=math.sqrt(A[k][k]-sum)
        # then we calculate the lower triangular matrix
        for i in range(k,n):
            sum = 0
            for s in range(0,k):
                sum = sum + L[i][s]*L[k][s]
            L[i][k]=(A[i][k]-sum)/L[k][k]
    return L

def transpose(A):
    L=[]
    #we go through the lines
    for i in range(0,len(A)):
        line=[]
        for j in range(0,len(A)):
            line.append (A[j][i])
        L.append(line)
    return L

def solve(A,b):
    n=len(A)
    L = cholesky(A)
    L2 = transpose(L)
    
    # we want to print the matrices:
    #matrix L
    print("L")
    Ausgabe(L)
    #matrix R
    print("A")
    Ausgabe(L2)


    #first we solve Lx=b
    x = Vector(len(A))
    for i in range (0, len(A)):
        sum=0
        for j in range(0,i):
            sum+=L[i][j]*x[j]
        x[i] = (b[i] - sum)/L[i][i]
    # then we solve Uy=x
    print(x)
    y=Vector(len(A))
    for i in range(len(A)-1,-1,-1):
        sum=0
        for j in range(len(A)-1,i,-1):
            sum+=L2[i][j]*y[j]
        y[i] = (x[i] -sum)/L2[i][i]
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
#print (len(A))
L=cholesky(A)
print("Print matrix L:")
Ausgabe(L)
#print("Print matrix L:")
#Ausgabe (L)
"""

#solve the linear system
b = [7.5,-8.68,-0.24]
print(solve(A,b))