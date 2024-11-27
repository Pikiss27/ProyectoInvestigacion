from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'machineLearning'

urlpatterns = [
    path('', views.formulario, name='formulario'),
    path('desarrolloCompetencias/', views.desarrolloCompetencias_view, name='desarrolloCompetencias'),
    path('liderazgo/', views.liderazgo_view, name='liderazgo'),
    path('accionControl/', views.accionControl_view, name='accionControl'),
    path('organizacionTrabajo/', views.organizacionTrabajo_view, name='organizacionTrabajo'),
    path('recuperacion/', views.recuperacion_view, name='recuperacion'),
    path('soporteApoyo/', views.soporteApoyo_view, name='soporteApoyo'),
    path('otros/', views.otros_view, name='otros'),
]


