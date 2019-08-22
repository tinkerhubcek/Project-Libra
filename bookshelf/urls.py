from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('books/', views.Books.as_view(), name='books'),
    path('authors/',views.Authors.as_view(), name='authors'),
    path('logs/',views.Logged.as_view(), name='logs'),
    #path('admins/',views.admin, name='admin'),
    path('bookadd/',views.book_add_view, name='bookadd'),
    path('barcodeadd/',views.barcodeadd, name='barcodeadd'),
    path('authoradd/',views.authoradd, name='authoradd'),
    path('useradd/',views.useradd, name='useradd'),
    path('log/',views.logger, name='logger')
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), 
]