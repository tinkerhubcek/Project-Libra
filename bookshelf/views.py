from django.shortcuts import render
from .models import Book,Log_user,A_Logger,Author,BarCode
# Create your views here.
def main_page(request):
    return render(request, 'bookshelf/index.html', {book:'book'})