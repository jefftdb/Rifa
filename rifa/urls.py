from django.urls import path

from . import views

app_name = 'rifa'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('nova_rifa', views.nova_rifa, name = 'nova_rifa'),
    path('edit_rifa/<int:rifa_id>/<int:id>', views.edit_rifa, name = 'edit_rifa'),
    path('<int:id>', views.rifa, name = 'rifa'),
    
]