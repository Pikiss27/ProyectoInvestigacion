from django.shortcuts import render, redirect
from .forms import UserUpdateForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def exit(request):
    logout(request)
    return redirect('home')

def resultados(request):
    return render(request, 'core/resultados.html')

def productos(request):
    return render(request, 'core/productos.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Cambia 'home' por tu vista deseada tras guardar
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'registration/edit_profile.html', {'form': form})