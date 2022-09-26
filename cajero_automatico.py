abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'
abc_2 =  'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234657890@|°¬!.*:#$%&/¡+[]^-_'
def recorrer(param):
    cont = 0
    for i in param:
        if i not in abc:
            cont += 1
    return cont

def recorrer2(param):
    cont = 0
    for i in param:
        if i not in abc_2:
            cont += 1
    return cont

def setParam(param):
    while(recorrer(param) > 0):
        param = input(f'El parametro {param} para el nombre es !INCORRECTO¡, favor de intentarlo de nuevo: ')
    return param

def setParam2(param):
    while(recorrer2(param) > 0):
        param = input(f'El parametro {param} para la (contraseña/correo) es !INCORRECTO¡, favor de intentarlo de nuevo: ')
    return param

def setParam3(param):
    while(param.isdigit() == False):
        param = input(f'El parametro {param} para el saldo es !INCORRECTO¡, favor de intentarlo de nuevo: ')
    return int(param)

def create_user(nombre_usuario,usuario_correo,contraseña,saldo):
    nombre_usuario = setParam(nombre_usuario)
    usuario_correo = setParam2(usuario_correo)
    contraseña = setParam2(contraseña)
    saldo = setParam2(saldo)
    
    var = cajero_autmatico(nombre_usuario,usuario_correo,contraseña,saldo)
    return var

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

    def retirar_Saldo(self,cantidad):
        while(float(cantidad) < 0 or float(cantidad) > self.saldo):
            if(float(cantidad) > self.saldo):
                cantidad = input(f'La cantidad digitada de {cantidad} supera a la actual de {self.saldo}, favor de volver a intentarlo: ')
            else:
                cantidad = input(f'La cantidad digitada de {cantidad} no es reconocible, favor de volver a intentarlo: ')

        self.saldo -= int(cantidad)
        print(f'Con la cantidad retirada de {cantidad}, el saldo actual en su cuenta seria de {self.saldo}')
    
    def sumar_Saldo(self,cantidad):
        while(float(cantidad) < 0):
            cantidad = input(f'La cantidad digitada de {cantidad} no es reconocible, favor de volver a intentarlo: ')
        self.saldo += int(cantidad)
        print(f'Ahora la cantidad actual de saldo en su caja es de {self.saldo}')

nombre = input(f'Digite el nombre del usuario: ')
correo = input(f'Digite su correo electronico: ')
contraseña = input(f'Digite su contraseña: ')
saldo = input(f'Digite su primer saldo: ')

create_user(nombre,correo,contraseña,saldo)

'''
Links importantes: 
clouds: https://www.meteorologiaenred.com/tipos-de-nubes.html#Altocumulos
watches: 
'''
