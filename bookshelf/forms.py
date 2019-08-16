from django import forms
from .models import Book,Log_user,A_Logger,Author,BarCode

#code_choices=BarCode.objects.all()
class BookForm(forms.ModelForm):
    Code=forms.ModelChoiceField(queryset=BarCode.objects.all(),widget=forms.Select(attrs={"class":"btn btn-secondary dropdown-toggle"}))
    title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title of the Book",
    "class":"form-control"}))
    author=forms.ModelChoiceField(queryset=Author.objects.all(),widget=forms.Select(attrs={"placeholder":"Author of the Book",
    "class":"form-control"}))
    
    class Meta:
        model=Book
        fields=[
            'Code',
            'title',
            'language',
            'author',
            'Edition'
        ]