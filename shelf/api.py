from rest_framework.viewsets import ModelViewSet

from .models import Book


class BookViewSet(ModelViewSet):
    model = Book