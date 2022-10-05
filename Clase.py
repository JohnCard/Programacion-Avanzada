class alumno:
    def __init__(self,nombre,folio,especialidad,semestre):
        self.nombre = nombre
        self.folio= folio
        self.especialidad = especialidad
        self.semestre = semestre
    def __str__(self):
        return f'''
Nombre del estudiante: {self.nombre}
Folio del estudiante: {self.folio}
Especialidad del estudiante: {self.especialidad}
Semestre actual cursado por el estudiante: {self.semestre}
        '''

class clase:
    def __init__(self,profesor,aula,horario,alumnos = []):
        self.profesor = profesor
        self.aula = aula
        self.horario = horario
        self.alumnos = alumnos
    def __str__(self):
        return(f'''
Nombre del profesor: {self.profesor}
Aula: {self.aula}
Horario: {self.horario}
Alumnos: {self.alumnos}''')
    def agreagar_alumno(self,alumno):
            self.alumnos.append(alumno)
    def mostrar_alumnos(self):
        for alumno in alumnos:
            print(alumno)

# datos para iniciar una clase:
profesor = input('Digite el nombre del profesor: ')
aula = input('Digite la dirección del aula: ')
horario = input('Digite el horario de la clase: ')

nueva_clase = clase(profesor,aula,horario)
print(nueva_clase)
# digitaremos 5 nuevos alumnos para provar el metodo del objeto clase
for i in range(5):
    a = input(f'Digite el nombre del alumno numero {i+1}: ')
    b = input(f'Digite su folio: ')
    c = input(f'Digite su especialidad: ')
    d = input(f'Digite su semestre actual: ')
    alumno_nuevezon = alumno(a,b,c,d)
    nueva_clase.agreagar_alumno(alumno_nuevezon)

# volvemos a imprimar toda nuestra nueva información nueva de nuestro objeto clase:
print('Lista de alumnos registrados: ')
for i in nueva_clase.alumnos:
    print(i)