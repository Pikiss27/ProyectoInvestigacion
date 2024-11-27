from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('', views.lista_usuarios, name='lista_usuarios'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('editar/<int:pk>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar/<int:pk>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('buscar/', views.buscar_usuario, name='buscar_usuario'),
]
