from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


class CustomLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'usuarios/login.html'

    def form_valid(self, form):
        user = form.get_user()
        if user.is_staff:
            return redirect('admin:index')
        else:
            return super().form_valid(form)


def novo_usuario(request):
    if request.method == 'POST':
        usuario = UserRegisterForm(request.POST)
        if usuario.is_valid():
            usuario.save()
            nome_usuario = usuario.cleaned_data.get('username')
            messages.success(request, f'O usuário {nome_usuario} foi criado com sucesso!')
            return redirect('login')

    contexto = {'formulario': UserRegisterForm()}
    return render(request, 'usuarios/registrar.html', contexto)
