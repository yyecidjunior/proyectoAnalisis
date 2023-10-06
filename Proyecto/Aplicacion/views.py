from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CostomUserCreationForm
from django.contrib.auth import authenticate,login
from .models import Cliente

 
# Create your views here. 
@login_required
def home(request):
    cliente = Cliente.objects.all()
    return render(request,'index.html',{"cliente":cliente})

def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})


def registro(request):
    return render(request,'registro.html')

def exit(request):
    logout(request)
    return redirect('home')

def registrarCliente(request):

    Nombre=request.POST['Nombre'] 
    Gmail = request.POST['Gmail']
    Celular = request.POST['Celular']
    Direccion = request.POST['Direccion']

    cliente = Cliente.objects.create(Nombre=Nombre, Gmail=Gmail, Celular=Celular, Direccion=Direccion)
    
    return redirect('/')




def edicionCliente(request, cliente_id):
    cliente=Cliente.objects.get(id=cliente_id)
    return render(request, "edicionCliente.html", {"cliente":cliente})


def editarInfo(request, cliente_id):

    Nombre = request.POST['Nombre']
    Gmail = request.POST['Gmail']
    Celular = request.POST['Celular']
    Direccion = request.POST['Direccion']

    cliente=Cliente.objects.get(id=cliente_id)

    cliente.Nombre = Nombre
    cliente.Gmail = Gmail
    cliente.Celular = Celular
    cliente.Direccion = Direccion

   
    cliente.save()

     
    return redirect('detalle_cliente', cliente_id=cliente.id)


def register(request):
    if request.method == 'POST':
        user_creation_form = CostomUserCreationForm(request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()
            # Autenticar al usuario y luego iniciar sesión
            username = user_creation_form.cleaned_data['username']
            password = user_creation_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')  

    else:
        user_creation_form = CostomUserCreationForm()

    return render(request, 'registration/register.html', {'form': user_creation_form})
