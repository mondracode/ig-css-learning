from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from instagramapp.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'registro.html')
def crear_usuario(request):
    _email = request.POST['email']
    _username = request.POST['username']
    _password = request.POST['password']
    _name = request.POST['name']
    print (_email)
    print (_username)
    print (_password)
    print (_name)
    user = User.objects.create_user( username = _username , email = _email , first_name = _name , password = _password )
    myuser = MiUsuario( usuario = user )
    myuser.save()
    print (user)
    print (User.password)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'home.html')
@login_required
def perfil(request):
    return render(request, 'perfil.html')
@login_required
def buscar(request):
    return render(request, 'buscar.html')
@login_required    
def subir(request):
    return render(request, 'subir.html')
