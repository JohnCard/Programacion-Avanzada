# --- Etapa 1 del proyecto (creción de la clase reloj): ---

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
            
    def getNombre(self):
        return f'El Nombre del usuario es: {self.usuario}'
        
    def getHoras(self):
        return f'La hora es: {self.horas}'
        
    def getMinutos(self):
        return f'Minutos: {self.minutos}'
        
    def getSegundos(self):
        return f'Segundos: {self.segundos}'
        
    def setHoras(self,hora_nueva):
        self.horas = hora_nueva
    
    def setMinutos(self,minuto_nuevo):
        self.minutos = minuto_nuevo
    
    def setSegundos(self,segundo_nuevo):
        self.segundos = segundo_nuevo
        
######################################################################################################################################################################
######################################################################################################################################################################
######################################################################################################################################################################
# --- Etapa 2 del proyecto (creción de la función para crear usuarios): ---

def crear_usuario(usuario,horas,minutos,segundos):
    usuario_nuevo = reloj(usuario,horas,minutos,segundos)
    
    while(type(usuario_nuevo.getNombre()) != type('string'))