from django.db import models

# Create your models here.
class Persona(models.Model):
    # Campos del modelo Personas
    documento = models.CharField(max_length=20, primary_key=True, default='')
    tipo_documento=models.CharField(max_length=20, default='')
    nombre = models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.nombre

class Tarea(models.Model):
    # Campos del modelo Tareas
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
   
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tareas')
    
    def __str__(self):
        return self.titulo
    
    