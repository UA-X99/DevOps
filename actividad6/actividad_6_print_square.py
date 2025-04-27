def print_numbers():#uriel alejandro hernandez hernandez
        for number in range (n):
            if((n % 2) == 0):
                print("el numero es: " + number)


        else:
            print("El cuadrado del numero es: "+ number ** 2)

print("Ingrese un numero")
try:
    n = int(input())
    print("El numero ingresado: " + n)
  

except:
    print("Ingresa un numero")