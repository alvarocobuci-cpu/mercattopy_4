from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque', 'ativo', 'categoria']

    # Validação do preço
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 0:
            raise forms.ValidationError("O preço não pode ser negativo.")
        return preco

    # Validação do estoque
    def clean_estoque(self):
        estoque = self.cleaned_data.get('estoque')
        if estoque < 0:
            raise forms.ValidationError("O estoque não pode ser negativo.")
        return estoque

    # Validação do nome
    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if len(nome) < 3:
            raise forms.ValidationError("O nome deve ter pelo menos 3 caracteres.")
        return nome

    # Regra: categoria precisa estar ativa
    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria.ativa:
            raise forms.ValidationError("A categoria selecionada está inativa.")
        return categoria