from django.db import models
import datetime

ahora = datetime.datetime.now

# Create your models here.


class Nacionalidad(models.Model):
    pais = models.CharField(max_length=50, blank=True)
    nacionalidad = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Autor(models.Model):
    id_nacionalidad = models.ForeignKey(
        Nacionalidad, on_delete=models.CASCADE, blank=True)
    nombre = models.CharField(max_length=250, blank=True)
    pseudonimo = models.CharField(max_length=50, blank=True)
    biografia = models.TextField(blank=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Comuna(models.Model):
    codigo_comuna = models.CharField(max_length=5, blank=True)
    nombre_comuna = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, blank=True)
    calle = models.CharField(max_length=50, blank=True, default='')
    numero = models.CharField(max_length=10, blank=True, default='')
    departamento = models.CharField(max_length=10, blank=True)
    detalles = models.TextField(blank=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Biblioteca(models.Model):
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, blank=True)
    nombre_biblioteca = models.CharField(max_length=100, blank=True)
    web = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Lector(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, blank=True)
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, blank=True)
    rut_lector = models.IntegerField(blank=True, unique=True)
    digito_verificador = models.CharField(max_length=1, blank=True)
    nombre_lector = models.CharField(max_length=255, blank=True)
    correo_lector = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class TipoCategoria(models.Model):
    tipo_categoria = models.CharField(max_length=50, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Categoria(models.Model):
    id_tipo_categoria = models.ForeignKey(
        TipoCategoria, on_delete=models.CASCADE, blank=True)
    categoria = models.CharField(max_length=100, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Libro(models.Model):
    id_biblioteca = models.ForeignKey(
        Biblioteca, on_delete=models.CASCADE, blank=True)
    id_categoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=True)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, blank=True)
    titulo = models.CharField(max_length=255, blank=True)
    paginas = models.IntegerField(blank=True)
    copias = models.IntegerField(blank=True)
    ubicacion = models.CharField(max_length=255, blank=True)
    fisico = models.BooleanField(default=True)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)


class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE, blank=True)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE, blank=True)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateField(blank=True)
    fecha_retorno = models.DateTimeField(blank=True)