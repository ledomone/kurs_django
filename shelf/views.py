from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView

from .models import Author, Book
from .forms import AuthorForm


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class AuthorAddView(FormView):
    form_class = AuthorForm
    template_name = 'shelf/author_form.html'
    success_url = '/shelf/authors/'

    def form_valid(self, form):
        form.save()
        return super(AuthorAddView, self).form_valid(form)


class BookListView(ListView):
    model = Book


class BookDetailView(DetailView):
    model = Book