def MatrixPower(M, n):
    if n == 1:
        return M
    if n % 2 == 0:  
        half = MatrixPower(M, n // 2)
        return MatrixMultiply(half, half)
    else:  
        return MatrixMultiply(M, MatrixPower(M, n - 1))

def MatrixMultiply(A, B):
    return [
        [A[0][0]*B[0][0] + A[0][1]*B[1][0],
         A[0][0]*B[0][1] + A[0][1]*B[1][1]],
        [A[1][0]*B[0][0] + A[1][1]*B[1][0],
         A[1][0]*B[0][1] + A[1][1]*B[1][1]]
    ]

def Fibonacci(n):
    if n <= 1:
        return n
    M = [[1, 1], [1, 0]]
    result = MatrixPower(M, n)
    return result[0][1]

