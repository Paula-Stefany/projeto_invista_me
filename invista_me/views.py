from django.shortcuts import render, redirect
from .models import Investimento
from .forms import InvestimentoForm
from django.contrib.auth.decorators import login_required


@login_required
def investimentos(request):
    contexto = {'investimentos': Investimento.objects.all()}
    return render(request, 'investimentos/investimentos.html', contexto)


@login_required
def criar(request):

    if request.method == 'POST':
        novo_investimento = InvestimentoForm(request.POST)
        if novo_investimento.is_valid():
            novo_investimento.save()
        return redirect('investimentos')

    contexto = {'formulario': InvestimentoForm}
    return render(request, 'investimentos/novo_investimento.html', contexto)


@login_required
def detalhe(request, id_investimento):
    contexto = {'investimento': Investimento.objects.get(pk=id_investimento)}
    return render(request, 'investimentos/detalhe.html', contexto)


@login_required
def editar(request, id_investimento):
    investimento_a_ser_editado = Investimento.objects.get(pk=id_investimento)

    if request.method == 'POST':
        investimento_editado = InvestimentoForm(request.POST, instance=investimento_a_ser_editado)
        if investimento_editado.is_valid():
            investimento_editado.save()
        return redirect('investimentos')

    contexto = {'formulario': InvestimentoForm(instance=investimento_a_ser_editado)}
    return render(request, 'investimentos/novo_investimento.html', contexto)


@login_required
def excluir(request, id_investimento):
    investimento_a_ser_excluido = Investimento.objects.get(pk=id_investimento)

    if request.method == 'POST':
        investimento_a_ser_excluido.delete()
        return redirect('investimentos')

    contexto = {'investimento': investimento_a_ser_excluido}
    return render(request, 'investimentos/excluir_investimento.html', contexto)
