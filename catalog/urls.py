from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('produtos/', views.lista_produtos, name='lista_produtos'),
    path('produtos/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    path('produtos/novo/', views.produto_create, name='produto_create'),
    path('produtos/<int:pk>/editar/', views.produto_update, name='produto_update'),
    path('produtos/<int:pk>/excluir/', views.produto_delete, name='produto_delete'),
]