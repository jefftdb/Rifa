from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_protect
from .models import Rifa,Number
from .forms import RifaForms


# Create your views here.
def home(request): 
    
    return redirect("rifa:nova_rifa")

def rifa(request,id):
   
    rifa = Rifa.objects.get(id = id)
    
    return render(request, 'template/index.html', context={
        'rifa': rifa 
    })


@csrf_protect
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


def edit_rifa(request,rifa_id,id):
   Number.objects.filter(id=id).update(status=False)

   return redirect('rifa:rifa', id=rifa_id)


def delete_recipe(request):
    pass


def login(request):
    pass