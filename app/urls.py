"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rifa.views import home
from django.conf import settings
from django.conf.urls.static import static
import os
from app.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('rifa/', include('rifa.urls')),
    path('pagamento/', include('pagamento.urls')),
    path('usuario/', include('usuario.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static('/usuario/static/', document_root=os.path.join(BASE_DIR, 'usuario/static'))
    urlpatterns += static('/rifa/static/', document_root=os.path.join(BASE_DIR, 'rifa/static'))
    urlpatterns += static('/pagamento/static/', document_root=os.path.join(BASE_DIR, 'pagamento/static'))