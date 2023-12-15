import math

def gauss_seidel(A, b, x0, tol=1e-10, max_iterations=1000):
    n = len(A)
    x = x0.copy()

    for k in range(max_iterations):
        x_old = x.copy()

        for i in range(n):
            sum = 0
            for j in range(n):
                if j != i:
                    sum += A[i][j] * x[j]
            x[i] = (b[i] - sum) / A[i][i]
        
        if max(abs(x[i] - x_old[i]) for i in range(n)) < tol:
            return x
        #print(x)
    return x




A=[[3,1,1],[3,1,-5],[1,3,-1]]
b=[5,-1,3]


print(gauss_seidel(A,b,[2,2,1]))