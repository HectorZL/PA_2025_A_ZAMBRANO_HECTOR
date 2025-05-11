# Crear instancia de la clase Metodos
from buenas import Metodos

hola = Metodos()  # Instancia de la clase Metodos

def menu():
    while True:
        print("\n==== Menú de Listas ====")
        print("1. Ingresar Valor a la Lista")
        print("2. Eliminar Valor de la Lista")
        print("3. Calcular Promedio de Valores")
        print("4. Calcular Factorial de un Número")
        print("5. Calcular Serie de Fibonacci")
        print("6. Calcular Número Mayor")
        print("7. Ordenar Lista de Valores")
        print("8. Mostrar Lista de Valores")
        print("9. Salir")
        print("==========================")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                valor = float(input("Ingrese el valor a agregar: "))
                hola.ingresar_valor(valor)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        elif opcion == '2':
            try:
                valor = float(input("Ingrese el valor a eliminar: "))
                hola.eliminar_valor(valor)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        elif opcion == '3':
            promedio = hola.calcular_promedio()
            print(f"El promedio de los valores es: {promedio}")

        elif opcion == '4':
            try:
                numero = int(input("Ingrese un número para calcular su factorial: "))
                factorial = hola.calcular_factorial(numero)
                print(f"El factorial de {numero} es: {factorial}")
                print(f"Valores usados en el factorial: {hola.factorial_valores}")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

        elif opcion == '5':
            try:
                n = int(input("Ingrese la cantidad de números para la serie de Fibonacci: "))
                hola.calcular_fibonacci(n)
                print("Serie de Fibonacci:", hola.fibonacci_lista)
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número entero.")

        elif opcion == '6':
            mayor = hola.calcular_mayor()
            if mayor is not None:
                print(f"El número mayor es: {mayor}")
            else:
                print("No hay valores en la lista.")

        elif opcion == '7':
            hola.ordenar_lista()
            print(f"Lista ordenada: {hola.valores}")

        elif opcion == '8':
            hola.mostrar_lista()
            print(f"Lista de valores: {hola.valores}")
            break
        elif opcion == '9':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")


if __name__ == "__main__":
    menu()