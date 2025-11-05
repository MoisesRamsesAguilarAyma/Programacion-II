from datetime import date
class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

    def mostrar_pagina(self):
        print(f"Página {self.numero}: {self.contenido}")
class Libro:
    def __init__(self, titulo, isbn, paginas_contenido):
        self.titulo = titulo
        self.isbn = isbn
        self.paginas = [Pagina(i+1, contenido) for i, contenido in enumerate(paginas_contenido)]
    def leer(self):
        print(f"\n Leyendo el libro: {self.titulo}")
        for pagina in self.paginas:
            pagina.mostrar_pagina()
class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
    def mostrar_info(self):
        print(f"Autor: {self.nombre} ({self.nacionalidad})")
class Estudiante:
    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre
    def mostrar_info(self):
        print(f"Estudiante {self.nombre} - Código: {self.codigo}")
class Prestamo:
    def __init__(self, estudiante, libro):
        self.estudiante = estudiante
        self.libro = libro
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
    def mostrar_info(self):
        print(f"\n Préstamo:")
        print(f"  Libro: {self.libro.titulo}")
        print(f"  Estudiante: {self.estudiante.nombre}")
        print(f"  Fecha de préstamo: {self.fecha_prestamo}")
        print(f"  Fecha de devolución: {self.fecha_devolucion if self.fecha_devolucion else 'Aún no devuelto'}")
class Horario:
    def __init__(self, dias_apertura, hora_apertura, hora_cierre):
        self.dias_apertura = dias_apertura
        self.hora_apertura = hora_apertura
        self.hora_cierre = hora_cierre

    def mostrar_horario(self):
        print(f" Horario: {self.dias_apertura}, de {self.hora_apertura} a {self.hora_cierre}")
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.autores = []
        self.prestamos = []
        self.horario = Horario("Lunes a Viernes", "08:00", "18:00")
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f" Libro agregado: {libro.titulo}")
    def agregar_autor(self, autor):
        self.autores.append(autor)
        print(f" Autor registrado: {autor.nombre}")
    def prestar_libro(self, estudiante, libro):
        prestamo = Prestamo(estudiante, libro)
        self.prestamos.append(prestamo)
        print(f" Se ha prestado '{libro.titulo}' a {estudiante.nombre}")
    def mostrar_estado(self):
        print(f"\n===== Estado de la Biblioteca '{self.nombre}' =====")
        self.horario.mostrar_horario()
        print("\n Libros disponibles:")
        for libro in self.libros:
            print(f" - {libro.titulo}")
        print("\n Autores registrados:")
        for autor in self.autores:
            autor.mostrar_info()
        print("\n Préstamos activos:")
        for prestamo in self.prestamos:
            prestamo.mostrar_info()
    def cerrar_biblioteca(self):
        print(f"\n La biblioteca '{self.nombre}' está cerrando. Todos los préstamos serán eliminados.")
        self.prestamos.clear()
if __name__ == "__main__":
    biblioteca = Biblioteca("Biblioteca Central UMSA")
    autor1 = Autor("Gabriel García Márquez", "Colombiano")
    autor2 = Autor("Julio Cortázar", "Argentino")
    biblioteca.agregar_autor(autor1)
    biblioteca.agregar_autor(autor2)
    libro1 = Libro("Cien Años de Soledad", "123-ABC", ["Inicio del libro...", "Desarrollo...", "Final."])
    libro2 = Libro("Rayuela", "456-XYZ", ["Capítulo 1...", "Capítulo 2...", "Capítulo 3..."])
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    estudiante1 = Estudiante("2025001", "Moises Aguilar")
    biblioteca.prestar_libro(estudiante1, libro1)
    biblioteca.mostrar_estado()
    libro1.leer()
    biblioteca.cerrar_biblioteca()
