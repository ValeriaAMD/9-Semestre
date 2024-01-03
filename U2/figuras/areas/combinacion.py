def calcular_combi(z, r):
    if not isinstance(z, int) or not isinstance(r, int):
        raise ValueError('Ambos valores deben ser enteros')
    if z < 0 or r < 0:
        raise ValueError('Ambos valores deben ser positivos')
    if r > z:
        raise ValueError('El valor de r no puede ser mayor que z')

    ### Estas lineas definen una función llamada calcular_combinaciones que llama dos variables como z y r. 
    # Se realizan comparaciones para asegurarse de que z y r sean números enteros positivos y que r no sea mayor que z.
    
    resultado = 1           ###Aquí creamos una variable resultado y la inicializamos en 1. Luego, utilizamos un for para iterar desde z 
    for i in range(z, z - r, -1): # hasta z - r + 1, restando 1 en cada iteración. Dentro del bucle, multiplicamos resultadopor los valores de ien cada iteración.
        resultado *= i   # Esto nos da el resultado de todos los números desde n hasta z - r + 1.
    
    for i in range(1, r + 1): # Después, utilizamos otro bucle for para iterar desde 1 hasta r + 1, 
        resultado //= i  
    # incrementando en 1 en cada iteración. Dentro de este segundo bucle, dividimos resultado por los valores de ien cada iteración. 
    # Esto nos permite calcular el resultado de todos los números desde 1 hasta r. 
    
    return resultado
    # Finalmente, se devuelve el valor de resultado.