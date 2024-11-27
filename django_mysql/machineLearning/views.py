from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from joblib import load
from .models import Respuesta
from django.db.models import Avg
import plotly.express as px

model = load('model/modelCRT.joblib')
# Create your views here.
@login_required
def formulario(request):
    
    if request.method == 'POST':
        pregunta1 = int(request.POST['pregunta1'])
        pregunta2 = int(request.POST['pregunta2'])   
        pregunta3 = int(request.POST['pregunta3'])
        pregunta4 = int(request.POST['pregunta4'])
        pregunta5 = int(request.POST['pregunta5'])
        pregunta6 = int(request.POST['pregunta6'])
        pregunta7 = int(request.POST['pregunta7'])
        pregunta8 = int(request.POST['pregunta8'])
        
        Y_pred = model.predict([[pregunta1, pregunta2, pregunta3, pregunta4]])
        
        if 13 <= Y_pred[0] <= 16:
            Y_pred = 'RIESGO BAJO'
        elif 8 <= Y_pred[0] <= 12:
            Y_pred = 'RIESGO MEDIO'
        elif 4 <= Y_pred[0] <= 7:
            Y_pred = 'RIESGO ALTO'
        else:
            Y_pred = 'FUERA DE RANGO'
            

        respuesta = Respuesta(
            pregunta1=pregunta1,
            pregunta2=pregunta2,
            pregunta3=pregunta3,
            pregunta4=pregunta4,
            pregunta5=pregunta5,
            pregunta6=pregunta6,
            pregunta7=pregunta7,
            pregunta8=pregunta8,
            resultado=Y_pred,
            usuario=request.user,
        )
        respuesta.save()
            
      #  return render(request, 'index.html', {'response': Y_pred})
    return render(request, 'index.html')


def graficar_resultados(request):
    # Obtener los datos de las respuestas
    respuestas = Respuesta.objects.all()

    # Lista de preguntas
    preguntas = ['pregunta1', 'pregunta2', 'pregunta3', 'pregunta4', 'pregunta5', 'pregunta6', 'pregunta7', 'pregunta8']

    # Diccionario para almacenar los gráficos HTML de cada pregunta
    graficos = {}

    # Generar un gráfico por cada pregunta
    for pregunta in preguntas:
        # Calcular el promedio para la pregunta actual
        promedio = respuestas.aggregate(promedio=Avg(pregunta))['promedio']

        # Crear el gráfico con Plotly
        fig = px.bar(
            x=[pregunta],  # Solo la pregunta actual
            y=[promedio],  # Su promedio
            labels={'x': 'Pregunta', 'y': 'Promedio'},
            title=f'Promedio de Respuestas para {pregunta}'
        )

        # Convertir el gráfico a HTML y almacenarlo
        graficos[pregunta] = fig.to_html(full_html=False)

    # Pasar todos los gráficos al template
    return render(request, 'grafico.html', {'graficos': graficos})