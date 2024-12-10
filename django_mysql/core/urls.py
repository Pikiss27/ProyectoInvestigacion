
from django.urls import path
from .views import home, productos, register, resultados, exit
from .views import edit_profile


urlpatterns = [
    path('', home, name='home'),
    path('informacion/', productos, name='informacion'),
    path('resultados/', resultados, name='resultados'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
    path('edit-profile/', edit_profile, name='edit_profile'),

    
]