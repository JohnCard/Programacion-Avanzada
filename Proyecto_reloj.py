import string
from string import ascii_lowercase,ascii_uppercase

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz'

def recorrer(param):
    cont = 0
    for i in param:
        if i not in abc:
            cont += 1
    return cont

def setParam(param):
    while(recorrer(param) > 0):
        param = input(f'El parametro {param} es !INCORRECTO¡, favor de intentarlo de nuevo: ')
    return param

def setParam_dos(param):
    while(param.isdigit() == False):
        param = input(f'El parametro es invalido, intentelo de nuevo: ')
    return param

class reloj:
    def __init__(self,usuario,horas,minutos,segundos):
        self.usuario = usuario
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def __str__(self): 
            return f'''
Nombre de usuario: {self.usuario}
Horas: {self.horas}
Minutos: {self.minutos}
Segundos: {self.segundos}
            '''
    def getUser_name(self):
        return self.usuario
    
    def getHours(self):
        return self.horas

    def getMinutes(self):
        return self.minutos
    
    def getSegundos(self):
        return self.segundos
    
######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################
# --- Etapa 2 del proyecto (creción de la función para crear relojes): ---

def watch_create(usuario,horas,minutos,segundos):
    usuario = setParam(usuario)
    horas = setParam_dos(horas)
    minutos = setParam_dos(minutos)
    segundos = setParam_dos(segundos)
    
    var = reloj(usuario,horas,minutos,segundos)
    return var

nombre = input(f'Digite el nombre del usuario: ')
hours = input(f'Digite la hora del usuario: ')
minutes = input(f'Digite la cantidad de minutos: ')
seconds = input(f'Digite la cantidad de segundos: ')

watch_create(nombre,hours,minutes,seconds)
