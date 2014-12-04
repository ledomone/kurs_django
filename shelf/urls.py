from django.conf.urls import patterns, include, url


from shelf.views import AuthorListView, AuthorDetailView, AuthorAddView, BookListView, BookDetailView

urlpatterns = patterns('',
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
    url(r'^authors/new/$', AuthorAddView.as_view(), name='author-new'),
    url(r'^books/$', BookListView.as_view(), name='book-list'),
    url(r'^books/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book-detail'),
)
