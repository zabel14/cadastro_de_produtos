from django.shortcuts import render, redirect, get_object_or_404
from . import models
# Create your views here.
from .models import Produtos


def index(request):
    return render(request, 'base.html')


def produto_cadastrar(request):
    if request.method == "POST":
        nome = request.POST['nome']
        marca = request.POST['marca']
        particularidade = request.POST['particularidade']
        quantidade = request.POST['quantidade']
        categoria = request.POST['categoria']
        produto = Produtos.objects.create(nome=nome, marca=marca, particularidade=particularidade, quantidade=quantidade, categoria=categoria)
        produto.save()
        return redirect('produto_cadastrar_sucesso')
    return render(request, 'produto_cadastrar.html')

def produto_cadastrar_sucesso(request):
    return render(request, 'produto_cadastrar_sucesso.html')


def produto_listar(request):
    produto = Produtos.objects.all()
    produtos = {'lista': produto}
    return render(request, 'produto_listar.html', produtos)

def produto_remover(request, pk):
    produto = Produtos.objects.get(pk=pk)
    if request.method == "POST":
        produto.delete()
        return redirect('produto_listar')
    return render(request, 'produto_remover.html', {'produto': produto})

def produto_editar(request, pk):
    produto = get_object_or_404(Produtos, pk=pk)
    if request.method == 'POST':
        nome = request.POST['nome']
        marca = request.POST['marca']
        particularidade = request.POST['particularidade']
        quantidade = request.POST['quantidade']
        categoria = request.POST['categoria']
        produto.nome = nome
        produto.marca = marca
        produto.particularidade = particularidade
        produto.quantidade = quantidade
        produto.categoria = categoria
        produto.save(update_fields=['nome', 'marca', 'particularidade', 'quantidade', 'categoria'])
        return redirect('produto_editar_sucesso')
    return render(request, 'produto_editar.html', {'produto': produto})

def produto_editar_sucesso(request):
    return render(request, 'produto_editar_sucesso.html')