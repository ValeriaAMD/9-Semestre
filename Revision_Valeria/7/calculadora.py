from operaciones.suma import suma
from operaciones.resta import resta
from operaciones.division import division
from operaciones.multiplicacion import multiplicacion

while True:
    print("Elige la operacion a realizar: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elige una opción del 1 al 5: ")
    if opcion >= "6":
        print("No existe la opcion")
        continue
    
    if opcion == "5":
        break

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        resultado = suma(num1, num2)
        print("Resultado: ", resultado)
    elif opcion == "2":
        resultado = resta(num1, num2)
        print("Resultado: ", resultado)
    elif opcion == "3":
        resultado = multiplicacion(num2, num2)
        print("Resultado: ", resultado)
    elif opcion == "4":
        resultado = division(num1, num2)
        print("Resultado: ", resultado)