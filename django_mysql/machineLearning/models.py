from django.db import models
from django.contrib.auth.models import User

class Respuesta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Respuesta', default='INDETERMINADO')
    # Preguntas 1
    pregunta1 = models.IntegerField()
    pregunta2 = models.IntegerField()
    pregunta3 = models.IntegerField()
    pregunta4 = models.IntegerField()
    pregunta5 = models.IntegerField()
    pregunta6 = models.IntegerField()
    pregunta7 = models.IntegerField()
    pregunta8 = models.IntegerField()
   
    resultado = models.CharField(max_length=50, default='INDETERMINADO')
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Respuesta {self.id}'
