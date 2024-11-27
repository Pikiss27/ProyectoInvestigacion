from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from joblib import load
from .models import Respuesta

model = load('model/modelCRT.joblib')
# Create your views here.
@login_required
def formulario(request):
    
    if request.method == 'POST':
        pregunta1 = int(request.POST['pregunta1'])
        pregunta2 = int(request.POST['pregunta2'])   
        pregunta3 = int(request.POST['pregunta3'])
        pregunta4 = int(request.POST['pregunta4'])
        
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
            resultado=Y_pred,
            usuario=request.user,
        )
        respuesta.save()
            
      #  return render(request, 'index.html', {'response': Y_pred})
    return render(request, 'index.html')

   


def desarrolloCompetencias_view(request):
    # Puedes pasarle datos a la plantilla si es necesario
    
    return render(request, 'desarrolloCompetencias.html')
def liderazgo_view(request):
    # Puedes pasarle datos a la plantilla si es necesario
    
    return render(request, 'liderazgo.html')
def accionControl_view(request):
    # Puedes pasarle datos a la plantilla si es necesario
    
    return render(request, 'accionControl.html')
def organizacionTrabajo_view(request):
    # Puedes pasarle datos a la plantilla si es necesario
    
    return render(request, 'organizacionTrabajo.html')
def recuperacion_view(request):
    # Puedes pasarle datos a la plantilla si es necesario
    
    return render(request, 'recuperacion.html')
def soporteApoyo_view(request):
    # Puedes pasarle datos a la plantilla si es necesario
    
    return render(request, 'soporteApoyo.html')
def otros_view(request):
    # Puedes pasarle datos a la plantilla si es necesario
    
    return render(request, 'otros.html')