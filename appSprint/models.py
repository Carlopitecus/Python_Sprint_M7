from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    apellido = models.CharField(max_length=200)


class Tarea(models.Model):
    cat = [
        ("Trabajo", "Trabajo"),
        ("Hogar", "Hogar"),
        ("Estudio", "Estudio"),
    ]
    est = [
        ("Pendiente", "Pendiente"),
        ('En Progreso', 'En Progreso'),
        ('Completada', 'Terminada'),
    ]
    prioridad = [
        ("Alta", "Alta"),
        ("Media", "Media"),
        ("Baja", "Baja"),
    ]
    
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=200, verbose_name= 'Título')
    descripcion = models.TextField(verbose_name= 'Descripción')
    fechaTermino = models.DateField(verbose_name= 'Fecha de Termino')
    estado = models.CharField(choices=est, default = 'Pendiente',verbose_name= 'Estado')
    categoria = models.CharField(choices=cat, verbose_name= 'Categoría')
    prioridad = models.CharField(choices=prioridad, verbose_name= 'Prioridad')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.id + ' - ' +  str(self.titulo)
    

class Tareacompletada(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fechaCompletada = models.DateField()
    estado = models.CharField(max_length=150)
    categoria = models.CharField(max_length=150)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
