def divicion():
    try:
        num1 = float(input("Introduce el primer numero: "))
        num2 = float(input("introduce el segundo numero: "))
        print("la divicion es: " + str(num1/ num2))

    except ValueError:

        print("El valor introduccido es erroneo!")

    except ZeroDivisionError:

        print("No se puede dividir entre 0!! ")

        

print("Hemos finalizado!! ")

# esto es una divicion probando los except para evitar errores del codigo
