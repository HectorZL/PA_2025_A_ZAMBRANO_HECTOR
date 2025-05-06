# Zambrano Hector
# Practica 1 Figura POO python
# Herencia, Polimorfismo, anidacion menu
# 6 de mayo 2025, entrega
# 2025 - A - ABRIL-AGOSTO

# INGENIERO HERNAN VARGAS

# Definición de la clase base 'Figura'
class Figura:
    # Constructor de la clase Figura
    def __init__(self, nombre):
        # Inicializa el nombre de la figura (ej: "Rectángulo", "Triángulo")
        self.nombre = nombre

    # Método para calcular el área (abstracto, debe ser implementado en clases derivadas)
    def area(self):
        pass

    # Método para calcular el perímetro (abstracto, debe ser implementado en clases derivadas)
    def perimetro(self):
        pass

    # Método para mostrar información general de la figura
    def mostrar_info(self):
        print(f"Nombre de la figura: {self.nombre}")

# Definición de la clase derivada 'Rectangulo', hereda de 'Figura'
class Rectangulo(Figura):
    # Constructor de la clase Rectangulo
    def __init__(self, base, altura):
        # Llama al constructor de la clase base (Figura) para inicializar el nombre
        super().__init__("Rectángulo")
        # Inicializa los atributos específicos del Rectángulo
        self.base = base
        self.altura = altura

    # Implementación del método area para Rectangulo
    def area(self):
        return self.base * self.altura

    # Implementación del método perimetro para Rectangulo
    def perimetro(self):
        return 2 * (self.base + self.altura)

    # Método para una representación gráfica simple del Rectángulo
    def draw(self):
        """Representación gráfica del rectángulo."""
        # Aseguramos que las dimensiones sean enteros positivos para dibujar
        base_int = max(1, int(self.base)) # Asegura al menos 1 para dibujar
        altura_int = max(1, int(self.altura)) # Asegura al menos 1 para dibujar

        if base_int == 1 and altura_int == 1:
             print('*')
        elif altura_int == 1:
             print('*' * base_int)
        else:
            print('*' * base_int) # Dibuja la fila superior
            # Dibuja las filas intermedias
            for _ in range(altura_int - 2):
                # Borde izquierdo '*', espacios interiores, borde derecho '*'
                print('*' + ' ' * max(0, base_int - 2) + ('*' if base_int > 1 else ''))
            # Dibuja la fila inferior (solo si altura > 1)
            if altura_int > 1:
                print('*' * base_int)


    # Sobreescritura del método mostrar_info para incluir detalles específicos del Rectángulo
    def mostrar_info(self):
        # Llama al método mostrar_info de la clase base
        super().mostrar_info()
        # Muestra los atributos específicos y los cálculos
        print(f"Base: {self.base}, Altura: {self.altura}")
        print(f"Área: {self.area()}, Perímetro: {self.perimetro()}")
        # Llama al método draw para mostrar la representación gráfica
        self.draw()

# Definición de la clase derivada 'Triangulo', hereda de 'Figura'
class Triangulo(Figura):
    # Constructor de la clase Triangulo
    def __init__(self, base, altura, lado1, lado2):
        # Llama al constructor de la clase base (Figura)
        super().__init__("Triángulo")
        # Inicializa los atributos específicos del Triángulo
        self.base = base
        self.altura = altura # Altura usada para el cálculo del área
        self.lado1 = lado1   # Lado adyacente a la base (no la altura)
        self.lado2 = lado2   # Otro lado adyacente a la base (no la altura)


    # Implementación del método area para Triangulo (fórmula base por altura / 2)
    def area(self):
        return (self.base * self.altura) / 2

    # Implementación del método perimetro para Triangulo (suma de los lados)
    def perimetro(self):
        # Asumimos que lado1 y lado2 son los otros dos lados además de la base
        return self.base + self.lado1 + self.lado2

    # Método para una representación gráfica simple del Triángulo (ejemplo básico, no escalado)
    def draw(self):
        """Representación gráfica básica de un triángulo."""
        # Una representación simple podría ser escalonada
        base_int = max(1, int(self.base))
        for i in range(1, base_int + 1):
            print('*' * i)


    # Sobreescritura del método mostrar_info para incluir detalles específicos del Triangulo
    def mostrar_info(self):
        # Llama al método mostrar_info de la clase base
        super().mostrar_info()
        # Muestra los atributos específicos y los cálculos
        print(f"Base: {self.base}, Altura (para área): {self.altura}")
        print(f"Lado 1: {self.lado1}, Lado 2: {self.lado2}") # Mostrar lados para perímetro
        print(f"Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}")
        # Llama al método draw
        self.draw()

