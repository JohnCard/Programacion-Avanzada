class postman:
    def __init__(self,likes,comments,user_name,timestamp,dislikes):
        self.user_name = user_name
        self.timestamp = timestamp
        self.likes = likes
        self.dislikes = dislikes
        self.comments = list(comments)
        
    def __str__(self):
        return f'''Nombre del usuario: {self.user_name}
Tiempo activo: {self.timestamp}
Cantidad de likes: {self.likes}
Dislikes: {self.dislikes}
Comentarios: {self.comments}'''
    def getNombre(self):
        return f'El usuario se llama: {self.user_name}'
    def getLikes(self):
        return f'Cantidad de likes: {self.likes}'
    def getDislikes(self):
        return f'Cantidad de dislikes: {self.dislikes}'
    def tiempoTranscurrido(self):
        return f'Tiempo transcurrido desde inicio de sesión: {self.timestamp}'
    
class commentedPostmen(postman):
    def __init__(self,likes,comments,message,photo,date_post,user_post):
        super().__init__(likes,comments)
        self.date_post = date_post
        self.user_post = user_post
        self.likes = likes
        self.comments = comments
        self.message = message
        self.photo = photo
    def getMessage(self):
        return f'Mensaje a mostrar: {self.message}'
    def getLikes(self):
        return f'Cantidad de likes: {self.likes}'
    def getUser(self):
        return f'El usuario se llama: {self.user_post}'
    def __str__(self):
        return f'''Su mensaje: {self.message}
Cantidad de likes: {self.likes}
Nombre del usuario: {self.user_post}'''

class messagePost(commentedPostmen):
    def __init__(self,message,message_date,user_message):
        super().__init__(message)
        self.message_date = message_date
        self.user_message = user_message
    def getMessage(self):
        return f'Mensaje a mostrar: {self.message}'
    def __str__(self):
        return f'''Mensaje digitado: {self.message}
Fecha_mensaje: {self.message_date}
Mensaje del usuario: {self.user_message}'''

# creando un usario:

cantidad_usuarios = int(input('Digite la cantidad de usuarios a digitar: '))
for i in range(cantidad_usuarios):
    name = input(f'Digite el nombre del usuario número {i+1}: ')
    no_likes = int(input('Digite la cantidad de likes: '))
