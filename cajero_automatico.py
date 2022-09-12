class cajero_autmatico():
    def __init__(self,nombre_usuario,usuario_correo,contraseña,saldo):
        self.nombre_usuario = nombre_usuario
        self.usuario_correo = usuario_correo
        self.contraseña = contraseña
        self.saldo = saldo

    def __str__(self):
        return f'''
        Nombre del usuario: {self.nombre_usuario}
        Correo de {self.nombre_usuario}: {self.usuario_correo}
        Saldo actual de {self.nombre_usuario}: {self.saldo}
        '''
        
    def getSaldo(self):
        return(f'La cantidad de saldo del usuario {self.nombre_usuario} es de aproximadamente {self.saldo}')

    def setSaldo(self,cantidad):
        while(float(cantidad) < 0 or float(cantidad) > self.saldo):
            if(float(cantidad) > self.saldo):
                cantidad = input(f'La cantidad digitada de {cantidad} supera a la actual de {self.saldo}, favor de volver a intentarlo: ')
            else:
                cantidad = input(f'La cantidad digitada de {cantidad} no es reconocible, favor de volver a intentarlo: ')

        self.saldo = float(cantidad)
        cantidad = float(cantidad)
        print(type(cantidad))

pablito = cajero_autmatico('John Card','JohnCard978@outlook.com','contraseñaV2.0',17500)
print(pablito.getSaldo())
pablito.setSaldo(18000)