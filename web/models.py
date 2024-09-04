from django.db import models

# Create your models here.
class Estudiante(models.Model):
    rut = models.CharField(primary_key=True, max_length=9, null=False, blank=False)
    nombre = models.CharField(max_length=50,null=False, blank=False)
    apellido = models.CharField(max_length=50,null=False, blank=False)
    fecha_nac = models.DateField(null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField('Curso', related_name='estudiantes')

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=10, unique=True, null=False, blank=False)
    nombre = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self) -> str:
        return f'{self.codigo} - {self.nombre}'


class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    calle = models.CharField(max_length=50, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False)
    dpto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, null=False, blank=False)
    ciudad = models.CharField(max_length=50, null=False, blank=False)
    region = models.CharField(max_length=50, null=False, blank=False)
    estudiante_id = models.OneToOneField('Estudiante', max_length=9, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.calle} {self.numero}'

class Profesor(models.Model):
    rut = models.CharField(primary_key=True, max_length=9, null=False, blank=False)
    nombre = models.CharField(max_length=50,null=False, blank=False)
    apellido = models.CharField(max_length=50,null=False, blank=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    cursos = models.ManyToManyField('Curso', related_name='profesores')

    def __str__(self) -> str:
        return f'{self.nombre} {self.apellido}'