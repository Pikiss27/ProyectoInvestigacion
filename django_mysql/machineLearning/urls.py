from django.urls import path
from . import views



app_name = 'machineLearning'

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('graficar_resultados/', views.graficar_resultados, name='graficar_resultados'),
]


