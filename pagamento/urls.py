from django.urls import path

from . import views

app_name = 'pagamento'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('pag', views.pagamentos, name = 'pagamentos'),
    
]