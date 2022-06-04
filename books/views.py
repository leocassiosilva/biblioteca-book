from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from books.forms import BooksModelForm
from books.models import Books
from rest_framework import viewsets
from books.serializer import BookSerializer

#Class para criar livro
class BookCreate(CreateView):
    model = Books
    form_class = BooksModelForm
    template_name = 'books/new-book.html'
    success_message = "Livro cadastrado com sucesso!"
    success_url = reverse_lazy('list_book')

#Class para listar livro
class BookList(ListView):
    model = Books
    template_name = 'books/list_books.html'

#Class para atualizar informações do livro
class BookUpdate(UpdateView):
    model = Books
    form_class = BooksModelForm
    template_name = 'books/update_book.html'
    success_url = reverse_lazy('list_book')

#Class para deletar livro
class BookDelete(DeleteView):
    model = Books
    success_url = reverse_lazy('list_book')


#API
class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer