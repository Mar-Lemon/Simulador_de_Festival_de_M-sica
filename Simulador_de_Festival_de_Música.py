# ==========================================
# 1. Clase Base: Artista
# ==========================================
class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad  # Entero del 1 al 100

    def presentarse(self):
        print(f"Hola a todos. Soy {self.nombre}, artista del género {self.genero} (Popularidad: {self.popularidad}/100).")

    def actuar(self):
        # Método que será sobrescrito por las subclases
        pass

    def despedirse(self):
        print(f"Muchas gracias por acompañarnos, fue un placer tocar para ustedes. Atentamente, {self.nombre}.\n")


# ==========================================
# 2. Subclases de Artista
# ==========================================

class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su éxito {self.cancion_mas_popular} con gran energía.")


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes  # Número de integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")


# ==========================================
# 3. Función para iniciar el festival
# ==========================================
def iniciar_festival(lista_artistas):
    """
    Recibe una lista de artistas y aplica polimorfismo llamando a sus métodos
    sin utilizar condicionales (if/else) para distinguir el tipo de artista.
    """
    print("========================================")
    print("      DA COMIENZO EL FESTIVAL           ")
    print("========================================\n")
    
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación")
        print("-" * 40)


# ==========================================
# 4. Programa principal (main.py)
# ==========================================
def main():
    print("--- Registro de Artistas para el Festival ---")
    
    # Validar que se ingrese un número entero positivo
    while True:
        try:
            total_artistas = int(input("¿Cuántos artistas se presentarán?: "))
            if total_artistas > 0:
                break
            print("Por favor, ingresa un número mayor a 0.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

    lista_artistas = []

    for i in range(total_artistas):
        print(f"\n--- Datos del Artista {i + 1} ---")
        
        # Solicitar tipo de artista con validación básica
        while True:
            tipo = input("Tipo de artista (Cantante, DJ o Banda): ").strip().capitalize()
            if tipo in ["Cantante", "Dj", "Banda"]:
                if tipo == "Dj": 
                    tipo = "DJ" # Normalizar formato
                break
            print("Tipo no válido. Debe ser 'Cantante', 'DJ' o 'Banda'.")

        nombre = input("Nombre: ").strip()
        genero = input("Género musical: ").strip()
        
        # Validar popularidad (1 al 100)
        while True:
            try:
                popularidad = int(input("Popularidad (entero del 1 al 100): "))
                if 1 <= popularidad <= 100:
                    break
                print("El valor debe estar entre 1 y 100.")
            except ValueError:
                print("Entrada inválida. Ingresa un número entero.")

        # Solicitar atributo específico según el tipo de artista
        if tipo == "Cantante":
            cancion = input("Canción más popular: ").strip()
            objeto_artista = Cantante(nombre, genero, popularidad, cancion)
        elif tipo == "DJ":
            estilo = input("Estilo de mezcla: ").strip()
            objeto_artista = DJ(nombre, genero, popularidad, estilo)
        elif tipo == "Banda":
            while True:
                try:
                    integrantes = int(input("Número de integrantes: "))
                    if integrantes > 0:
                        break
                    print("Debe haber al menos 1 integrante.")
                except ValueError:
                    print("Entrada inválida. Ingresa un número entero.")
            objeto_artista = Banda(nombre, genero, popularidad, integrantes)

        # Agregar el objeto creado a la lista
        lista_artistas.append(objeto_artista)
        print(f"{nombre} registrado exitosamente.")

    print("\n\n")
    # Llamar a la función del festival
    iniciar_festival(lista_artistas)


if __name__ == "__main__":
    main() 