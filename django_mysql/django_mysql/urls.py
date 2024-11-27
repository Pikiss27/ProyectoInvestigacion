
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('machineLearning/', include('machineLearning.urls')),
    path('products/', include('products.urls')),
    path('usuarios/', include('usuarios.urls')),
   
]
