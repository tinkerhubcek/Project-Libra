from django import forms
from .models import Book,Log_user,A_Logger,Author,BarCode
code_choices=BarCode.objects.all()
class BookForm(forms.ModelForm):
    #code=forms.ModelMultipleChoiceField(queryset=BarCode.object.all())
    title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title of the Book",
    "class":"form-control"}))
    author=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Author of the Book",
    "class":"form-control"}))
    code=forms.ModelChoiceField(queryset=BarCode.objects.all(),widget=forms.ChoiceField(attrs={"class":"btn btn-secondary dropdown-toggle"}))
    class Meta:
        model=Book
        fields='__all__'
""" class BookForm(forms.Form):
    Code= forms.IntegerField()
    title=forms.CharField()
    language=forms.CharField() """
    # So hey you should try to make the dropdown box with better UI using some widgets and stuff