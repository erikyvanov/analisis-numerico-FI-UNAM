from sympy import Matrix

def backsubs(A: Matrix):
    n = A.shape[0]
    x = Matrix([0 for _ in range(n)])

    x[n-1] = A[n-1, n]/A[n-1, n-1]
 
    for i in range(n-2,-1,-1):
        x[i] = A[i, n]
        
        for j in range(i+1,n):
            x[i] = x[i] - A[i, j]*x[j]
        
        x[i] = x[i]/A[i, i]

    return x

def gausselim(A: Matrix):
    n = A.shape[0]
    A = A.copy()

    for i in range(n):
        for j in range(i+1, n):
            ratio = A[j, i]/A[i, i]
            for k in range(n+1):
                A[j, k] = A[j, k] - ratio * A[i, k]

    return A