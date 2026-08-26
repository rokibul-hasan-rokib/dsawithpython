def sumOfFirst(n):
    if n == 0:
        return 0
    return n + sumOfFirst(n - 1)

print(sumOfFirst(5))