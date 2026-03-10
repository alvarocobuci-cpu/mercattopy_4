from django.shortcuts import render, redirect
from catalog.models import Produto
from .models import Sale, SaleItem


def create_sale(request):

    products = Produto.objects.all()

    if request.method == 'POST':

        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity'))

        product = Produto.objects.get(id=product_id)

        # valida estoque
        if quantity > product.estoque:
            return render(request, 'sales/create_sale.html', {
                'products': products,
                'error': 'Estoque insuficiente'
            })

        sale = Sale.objects.create()

        subtotal = product.preco * quantity

        SaleItem.objects.create(
            sale=sale,
            product=product,
            quantity=quantity,
            unit_price=product.preco,
            subtotal=subtotal
        )

        sale.total = subtotal
        sale.save()

        # baixa estoque
        product.estoque -= quantity
        product.save()

        return redirect('/')

    return render(request, 'sales/create_sale.html', {'products': products})