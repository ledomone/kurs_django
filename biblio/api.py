# coding: utf-8

from rest_framework import routers
from shelf.api import AuthorViewSet, BookViewSet


router = routers.DefaultRouter()


router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
