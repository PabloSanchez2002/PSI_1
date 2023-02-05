from django.urls import *
from . import views



urlpatterns = [
    path('catalog/', include('catalog.urls')),
]

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

urlpatterns += [
   path('', views.index, name='index'),
   path('authors/', views.AuthorListView.as_view(), name='authors'),
]

urlpatterns += [
  path('', views.index, name='index'),
  path('authors/', views.AuthorListView.as_view(), name='authors'),
  path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

