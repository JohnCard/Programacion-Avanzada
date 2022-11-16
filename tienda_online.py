# Etapa uno de nuestro modulo
class article:
    def __init__(precio,nombre,codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
    
    def __str__(self):
        return f'''Nombre del producto: {self.nombre}
Codigo: {self.codigo}
Precio: ${self.precio}
'''
    def getPrecio(self):
        return f'Precio del producto {self.nombre}: ${self.precio}'
    def getNombre(self):
        return f'Nombre del producto: {self.nombre}'
    def getCode(self):
        return f'Codigo del producto {self.nombre}: {self.codigo}'

class electronics(article):
    def __init__(precio,nombre,codigo,descripcion,estancia):
        super().__init__(precio,nombre,codigo)
    def getDescripcion(self):
        return f'Descripción del proucto {self.nombre}: {self.descripcion}'