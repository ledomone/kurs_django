from rest_framework import routers

from shelf.api import BookViewSet


router = routers.DefaultRouter()

router.register(r'books', BookViewSet)
# router.register(r'groups', views.GroupViewSet)