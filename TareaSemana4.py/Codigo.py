class Tarea:
    def __init__(self, tarea_id, titulo, calificacion, categoria):
        self.tarea_id = tarea_id
        self.titulo = titulo
        self.calificacion = calificacion
        self.categoria = categoria

    def __str__(self):
        return f"ID: {self.tarea_id}, Título: {self.titulo}, Calificación: {self.calificacion}, Categoría: {self.categoria}"

def clasificar_categoria(numero_categoria):
    categorias = {
        1: "quiz",
        2: "parcial",
        3: "trabajo"
    }
    return categorias.get(numero_categoria, "Categoría no válida")

def registrar_tareas():
    tareas = []
    while True:
        tarea_id = input("Ingrese el ID de la tarea: ")
        titulo = input("Ingrese el título de la tarea: ")
        
        while True:
            try:
                calificacion = float(input("Ingrese la calificación (0-5): "))
                if 0 <= calificacion <= 5:
                    break
                else:
                    print("La calificación debe estar entre 0 y 5.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        while True:
            try:
                numero_categoria = int(input("Ingrese la categoría (1: quiz, 2: parcial, 3: trabajo): "))
                categoria = clasificar_categoria(numero_categoria)
                if categoria != "Categoría no válida":
                    break
                else:
                    print(categoria)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        
        tarea = Tarea(tarea_id, titulo, calificacion, categoria)
        tareas.append(tarea)

        continuar = input("¿Desea ingresar otra tarea? (s/n): ").lower()
        if continuar != 's':
            break

    return tareas

def imprimir_tareas(tareas):
    print("\nLista de Tareas Registradas:")
    for tarea in tareas:
        print(tarea)

if __name__ == "__main__":
    tareas = registrar_tareas()
    imprimir_tareas(tareas)