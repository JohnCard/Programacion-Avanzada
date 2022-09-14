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
    
    def setName(self,new_userName):
        self.usuario = new_userName
    
    def setHours(self,new_Hours):
        self.horas = new_Hours

    def setMinutes(self,new_minute):
        self.minutos = new_minute
    
    def setSegundos(self,new_second):
        self.segundos = new_second
    
######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################
# --- Etapa 2 del proyecto (creción de la función para crear relojes): ---

def watch_create(usuario,horas,minutos,segundos):
    new_user = reloj(usuario,horas,minutos,segundos)

    while(type(float(new_user.getUser_name())) != type('string')):
        new_nombre = input(f'El parametro digitado por usted ({new_user.getUser_name()}) es absolutamente invalido, vuelva a intentarlo porfas: ')
        new_user.setName(new_nombre)

nombre_uno = watch_create(4,24,23,30)
