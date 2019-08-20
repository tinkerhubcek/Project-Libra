from django.shortcuts import render
from django.views import generic
from rest_framework import viewsets
from .forms import BookForm,BarcodeForm,AuthorForm,Log_userForm,LogForm
from .models import Book,Log_user,A_Logger,Author,BarCode
from .serializers import UserSerializer,BookSerializer
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
    context_object_Name='lgg'
    template='bookshelf/a_logger_list.html'
    queryset=A_Logger.objects.filter(status__exact='On loan')

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
class User_API_View(viewsets.ModelViewSet):
    queryset=A_Logger.objects.all()
    serializer_class=UserSerializer
class Book_API_View(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer