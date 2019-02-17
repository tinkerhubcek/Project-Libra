from django.shortcuts import render
from django.views import generic
from .models import Book,Log_user,A_Logger,Author,BarCode
# Create your views here.
def main_page(request):
    num_books = Book.objects.all().count()
    bar_num= BarCode.objects.all().count()
    context = {
        'book': num_books,
        'bar_code':bar_num,
        #'num_instances': num_instances,
        #'num_instances_available': num_instances_available,
        #'num_authors': num_authors,
    }
    
    return render(request, 'bookshelf/index.html', context=context)