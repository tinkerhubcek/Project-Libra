from django.shortcuts import render
from django.views import generic
from .models import Book,Log_user,A_Logger,Author,BarCode
# Create your views here.
def main_page(request):
    num_books = Book.objects.all().count()
    bar_num= BarCode.objects.all().count()
    user_num= Log_user.objects.all().count()
    ln_books= A_Logger.objects.filter(status__exact='On loan').count()
    #avail_books=A_Logger.objects.filter(status__exact ='On loan').count()
    av_book = num_books-ln_books
    context = {
        'book': num_books,
        'bar_code':bar_num,
        'num_users': user_num,
        'book_onloan': ln_books,
        'book_av':av_book,
        #'num_authors': num_authors,
    }
    return render(request, 'bookshelf/index.html', context=context)
class Books(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'
    template="bookshelf/book_list.html"   # your own name for the list as a template variable
    queryset = Book.objects.all() # Get 5 books containing the title war  # Specify your own template name/location """ """