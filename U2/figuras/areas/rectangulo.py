
def area_rectangulo(b,a):
    ###Este código define una función llamada area_rectanguloque calcula el área de un rectángulo.
    # La función toma dos parámetros: bque representa la base del rectángulo, y aque representa la altura del rectángulo.
    # A continuación, se realizan comparaciones para asegurarse de que las variables 
    if not isinstance(b,(int,float)):                    
        raise ValueError('Base debe ser numerico')     #un número entero o de punto flotante
    if not isinstance(a,(int,float)):
        raise ValueError('Altura debe ser numerico')    #es un número entero o de punto flotante
    if b < 0:
        raise ValueError('Base debe ser un numero positivo')  #omprueba si b es menor que cero
    if a < 0: 
        raise ValueError('Altura debe ser un numero')  #comprueba si a es menor que cero
    return b*a
    ###Si pasan todas las validaciones, la función calcula el área del rectángulo multiplicando la base por la altura y devuelve el resultado.    