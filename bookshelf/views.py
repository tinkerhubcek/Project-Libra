from django.shortcuts import render
from django.views import generic
from .models import Book,Log_user,A_Logger,Author,BarCode
# Create your views here.
def main_page(request):
    num_books = Book.objects.all().count()
    bar_num= BarCode.objects.all().count()
    user_num= Log_user.objects.all().count()
    ln_books= A_Logger.objects.filter(status__exact='On loan').count()
    avail_books=A_Logger.objects.filter(status__exact='Available').count()
    context = {
        'book': num_books,
        'bar_code':bar_num,
        'num_users': user_num,
        'book_onloan': ln_books,
        'book_av':avail_books,
        #'num_authors': num_authors,
    }
    
    return render(request, 'bookshelf/index.html', context=context)