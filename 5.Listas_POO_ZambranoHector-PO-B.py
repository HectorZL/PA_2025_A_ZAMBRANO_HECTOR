import math
# Zambrano Hector
# Practica 2 lista POO Python
# 12 de mayo 2025, entrega
# 2025 - A - ABRIL-AGOSTO

# INGENIERO HERNAN VARGAS

# Definición de la clase base 'Figura'
class ListaAnalizable:
    """
    Clase base para listas con funcionalidades extendidas.
    """
    def __init__(self, data):
        self.data = data

    def obtener_data(self):
        return self.data

    def encontrar_mayor(self):
        """Encuentra el mayor elemento en la lista."""
        if not self.data:
            return None
        mayor = self.data[0]
        for elemento in self.data:
            if elemento > mayor:
                mayor = elemento
        return mayor

    def eliminar_duplicados(self):
        """Elimina los elementos duplicados de la lista."""
        unica = []
        for elemento in self.data:
            if elemento not in unica:
                unica.append(elemento)
        return ListaAnalizable(unica)  # Retorna una nueva instancia para permitir el encadenamiento

    def ordenar_lista(self):
        """Ordena la lista en orden ascendente."""
        nueva_lista = self.data[:]  # Crea una copia para no modificar la original directamente
        nueva_lista.sort()
        return ListaAnalizable(nueva_lista)

    def calcular_promedio(self):
        """Calcula el promedio de los elementos en la lista."""
        if not self.data:
            return 0
        return sum(self.data) / len(self.data)

    def __len__(self):
        """Permite usar len() en la lista analizable"""
        return len(self.data)

    def __getitem__(self, indice):
      """Permite acceder a los elementos usando  []"""
      return self.data[indice]

class ListaNumerica(ListaAnalizable):
    """
    Clase derivada para listas numéricas con funcionalidades específicas.
    """
    def __init__(self, data):
        super().__init__(data)

    def calcular_suma(self):
        """Calcula la suma de los elementos."""
        return sum(self.data)

    def calcular_producto(self):
        """Calcula el producto de los elementos."""
        if not self.data:
            return 0
        producto = 1
        for elemento in self.data:
            producto *= elemento
        return producto

class ListaTexto(ListaAnalizable):
    """
    Clase derivada para listas de texto con funcionalidades específicas.
    """
    def __init__(self, data):
        super().__init__(data)

    def concatenar_elementos(self, separador=" "):
        """Concatena los elementos de la lista en una sola cadena."""
        return separador.join(self.data)

    def encontrar_palabra_mas_larga(self):
        """Encuentra la palabra más larga en la lista."""
        if not self.data:
            return None
        mas_larga = ""
        for elemento in self.data:
            if len(elemento) > len(mas_larga):
                mas_larga = elemento
        return mas_larga

# ### Programa Principal ###

def menu_listas():
    while True:
        print("\n--- Menú de Operaciones con Listas ---")
        print("1.  Analizar Lista Numérica")
        print("2.  Analizar Lista de Texto")
        print("3.  Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_y_analizar_numeros()
        elif opcion == "2":
            ingresar_y_analizar_texto()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def ingresar_y_analizar_numeros():
    numeros_str = input("Ingrese números separados por espacios: ").split()
    try:
        numeros = [float(num) for num in numeros_str]
        lista_numerica = ListaNumerica(numeros)

        print(f"Mayor: {lista_numerica.encontrar_mayor()}")
        print(f"Suma: {lista_numerica.calcular_suma()}")
        print(f"Producto: {lista_numerica.calcular_producto()}")
        print(f"Promedio: {lista_numerica.calcular_promedio()}")
        print(f"Lista Ordenada: {lista_numerica.ordenar_lista().obtener_data()}")
        print(f"Lista sin Duplicados: {lista_numerica.eliminar_duplicados().obtener_data()}")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese solo números.")

def ingresar_y_analizar_texto():
    textos = input("Ingrese palabras o frases separadas por comas: ").split(",")
    textos = [t.strip() for t in textos]  # Limpiar espacios alrededor de las palabras
    lista_texto = ListaTexto(textos)

    print(f"Concatenado: {lista_texto.concatenar_elementos(separador=' | ')}")
    print(f"Palabra más larga: {lista_texto.encontrar_palabra_mas_larga()}")
    print(f"Lista sin Duplicados: {lista_texto.eliminar_duplicados().obtener_data()}")


if __name__ == "__main__":
    menu_listas()