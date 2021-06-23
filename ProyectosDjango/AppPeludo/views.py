from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from AppPeludo.models import Mascotas



#Clases
class Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

# Create your views here.
def home (request):
    return render (request,'Index.html')

def Clima(request):
    return render(request,'Clima.html')

def Blanca(request):
    return render(request,'Blanca.html')    

def Zohan(request):
    return render(request,'Zohan.html')    

def Sticha(request):
    return render(request,'Sticha.html')

def Escanor(request):
    return render(request,'Escanor.html')            

def Rudeus(request):
    return render(request,'Rudeus.html')        

def nachotell(request):
    return render(request,'nachotell.html')        

def Meliodas(request):
    return render(request,'Meliodas.html')        

def Jey_Jey(request):
    return render(request,'Jey-Jey.html')    

def contacto(request):
    return render(request,'contacto.html')            

def nosotros(request):
    return render(request,'nosotros.html')        

def geolocal(request):
    return render(request,'geolocal.html')       

def gatos(request):
    return render(request,'gatos.html')      

def perros(request):
    return render(request,'perros.html')      

def Formulario(request):
    return render(request,'Formulario.html')    





#Objetos

def crearMascota(request):
    mascota = Mascotas(
        codigo = "MAS001",
        nombre = "Rudeus",
        especie = "Can",
        adoptado = False
    )
    mascota.save()

    return HttpResponse("Registro Mascota creado!!")

 
def prueba(request):
    lista=["Lasaña","Porotos","Charquican"]

    hijo=Persona("Fernando", "8")

    contexto = {"nombre":"Claudia Andrea","comidas":lista, "hijo":hijo}

    return render(request, 'test.html', contexto)   



#2° commit
def listaMascotas(request):
    mascotas = Mascotas.objects.all()

    return render(request, 'ListaMascotas.html', {'mascotas':mascotas})

def crearMascotaNav(request, codigo, nombre, especie):
    mascota = Mascotas(
        codigo = codigo,
        nombre = nombre,
        especie = especie,
        adoptado = 0
    )
    mascota.save()

    return redirect('listamascotas')

def leer_mascota(request, id):
    mascota = Mascotas.objects.get(id=id)

    return HttpResponse(f"La Mascota es : {mascota.codigo}, {mascota.nombre}")

def editar_mascota(request, id):
    mascota = Mascotas.objects.get(id=id)

    mascota.nombre = "Pecca"

    mascota.save()

    return HttpResponse(f"Nombre de mascota actualizado : {mascota.nombre}")

def borrar_mascota(request,id):
    mascota = Mascotas.objects.get(id=id)

    mascota.delete()

    return redirect('listamascotas')

def nuevaMascota(request):
    return render(request,'AgregarMascota.html')

def guardarMascota(request):

    codigo = request.POST['codigo']
    nombre = request.POST['nombre']
    especie = request.POST['especie']

    mascota = Mascotas(
        codigo = codigo,
        nombre = nombre,
        especie = especie,
        adoptado = 0
    )

    mascota.save()

    return redirect('listamascotas')