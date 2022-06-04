from django import forms

from .models import Books


class BooksModelForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['nome', 'autor', 'descricao']