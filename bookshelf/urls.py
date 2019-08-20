from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('Add Books',views.Book_API_View)

urlpatterns = [
    path('', views.main_page, name='index'),
    path('books/', views.Books.as_view(), name='books'),
    path('authors/',views.Authors.as_view(), name='authors'),
    path('logs/',views.Logged.as_view(), name='logs'),
    path('bookadd/',views.book_add_view, name='bookadd'),
    path('barcodeadd/',views.barcodeadd, name='barcodeadd'),
    path('authoradd/',views.authoradd, name='authoradd'),
    path('useradd/',views.useradd, name='useradd'),
    path('log/',views.logger, name='logger'),
    path('API/',include(router.urls)),
    #path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), 
]
