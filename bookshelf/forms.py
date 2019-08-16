from django import forms
from .models import Book,Log_user,A_Logger,Author,BarCode

#code_choices=BarCode.objects.all()
class BookForm(forms.ModelForm):
    Code=forms.ModelChoiceField(queryset=BarCode.objects.all(),widget=forms.Select(attrs={"class":"btn btn-secondary dropdown-toggle"}))
    title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title of the Book",
    "class":"form-control"}))
    author=forms.ModelChoiceField(queryset=Author.objects.all(),widget=forms.Select(attrs={"placeholder":"Author of the Book",
    "class":"btn btn-danger dropdown-toggle"}))
    language=forms.ChoiceField()
    class Meta:
        model=Book
        fields='__all__'



""" class BookForm(forms.Form):
    Code= forms.IntegerField()
    title=forms.CharField()
    language=forms.CharField() """
    # So hey you should try to make the dropdown box with better UI using some widgets and stuff

