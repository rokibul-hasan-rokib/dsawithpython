def Febonacci(n):
    if n<=1:
        return n
    return Febonacci(n-1) + Febonacci(n-2)
    
print(Febonacci(6))