# Definición de la clase derivada 'Hexagono', hereda de 'Figura'
class Hexagono(Figura):
    # Constructor de la clase Hexagono
    def __init__(self, lado):
        # Llama al constructor de la clase base (Figura)
        super().__init__("Hexágono")
        # Inicializa el atributo específico del Hexágono (longitud del lado)
        self.lado = lado

    # Implementación del método area para Hexagono regular
    # Fórmula: (3 * sqrt(3) / 2) * lado^2
    def area(self):
        """Área de un hexágono regular: (3*sqrt(3)/2) * lado^2"""
        # Se importa math para usar la función sqrt (raíz cuadrada)
        import math
        return (3 * math.sqrt(3) / 2) * (self.lado ** 2)

    # Implementación del método perimetro para Hexagono regular
    # Fórmula: 6 * lado
    def perimetro(self):
        """Perímetro de un hexágono regular: 6 * lado"""
        return 6 * self.lado

    # Método para una representación gráfica simple del Hexágono (puede ser compleja)
    def draw(self):
        """Representación gráfica básica de un hexágono (simplificada)."""
        # Nota: Dibujar un hexágono regular con caracteres es complejo y
        # esta es una representación artística o aproximada.
        lado_int = max(1, int(self.lado)) # Asegura al menos 1 para dibujar

        # Línea superior (parte superior del hexágono)
        print(' ' * (lado_int - 1) + '*' * (lado_int + (lado_int - 1))) # Ajuste para parecer hex
        # Parte superior-media
        for i in range(lado_int - 1):
             espacios_laterales = max(0, lado_int - 2 - i)
             espacios_centrales = max(0, lado_int + 2 * i - 1)
             if lado_int > 1:
                 print(' ' * espacios_laterales + '*' + ' ' * espacios_centrales + '*')
             else: # Caso lado_int == 1
                 print('*')

        # Parte media más ancha (los lados más largos visualmente)
        if lado_int > 0:
             print('*' * (lado_int * 3 - (lado_int > 1))) # Ajuste para parecer hex

        # Parte inferior-media (simetría con la superior-media)
        for i in range(lado_int - 2, -1, -1):
             espacios_laterales = max(0, lado_int - 2 - i)
             espacios_centrales = max(0, lado_int + 2 * i - 1)
             if lado_int > 1:
                 print(' ' * espacios_laterales + '*' + ' ' * espacios_centrales + '*')


        # Línea inferior (parte inferior del hexágono)
        if lado_int > 0:
            print(' ' * (lado_int - 1) + '*' * (lado_int + (lado_int - 1))) # Simetría con la superior


    # Sobreescritura del método mostrar_info para incluir detalles específicos del Hexagono
    def mostrar_info(self):
        # Llama al método mostrar_info de la clase base
        super().mostrar_info()
        # Muestra el atributo específico y los cálculos
        print(f"Lado: {self.lado}")
        # Se formatean los resultados a 2 decimales para mayor claridad
        print(f"Área: {self.area():.2f}, Perímetro: {self.perimetro():.2f}")
        # Llama al método draw
        self.draw()


