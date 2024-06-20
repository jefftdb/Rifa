from django.shortcuts import render,redirect,HttpResponse
from usuario.models import User,Endereco,Telefone
from usuario.forms import UsuarioEnderecoForm
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, login as auth_login

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioEnderecoForm(request.POST, request.FILES)
        if form.is_valid():
            
            # primeiro, salvar o endereço associado ao usuário
            endereco = Endereco(
                rua=form.cleaned_data['rua'],
                numero=form.cleaned_data['numero'],
                complemento=form.cleaned_data.get('complemento'),
                bairro=form.cleaned_data['bairro'],
                cidade=form.cleaned_data['cidade'],
                estado=form.cleaned_data['estado'],
                cep=form.cleaned_data['cep'],
                pais=form.cleaned_data['pais']
            )            

            # Segundo, salvar o usuário
            usuario = User(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=make_password(form.cleaned_data['password']),
                email=form.cleaned_data['email'],
                cpf=form.cleaned_data['cpf'],
                cover=form.cleaned_data.get('cover'),
                endereco=endereco  # Associate the saved Endereco
            )
            email = User.objects.filter(email = usuario.email).first()

            if email:
                return HttpResponse(f'Email já cadastrado {email}')
            else:

                endereco.save()
                usuario.save()

                # Associar o endereço ao usuário
                usuario.endereco = endereco
                usuario.save()

                telefone = Telefone(               
                    ddd = form.cleaned_data['ddd'],
                    telefone = form.cleaned_data['telefone'],
                    usuario = usuario
                )
                telefone.usuario = usuario
                telefone.save()

                return redirect('rifa:nova_rifa')  # Substitua 'success_url' pela URL desejada após o envio do formulário
    else:
        form = UsuarioEnderecoForm()
    return render(request, 'cadastro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if user:
            # Use o método authenticate com o username e password
            auth = authenticate(username=user.username, password=senha)
            if auth:
                auth_login(request, auth)
                return HttpResponse('Autenticado')
            else:
                return HttpResponse('Email ou senha invalido')
        else:
            return HttpResponse('Email ou senha invalido')
    else:
        return render(request, 'login.html')
    