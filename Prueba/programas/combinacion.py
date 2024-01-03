from programas.factorial import factorial
def combinacion(n, r):
    resultado = factorial(n) / (factorial(r) * factorial(n - r))
    return resultado
