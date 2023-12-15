def gauss(A, b):
    n = len(b)
    
    for i in range(n):
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]
        
        pivot = A[i][i]
        for j in range(i, n):
            A[i][j] /= pivot
        b[i] /= pivot
        
        for k in range(i+1, n):
            factor = A[k][i]
            for j in range(i, n):
                A[k][j] -= factor * A[i][j]
            b[k] -= factor * b[i]
            
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= A[i][j] * x[j]
    
    return x


A=[[3,1,1],[3,1,-5],[1,3,-1]]
b=[5,-1,3]


print(gauss(A,b))