def setParam(param,name):
    while(param.isalpha() == False):
        param = input(f'El parametro {param} para {name} es !INCORRECTO¡, favor de intentarlo de nuevo: ')
    return param

class nube:
    def __init__(self,grupo,nombre,descripcion,caracteristicas):
        self.grupo = grupo
        self.nombre = nombre
        self.descripcion = descripcion
        self.caracteristicas = caracteristicas
    
    def __str__(self):
        return f'''
    \n
    Nombre de la nube: {self.nombre}
    Clasificación de la nube {self.nombre}: {self.grupo}
    Descripción de la nube {self.nombre}: {self.descripcion}
    Caracteristicas de la nube {self.nombre}: {self.caracteristicas}
    \n
    '''    
    
    # Favor de utilizar la correspo
    
    def getNombre(self):
        return f'Nombre de la nube: {self.nombre}'
    def getCaracteristicas(self):
        return f'Caracteristicas de la nube {self.nombre}: {self.caracteristicas}'
    def getGrupo(self):
        return f'Clasificación de la nube {self.nombre}: {self.grupo}'
    def getDescripcion(self):
        return f'Descripción de la nube {self.nombre}: {self.descripcion}'
        
def creating_clouds(name,group,skills,description):
    name = setParam(name,'nombre')
    group = setParam(group,'clasificación')
    skills = setParam(skills,'caracteristicas')
    description = setParam(description,'descripción')
    var = nube(group,name,description,skills)
    
    return var

nombre = input('Digitar el nombre: ')
group = input('Digitar su clasificación: ')
skills = input('Digitar sus caracteristicas: ')
description = input('Digitar su descripción: ')

nube_nueva = creating_clouds(nombre,group,skills,description)
print(nube_nueva)