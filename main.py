class postman:
    def __init__(self,likes,comments):
        # self.user_name = user_name
        # self.timestamp = timestamp
        self.likes = likes
        # self.dislikes = dislikes
        self.comments = list(comments)
        
    def __str__(self):
        return f'''
Cantidad de likes: {self.likes}
Comentarios: {self.comments}'''
    # def getNombre(self):
    #     return f'El usuario se llama: {self.user_name}'
    def getLikes(self):
        return f'Cantidad de likes: {self.likes}'
    def getComments(self):
        return f'Comentarios: {self.comments}'
    # def tiempoTranscurrido(self):
    #     return f'Tiempo transcurrido desde inicio de sesión: {self.timestamp}'
    
class commentedPostmen(postman):
    def __init__(self,message,likes,comments):
        super().__init__(likes,comments)
        # self.date_post = date_post
        # self.user_post = user_post
        self.message = message
        # self.photo = photo
    def getMessage(self):
        return f'Mensaje a mostrar: {self.message}'
    def getLikes(self):
        return f'Cantidad de likes: {self.likes}'
    def __str__(self):
        return f'''Su mensaje: {self.message}
Cantidad de likes: {self.likes}'''

class messagePost(commentedPostmen):
    def __init__(self,message,likes,comments,message_date,user_message):
        super().__init__(message,likes,comments)
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
usuarios_nuevos = []
postmen_list = []
message_postlist = []
for i in range(cantidad_usuarios):
    name = input(f'Digite el nombre del usuario número {i+1}: ')
    no_likes = int(input('Digite la cantidad de likes: '))
    numero_comentarios = int(input('Digite la cantidad de comentarios que desea dejar en la caja: '))
    box_comments = []
    for i in range(numero_comentarios):
        comment = input(f'Digite el comentario número {i+1}: ')
        box_comments.append(comment)
    message = input('Digite una descripsión para su perfil: ')
    fecha_registro = input('Digite la fecha actual para su registro: ')
    
    new_user = postman(no_likes,box_comments)
    new_comented = commentedPostmen(message,no_likes,box_comments)
    message_post = messagePost(message,no_likes,box_comments,fecha_registro,name)
    postmen_list.append(new_comented)
    message_postlist.append(message_post)
    usuarios_nuevos.append(new_user)

# recorriendo cada usuario nuevo:
print('\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
for i in usuarios_nuevos:
    print(i)
print('\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
for i in postmen_list:
    print(i)
print('\n------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
for i in message_postlist:
    print(i)
