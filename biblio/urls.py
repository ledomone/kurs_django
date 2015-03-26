from django.conf.urls import patterns, include, url
from django.contrib import admin
from contact.views import MessageAddView
from django.conf import settings
from django.conf.urls.static import static
from .api import router

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shelf/', include('shelf.urls', namespace='shelf')),
    url(r'^contact/$', MessageAddView.as_view()),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^rental/', include('rental.urls', namespace='rental')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'api/v1/', include(router.urls)),


    url(r'^$', 'shelf.views.index_view', name='main-page'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

