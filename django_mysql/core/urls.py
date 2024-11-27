
from django.urls import path
from .views import home, productos, register, resultados, exit


urlpatterns = [
    path('', home, name='home'),
    path('productos/', productos, name='productos'),
    path('resultados/', resultados, name='resultados'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
    
]