# Definición de la clase 'MenuFiguras' para gestionar la interacción con el usuario y la colección de figuras
class MenuFiguras:
    # Constructor de la clase MenuFiguras
    def __init__(self):
        # Inicializa una lista vacía para almacenar objetos de figuras
        self.figuras = []

    # Método para agregar un Rectangulo a la colección
    def agregar_rectangulo(self, base, altura):
        # Crea una instancia de Rectangulo
        rectangulo = Rectangulo(base, altura)
        # Agrega la instancia a la lista de figuras
        self.figuras.append(rectangulo)
        print("Rectángulo agregado exitosamente.") # Mensaje de confirmación


    # Método para agregar un Triangulo a la colección
    def agregar_triangulo(self, base, altura, lado1, lado2):
        # Crea una instancia de Triangulo
        triangulo = Triangulo(base, altura, lado1, lado2)
        # Agrega la instancia a la lista de figuras
        self.figuras.append(triangulo)
        print("Triángulo agregado exitosamente.") # Mensaje de confirmación


    # Método para agregar un Hexagono a la colección
    def agregar_hexagono(self, lado):
        # Crea una instancia de Hexagono
        hexagono = Hexagono(lado)
        # Agrega la instancia a la lista de figuras
        self.figuras.append(hexagono)
        print("Hexágono agregado exitosamente.") # Mensaje de confirmación


    # Método para mostrar la información de todas las figuras en la colección
    def mostrar_figuras(self):
        # Verifica si hay figuras para mostrar
        if not self.figuras:
            print("No hay figuras para mostrar.")
            return # Sale del método si la lista está vacía

        print("\n--- Listado de Figuras ---")
        # Itera sobre cada figura en la lista
        for i, figura in enumerate(self.figuras):
            print(f"\nFigura #{i+1}") # Muestra el número de figura (empezando desde 1)
            # Llama al método mostrar_info de cada figura.
            # Aquí se aplica el polimorfismo: el mismo método se comporta
            # de forma diferente según el tipo de objeto (Rectangulo, Triangulo, Hexagono).
            figura.mostrar_info()
            print('-' * 30) # Separador entre figuras


    # Método principal para mostrar el menú de opciones e interactuar con el usuario
    def menu(self):
        # Bucle principal del menú que se ejecuta hasta que el usuario elija salir
        while True:
            print("\n===== Menú de Gestión de Figuras =====")
            print("1. Agregar Rectángulo")
            print("2. Agregar Triángulo")
            print("3. Agregar Hexágono")
            print("4. Mostrar Todas las Figuras")
            print("5. Salir")
            print("======================================")

            # Solicita la opción al usuario
            opcion = input("Seleccione una opción: ")

            # Estructura de control (if/elif/else) para manejar las opciones del menú (anidaciones)
            if opcion == "1":
                # Opción para agregar Rectángulo
                try:
                    base = float(input("Ingrese la base del rectángulo: "))
                    altura = float(input("Ingrese la altura del rectángulo: "))
                    # Valida que las dimensiones sean positivas
                    if base > 0 and altura > 0:
                         self.agregar_rectangulo(base, altura)
                    else:
                         print("La base y la altura deben ser números positivos.")
                except ValueError:
                    print("Entrada no válida. Por favor ingrese números.")

            elif opcion == "2":
                # Opción para agregar Triángulo
                try:
                    base = float(input("Ingrese la base del triángulo: "))
                    altura = float(input("Ingrese la altura del triángulo (para el área): "))
                    lado1 = float(input("Ingrese la longitud del lado 1 del triángulo: "))
                    lado2 = float(input("Ingrese la longitud del lado 2 del triángulo: "))
                     # Valida que las dimensiones sean positivas
                    if base > 0 and altura > 0 and lado1 > 0 and lado2 > 0:
                        # Nota: La validación estricta de si los lados forman un triángulo válido
                        # (suma de dos lados mayor al tercero) no está implementada aquí,
                        # pero es una consideración geométrica importante.
                        self.agregar_triangulo(base, altura, lado1, lado2)
                    else:
                         print("Todos los lados y la altura deben ser números positivos.")
                except ValueError:
                    print("Entrada no válida. Por favor ingrese números.")


            elif opcion == "3":
                # Opción para agregar Hexágono
                try:
                    lado = float(input("Ingrese la longitud del lado del hexágono: "))
                    # Valida que el lado sea positivo
                    if lado > 0:
                        self.agregar_hexagono(lado)
                    else:
                         print("La longitud del lado debe ser un número positivo.")
                except ValueError:
                    print("Entrada no válida. Por favor ingrese un número.")


            elif opcion == "4":
                # Opción para mostrar todas las figuras agregadas
                self.mostrar_figuras()

            elif opcion == "5":
                # Opción para salir del programa
                print("Saliendo del programa de gestión de figuras.")
                break # Sale del bucle while, terminando el programa

            else:
                # Mensaje para opciones no válidas
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


# Bloque principal que se ejecuta cuando el script es corrido directamente
if __name__ == "__main__":
    # Crea una instancia de la clase MenuFiguras
    gestor_menu = MenuFiguras()
    # Inicia el bucle del menú principal
    gestor_menu.menu()