from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('books/', views.Books.as_view(), name='books'),
    path('authors/',views.Authors.as_view(), name='authors'),
    path('bookadd/',views.book_add_view, name='bookadd'),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), 
]