import sys
def fibonacci(n, memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado=fibonacci(n-1, memo)+fibonacci(n-2, memo)
        memo[n]=resultado
    return resultado
sys.setrecursionlimit(10000)
n = int(input("escoje un numero: "))
print(fibonacci(n))