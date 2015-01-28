from django.conf.urls import patterns, include, url
from .views import BookRentView

urlpatterns = patterns('',
    url(r'^form/$', BookRentView.as_view(), name='rent-form'),
)