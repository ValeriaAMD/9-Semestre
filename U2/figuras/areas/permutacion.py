def calcular_perm(n, r):
    if not isinstance(n, int) or not isinstance(r, int):
        raise ValueError('Ambos valores deben ser enteros')
    if n < 0 or r < 0:
        raise ValueError('Ambos valores deben ser positivos')
    if r > n:
        raise ValueError('El valor de r no puede ser mayor que n')
    
    ###Estas primeras líneas definen una función calcular_permutaciones
    # que toma dos variableds: n y r. Luego, se realizan comparaciones para 
    # asegurarse de que n y r sean números enteros positivos y que r no sea mayor que n.
    
    resultado = 1       ###Aquí creamos una variable resultadoy la inicializamos en 1. Luego, utilizamos un 
    for i in range(n, n - r, -1): # for para iterar desde n hasta n - r + 1, restando 1 en cada iteración. Dentro del bucle, multiplicamos 
        resultado *= i # resultado por los valores de i en cada iteración. Esto nos da el resultado de todos los números desde n hasta n - r + 1.
    
    return resultado  # Finalmente, se devuelve el valor de resultado.