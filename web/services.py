from .models import Curso, Profesor, Direccion, Estudiante

#Se debe ingresar codigo y nombre
def crear_curso(nuevoCodigo, nuevoNombre):
    #Se crea el objeto y despues se guarda, imprimo mensaje en consola para confirmar
    nuevo_curso = Curso(codigo = nuevoCodigo, nombre = nuevoNombre)
    nuevo_curso.save()
    print('Curso creado correctamente')

#Se debe ingresar rut, nombre, apellido, estado, y quien 
# lo creo
def crear_profesor(nuevoRut, nuevoNombre, nuevoApellido, estadoActivo, creadoPor):
    #Se crea el objeto y despues se guarda, imprimo mensaje en consola para confirmar
    nuevo_profesor = Profesor(rut = nuevoRut, nombre = nuevoNombre, apellido = nuevoApellido, activo = estadoActivo, creado_por = creadoPor)
    nuevo_profesor.save()
    print('Profesor creado correctamente')

#Se debe ingresar rut, nombre, apellido, fecha nacimiento, estado, y quien lo creo
def crear_estudiante(nuevoRut, nuevoNombre, nuevoApellido, nuevaFechaNac, estadoActivo, creadoPor):
    #Se crea el objeto y despues se guarda, imprimo mensaje en consola para confirmar
    nuevo_estudiante = Estudiante(rut = nuevoRut, nombre = nuevoNombre, apellido = nuevoApellido, fecha_nac = nuevaFechaNac, activo = estadoActivo, creado_por = creadoPor)
    nuevo_estudiante.save()
    print('Estudiante creado correctamente')

#Se debe ingresar calle, numero, departamento, comuna, ciudad, region y el objeto estudiante
def crear_direccion(nuevaCalle, nuevoNumero, nuevoDpto, nuevaComuna, nuevaCiudad, nuevaRegion, idEstudiante):
    #Se crea el objeto y despues se guarda, imprimo mensaje en consola para confirmar
    nueva_direccion = Direccion(calle = nuevaCalle, numero = nuevoNumero, dpto = nuevoDpto, comuna = nuevaComuna, ciudad = nuevaCiudad, region = nuevaRegion, estudiante_id = idEstudiante)
    nueva_direccion.save()
    print('Direccion creada correctamente')


#Se debe ingresar el rut del estudiante
def obtiene_estudiante(rut_estudiante):
    #Obtengo el estudiante mediante el rut
    estudiante = Estudiante.objects.get(rut = rut_estudiante)
    return estudiante

#Se debe ingresar el rut del profesor
def obtiene_profesor(rut_profesor):
    #Obtengo el profesor mediante el rut
    profesor = Profesor.objects.get(rut = rut_profesor)
    return profesor

#Se debe ingresar el codigo del curso
def obtiene_curso(codigo_a_obtener):
    #Obtengo el curso mediante el codigo
    curso = Curso.objects.get(codigo = codigo_a_obtener)
    return curso

#Se debe ingresar el rut del profesor y el codigo del curso
def agrega_profesor_a_curso(rut_profesor, codigo_curso):
    #Obtengo profesor por rut y curso por el codigo y los asigno a variables
    profesor = Profesor.objects.get(rut = rut_profesor)
    curso = Curso.objects.get(codigo = codigo_curso)

    #Valido que exista el profesor, de lo contrario retorna mensaje
    if not profesor:
        return print('Profesor Inexistente')
    
    #Valido que exista el curso, de lo contrario retorna mensaje
    if not curso:
        return print('Curso Inexistente')
    
    #Añado el profesor al curso
    profesor.cursos.add(curso)
    print('Profesor añadido a curso correctamente')

#Se debe ingresar el rut del estudiante y el codigo del curso
def agrega_cursos_a_estudiante(rut_estudiante, codigo_curso):
    #Obtengo estudiante por rut y curso por el codigo y los asigno a variables
    estudiante = Estudiante.objects.get(rut = rut_estudiante)
    curso = Curso.objects.get(codigo = codigo_curso)

    #Valido que exista el estudiante, de lo contrario retorna mensaje
    if not estudiante:
        return print('Estudiante Inexistente')
    
    #Valido que exista el curso, de lo contrario retorna mensaje
    if not curso:
        return print('Curso Inexistente')
    
    #Añado el estudiante al curso
    estudiante.cursos.add(curso)
    print('Estudiante añadido a curso correctamente')

#Se debe ingresar el rut del estudiante
def imprime_estudiante_cursos(id_estudiante):
    #Obtengo el estudiante junto con sus cursos asociados con prefetch (buena practica para reducir las consultas a la DB), y distingo por el rut del estudiante
    estudiante = Estudiante.objects.prefetch_related('cursos').get(rut=id_estudiante)
    #Obtengo los cursos del estudiante y los guardo en una variable aparte para recorrerla
    cursos_del_estudiante = estudiante.cursos.all()

    #Imprimo el nombre del estudiante
    print(f"""Estudiante: {estudiante.nombre} {estudiante.apellido}
Cursos: """)
    #Recorro todos los cursos asociados al estudiante y los imprimo uno por uno
    for curso in cursos_del_estudiante:
        print(f"- {curso.nombre}")
    