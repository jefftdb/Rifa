from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import Rifa,Number
from .forms import RifaForms
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request): 
    
    return render(request,'index.html')

def rifa(request,id):
   
    rifa = Rifa.objects.get(id = id)
    
    return render(request, 'rifa.html', context={
        'rifa': rifa 
    })


@csrf_protect
@login_required(login_url='/usuario/login')
def nova_rifa(request):
    if request.method == 'POST':
        form = RifaForms(request.POST, request.FILES)
        if form.is_valid():
            rifa = form.save()
            rifa.make_number()
            
            print("Formulário salvo com sucesso")
            return redirect('rifa:home')
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = RifaForms()
    return render(request, 'novaRifa.html', {'form': form})

@login_required(login_url='/usuario/login')
def edit_rifa(request,rifa_id,id):
   Number.objects.filter(id=id).update(status=False)

   return redirect('rifa:rifa', id=rifa_id)


def delete_rifa(request):
    pass


def login(request):
    pass