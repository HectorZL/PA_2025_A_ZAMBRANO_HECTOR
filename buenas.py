class Metodos:
    def __init__(self):
        self.valores = []
        self.factorial_valores = []
        self.fibonacci_lista = []

    def ingresar_valor(self, valor):
        self.valores.append(valor)
        print(f"Valor {valor} ingresado a la lista.")

    def eliminar_valor(self, valor):
        try:
            self.valores.remove(valor)
            print(f"Valor {valor} eliminado de la lista.")
        except ValueError:
            print(f"Valor {valor} no encontrado en la lista.")

    def calcular_promedio(self):
        if not self.valores:
            return 0
        return sum(self.valores) / len(self.valores)

    def calcular_factorial(self, numero):
        if numero < 0:
            return "El factorial no está definido para números negativos."
        elif numero == 0:
            return 1
        else:
            factorial = 1
            self.factorial_valores = []  # Reiniciar la lista
            for i in range(1, numero + 1):
                factorial *= i
                self.factorial_valores.append(i)
            return factorial

    def calcular_fibonacci(self, n):
        self.fibonacci_lista = []  # Reiniciar la lista
        a, b = 0, 1
        for _ in range(n):
            self.fibonacci_lista.append(a)
            a, b = b, a + b

    def calcular_mayor(self):
        if not self.valores:
            return None
        return max(self.valores)

    def ordenar_lista(self):
        self.valores.sort()
        print("Lista de valores ordenada.")

    def mostrar_lista(self):
        if not self.valores:
            print("La lista está vacía.")
        else:
            print("Lista de valores:", self.valores)
        