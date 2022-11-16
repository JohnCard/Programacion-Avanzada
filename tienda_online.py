# Etapa uno de nuestro modulo
class article:
    def __init__(precio,nombre,codigo):
        self.nombre = nombre
        self.precio = precio
        self.codigo = codigo
    
    def __str__(self):
        return f'''Nombre del producto: {self.nombre}
Codigo: {self.codigo}
Precio: ${self.precio}'''
    def getPrecio(self):
        return f'Precio del producto {self.nombre}: ${self.precio}'
    def getNombre(self):
        return f'Nombre del producto: {self.nombre}'
    def getCode(self):
        return f'Codigo del producto {self.nombre}: {self.codigo}'

class comida(article):
    def __init__(precio,nombre,codigo,tipo,grupo):
        super().__init__(precio,nombre,codigo)
        self.tipo = tipo
        self.grupo = grupo
    def __str__(self):
        return f'''El producto {self.nombre} es del tipo {self.tipo}
Codigo del producto {self.nombre}: {self.codigo}, que pertenece al grupo de {self.grupo}'''

class bebida(article,comida):
    def __init__(precio,nombre,codigo,tipo,grupo,sabor):
        article.__init__(self,precio,nombre,codigo)
        comida.__init__(self,tipo,grupo)
        self.sabor = sabor
    def __str__(self):
        return f'''Nombre del producto: {self.nombre}
La bebida {self.nombre} cuesta ${self.precio} y se rige por el codigo {self.codigo}
La bebida {self.nombre} pertenece al grupo {self.grupo} y tiene sabor a {self.sabor}'''
    def getTipado(self):
        return f'El producto {self.nombre} pertnece al grupo de {self.tipo}'

class electronics(article):
    def __init__(precio,nombre,codigo,no_bites,tipo_cargador):
        super().__init__(precio,nombre,codigo)
        self.no_bites = no_bites
        self.tipo_cargador = tipo_cargador
    def getDescripcion(self):
        return f'El producto {self.nombre} utiliza un cargador de tipo {self.tipo_cargador}'
    def getEstancia(self):
        return f'El producto {self.nombre} tiene {self.no_bites}'
    def __str__(self):
        return f'''El producto se llama {self.nombre}
El producto {self.nombre} tiene un precio de {self.precio} y el codigo de {self.codigo}
El producto tiene una cantidad de {self.no_bites} bites y se recarga con cargadores del tipo {self.tipo_cargador}'''

class computer(article,electronics):
    def __init__(self,precio,nombre,codigo,no_bites,tipo_cargador,tipo,marca)
        article.__init__(self,precio,nombre,codigo)
        electronics.__init__(self,no_bites,tipo_cargador)
        self.tipo = tipo
        self.marca = marca
    def __str__(self):
        return f'''Nombre del la pc: {self.nombre}
La computadora {self.nombre} tiene un precio de {self.precio} y sigue el codigo: {self.codigo}
La computadora {self.nombre} pertenece a la marca {self.marca} y es del tipo {self.tipo}'''

answer = 's'
while(answer == 's'):
    tipo_producto = input('''Digite el tipo de producto que quiere comprar 
a) para un comestible y b) para un  electrodomestico: ''')
    if(tipo_producto == 'a'):
        product_name = input('Ahora digite a) para un electrodomestico cualquiera o b) para una pc: ')
        if(product_name == 'a'):
            name = input('Digite el nombre del producto a comprar: ')