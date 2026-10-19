# para POO Todo algoritmo que se empiece se debe empezar así:
# Los atributos de clase se  crean en el pass ISB, titulo, autor y etado de disponibilidad disponible o prestado)

class Libro:
    def __init__(self, codigo, titulo, autor):
    self.ISBN = None
    self.titulo = titulo
    self.autor = autor 
    self.estado = "disponible"   #disponible|PRESTADO

class GestionBiblioteca:
    def __Str__(self):
        return f"""
        Código: {self.ISBN}
        Título: {self.titulo}
        Autor: {self.autor}
        Estado: {self.estado}
        """


if __name__ == "__main__":
    pass 
