from django.db import models

# Create your models here.
class Personas(models.Model):
    # Campos del modelo Personas
    nombre = models.CharField(max_length=100)
    # Otros campos que consideres relevantes
    
    def __str__(self):
        return self.nombre

class Tareas(models.Model):
    # Campos del modelo Tareas
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    # Otros campos que consideres relevantes
    
    # Relación muchos a uno con el modelo Personas
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE, related_name='tareas')
    
    def __str__(self):
        return self.titulo