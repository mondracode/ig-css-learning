from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'registro.html')
def crear_usuario(request):
    print ("Entre")
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    name = request.POST['name']
    print (email)
    print (username)
    print (password)
    print (name)
    return render(request, 'registro.html')

def login(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'home2.html')
def perfil(request):
    return render(request, 'perfil.html')
def buscar(request):
    return render(request, 'buscar.html')
