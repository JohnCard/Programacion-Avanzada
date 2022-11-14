class postman:
    def __init__(self,likes,comments = [],username,timestamp,dislikes):
        self.username = username
        self.timestamp = timestamp
        self.likes = likes
        self.dislikes = dislikes
        self.comments = comments
        
        def __str__(self):
            return f'''
            Nombre del usuario: {self.username}
            Tiempo activo: {self.timestamp}
            Cantidad de likes: {self.likes}
            Dislikes: {self.dislikes}
            Comentarios: {self.comments}
            '''
        def getNombre(self):
            return f'El usuario se llama: {self.username}'
        def getLikes(self):
            return f'Cantidad de likes: {self.likes}'
        def getDislikes(self):
            return f'Cantidad de dislikes: {self.dislikes}'
        def tiempoTranscurrido(self):
            return f'Tiempo transcurrido desde inicio de sesión: {self.timestamp}'
    
class commentedPostmen(postman):
    def __init__(self,likes,comments,message,photo,date_post,user_post):
        super().__init__(likes,comments)
        self.user_post = user_post
        self.likes = likes
        self.comments = comments
        self.message = message
        self.photo = photo
    def getMessage(self):
        return f'Mensaje a mostrar: {self.message}'

class messagePost(commentedPostmen):
    def __init__(self,message,message_date,user_message):
        super().__init__(message)
        self.message_date = message_date
        self.user_message = user_message
    def getMessage(self):
        return f'Mensaje a mostrar: {self.message}'
    def __str__(self):
        return f'''
        Mensaje digitado: {self.message}
        Fecha_mensaje: {self.message_date}
        Mensaje del usuario: {self.user_message}
        '''