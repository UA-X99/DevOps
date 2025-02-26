class Entero:
    def __init__(self, n): 
        self.n = n 

    def print_numbers(self): 
        for number in range(self.n):
            if (number % 2) == 0:
                print("El número es:", number)
            else:
                print("El cuadrado del número es:", number ** 2)


print("Ingrese un número:")
num = int(input())  


entero = Entero(num)
entero.print_numbers()