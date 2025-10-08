from django.db import models
import datetime

ahora = datetime.datetime.now

# Create your models here.


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, null=True)
    nacionalidad = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Autor(models.Model):
    id_nacionalidad = models.ForeignKey(
        Nacionalidad, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=250, null=True)
    pseudonimo = models.CharField(max_length=50, null=True)
    biografia = models.TextField(null=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Comuna(models.Model):
    codigo_comuna = models.CharField(max_length=5, null=True)
    nombre_comuna = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True)
    calle = models.CharField(max_length=50, null=True, default='')
    numero = models.CharField(max_length=10, null=True, default='')
    departamento = models.CharField(max_length=10, null=True)
    detalles = models.TextField(null=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Biblioteca(models.Model):
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, null=True)
    nombre_biblioteca = models.CharField(max_length=100, null=True)
    web = models.CharField(max_length=255, null=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Lector(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, null=True)
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, null=True)
    rut_lector = models.IntegerField(null=True, unique=True)
    digito_verificador = models.CharField(max_length=1, null=True)
    nombre_lector = models.CharField(max_length=255, null=True)
    correo_lector = models.CharField(max_length=255, null=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class TipoCategoria(models.Model):
    tipo_categoria = models.CharField(max_length=50, null=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Categoria(models.Model):
    id_tipo_categoria = models.ForeignKey(
        TipoCategoria, on_delete=models.CASCADE, null=True)
    categoria = models.CharField(max_length=100, null=True)
    descripcion = models.CharField(max_length=255, null=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Libro(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, null=True)
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=255, null=True)
    paginas = models.IntegerField(null=True)
    copias = models.IntegerField(null=True)
    ubicacion = models.CharField(max_length=255, null=True)
    fisico = models.BooleanField(default=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE, null=True)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True)
    fecha_retorno = models.DateTimeField(null=True)