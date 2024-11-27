# models.py

# machineLearning/models.py

from django.db import models

class Respuesta(models.Model):
    pregunta1 = models.IntegerField()
    pregunta2 = models.IntegerField()
    pregunta3 = models.IntegerField()
    pregunta4 = models.IntegerField()
    resultado = models.CharField(max_length=50, default='INDETERMINADO')
    fecha = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Respuesta {self.id}'
