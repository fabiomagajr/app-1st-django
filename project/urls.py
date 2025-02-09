"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse

def empty_view(request):
    return HttpResponse('Aqui nao tem nada')

def home_view(request):
    return HttpResponse('Home page')

def my_view(request):
    print('Servidor rodando normalmente.')
    return HttpResponse('Primeiros passos no django')

def teste(id):
    return HttpResponse(f'Seu ID é {id}')

urlpatterns = [
    path('',empty_view),
    path('home/',home_view),
    path('admin/', admin.site.urls),
    path('blog/',my_view),
    # path('teste/<int:id>',teste(id))
]
