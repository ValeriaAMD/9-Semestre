from Operaciones.suma import suma
from Operaciones.resta import resta
from Operaciones.multiplicacion import multiplicacion
from Operaciones.division import division

a=int(input("Ingresa un Numero: "))
b=int(input("Ingresa otro Numero: "))

eleccion = 0

while eleccion!= 6:
    print("""
          1) Suma
          2) Resta
          3) Multiplicacion
          4) Division
          5) Cambio de Valores
          6) Salir
          """)
    
    eleccion = int(input("Selecciona una opción (1/2/3/4/5/6): "))

    if eleccion == 1:
        print("El Resultado de la suma es:")
        print(suma(a,b))
          
    elif eleccion == 2:
       print("El Resultado de la resta es:")
       print(resta(a,b))

    elif eleccion == 3:
       print("El Resultado de la multiplicacion es:")
       print(multiplicacion(a,b))

    elif eleccion == 4:
        print("El Resultado de la division es:")
        print(division(a,b))

    elif eleccion == 5:
        a=int(input("Ingresa un numero: "))
        b=int(input("Ingresa otro Numero: "))

    elif eleccion == 6:
        print("ADIOS")

    else:
        print("Opción invalida, ingresa otra opcion")