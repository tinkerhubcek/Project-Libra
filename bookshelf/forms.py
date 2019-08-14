from django import forms
from .models import Book,Log_user,A_Logger,Author,BarCode

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=[
            'Code',
            'title',
            'language',
            'author',
            'Edition'
        ]