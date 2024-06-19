from django.contrib import admin
from usuario.models import Endereco,Usuario,Telefone

class EnderecoAdmin(admin.ModelAdmin):
       list_display =( "id", "rua","numero" ,"complemento" ,"bairro","cidade","estado","cep","pais")
       search_fields = ( "id", "rua","numero","bairro","cidade","estado","cep","pais")

class UsuarioAdmin(admin.ModelAdmin):
       list_display =( "id", "first_name","last_name" ,"password" ,"email","cpf","endereco")
       search_fields = ( "id", "first_name","last_name","email","cpf","telefone")

class TelefoneAdmin(admin.ModelAdmin):
       list_display =( "id", "ddd","telefone","usuario_id")
       search_fields = ( "id","telefone")

admin.site.register(Endereco,EnderecoAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Telefone,TelefoneAdmin)
