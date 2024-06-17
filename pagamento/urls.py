from django.urls import path

from . import views

app_name = 'pagamento'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('pag', views.pagamentos, name = 'pagamentos'),
    path('pix/<int:rifa_id>/<int:num_id>', views.pagar_com_pix, name = 'pagar_com_pix'),
    
]