def Fibonacci(n, memo=None):
    if memo is None:
        memo = {}
        memo[0] = 0
        memo[1] = 1

    if n in memo:
        return memo[n]

    for i in range(2, n + 1):
        if i not in memo:
            memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]

