from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from rest_framework import viewsets
from .forms import *
from .models import *
from .serializers import *
# Create your views here.
@login_required
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
    context_object_name = 'book_list'
    template="bookshelf/book_list.html"   # your own name for the list as a template variable
    queryset = Book.objects.all() # Get 5 books containing the title war  # Specify your own template name/location """ """
class Authors(generic.ListView):
    model=Author
    context_object_name='auth_list'
    template='bookshelf/author_list.html'
    queryset=Author.objects.all()
class Logged(generic.ListView):
    model=A_Logger
    context_object_Name='log_user_list'
    template='bookshelf/a_logger_list.html'
    queryset=A_Logger.objects.filter(status__exact='On loan')

""" def admin(request):
    form=adminForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=adminForm()
    context={
        'form':form
    }
    return render(request,"bookshelf/admin.html",context) """
def book_add_view(request):
    form=BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=BookForm()
    context={
        'form':form
    }
    return render(request,"bookshelf/add_book.html",context)
def barcodeadd(request):
    form=BarcodeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=BarcodeForm()
    context={
        'form':form
    }
    return render(request,"bookshelf/baradd.html",context)
def useradd(request):
    form=Log_userForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=Log_userForm()
    context={
        'form':form
    }
    return render(request,"bookshelf/useradd.html",context)
def authoradd(request):
    form=AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=AuthorForm()
    context={
        'form':form
    }
    return render(request,"bookshelf/authoradd.html",context)
def logger(request):
    form=LogForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=LogForm()
    context={
        'form':form
    }
    return render(request,"bookshelf/logger.html",context)
class Code_API_View(viewsets.ModelViewSet):
    queryset=BarCode.objects.all()
    serializer_class=CodeSerializer
class Book_API_View(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
class Author_API_View(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
class Log_API_View(viewsets.ModelViewSet):
    queryset=A_Logger.objects.all()
    serializer_class=LoggerSerializer
class User_API_View(viewsets.ModelViewSet):
    queryset=Log_user.objects.all()
    serializer_class=UserSerializer
class Users(generic.ListView):
    model = Log_user
    context_object_name = 'log_user_list'
    template="bookshelf/log_user_list.html"   # your own name for the list as a template variable
    queryset = Log_user.objects.all()

from django.contrib.postgres.search import SearchVector,SearchQuery
class BookSearch(generic.ListView):
    model = Book
    def get_queryset(self): # new
        query= self.request.GET.get('q')
        object_list = Book.objects.filter(
             title__search=query
        )
        return object_list
class logSearch(generic.ListView):
    model=Log_user
    def get_queryset(self): # new
        query= self.request.GET.get('q')
        object_list = Log_user.objects.filter(
             Name__search=query
        )
        return object_list
class bsearch(generic.TemplateView):
    template_name="bookshelf/bsearch.html"
class usearch(generic.TemplateView):
    template_name="bookshelf/usearch.html"