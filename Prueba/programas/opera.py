from programas.combinacion import combinacion

def validar_numeros(n, r):
    if not isinstance(n,(int,float)) or not isinstance(r,(int,float)):
        raise ValueError('n y r no deben ser de tipo string')
    if isinstance(n, (int,float)) or isinstance(r, (int,float)):
        raise ValueError('n y r deben ser números enteros No de punto flotante')
    if n < r:
        raise ValueError('n debe ser mayor o igual que r')
    if n < 0 or r < 0:
        raise ValueError('n y r deben ser números no negativos')

try:
    n = float(input("Ingrese el valor de n: "))
    r = float(input("Ingrese el valor de r: "))
    
    validar_numeros(n, r)
    
    n = int(n)
    r = int(r)
    
    resultado_combinacion = combinacion(n, r)
    print(f"{n}C{r} = {resultado_combinacion}")
except ValueError as e:
    print(f"Error: {e}")