from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Usuario
from .forms import UsuarioForm

# Vista para listar usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

# Vista para crear un nuevo usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:lista_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/crear_usuario.html', {'form': form})

# Vista para editar un usuario existente
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:lista_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/editar_usuario.html', {'form': form})

# Vista para eliminar un usuario
def eliminar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios:lista_usuarios')
    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})

# Vista para buscar usuarios
def buscar_usuario(request):
    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(nombre__icontains=query)
    else:
        usuarios = Usuario.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})
