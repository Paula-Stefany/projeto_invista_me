"""
URL configuration for projeto_invista_me project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from usuarios import views as user_views
from invista_me import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', user_views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name="usuarios/logout.html"), name='logout'),
    path('investimentos/', views.investimentos, name='investimentos'),
    path('investimentos/novo_investimento/', views.criar, name='novo_investimento'),
    path('investimentos/detalhe/<int:id_investimento>/', views.detalhe, name='detalhe'),
    path('investimentos/editar/<int:id_investimento>/', views.editar, name='editar'),
    path('investimentos/excluir/<int:id_investimento>/', views.excluir, name='excluir'),
    path('cadastro/', user_views.novo_usuario, name='novo_usuario')
]
