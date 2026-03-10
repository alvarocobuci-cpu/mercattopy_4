from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Produto
from .forms import ProdutoForm
from .models import Produto, Categoria

def lista_categorias(request):
    categorias = Categoria.objects.filter(ativa=True)
    return render(request, 'catalog/categorias.html', {
        'categorias': categorias
    })


def lista_produtos(request):
    produtos = Produto.objects.select_related('categoria').filter(ativo=True)
    return render(request, 'catalog/produtos.html', {
        'produtos': produtos
    })


def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id, ativo=True)
    return render(request, 'catalog/detalhe_produto.html', {
        'produto': produto
    })

def produto_create(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto cadastrado com sucesso!")
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'catalog/produto_form.html', {'form': form})


def produto_update(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, "Produto atualizado com sucesso!")
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'catalog/produto_form.html', {'form': form})


def produto_delete(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        if produto.quantidade_estoque > 0:
            messages.error(request, "Não é possível excluir produto com estoque maior que zero.")
            return redirect('lista_produtos')

        produto.delete()
        messages.success(request, "Produto excluído com sucesso!")
        return redirect('lista_produtos')

    return render(request, 'catalog/produto_confirm_delete.html', {'produto': produto})