from django.shortcuts import render,redirect
from usuario.models import Usuario,Endereco,Telefone
from usuario.forms import UsuarioEnderecoForm
from django.contrib.auth.hashers import make_password

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
            endereco.save()

            # Segundo, salvar o usuário
            usuario = Usuario(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=make_password(form.cleaned_data['password']),
                email=form.cleaned_data['email'],
                cpf=form.cleaned_data['cpf'],
                cover=form.cleaned_data['cover'],
                endereco=endereco  # Associate the saved Endereco
            )
            usuario.save()

            # Associar o endereço ao usuário
            usuario.endereco = endereco
            usuario.save()

            telefone = Telefone(
                pais = form.cleaned_data['pais'],
                ddd = form.cleaned_data['ddd'],
                telefone = form.cleaned_data['telefone'],
                usuario_id = usuario
            )
            telefone.usuario_id = usuario
            telefone.save()

            return redirect('rifa:nova_rifa')  # Substitua 'success_url' pela URL desejada após o envio do formulário
    else:
        form = UsuarioEnderecoForm()
    return render(request, 'cadastro.html', {'form': form})
