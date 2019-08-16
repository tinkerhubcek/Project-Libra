from django import forms
from .models import Book,Log_user,A_Logger,Author,BarCode

#code_choices=BarCode.objects.all()

status = (
        ('On loan', 'On loan'),
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
    )
depts=(
     ('CS',"Computer Science"),
     ('IT',"Information Technology"),
    )
bch=(
        ('B.Tech',"B.Tech"),
        ('M.Tech',"M.Tech")
    )
sem=(
        ('S1',"S1"),
        ('S2',"S2"),
        ('S3',"S3"),
        ('S4',"S4"),
        ('S5',"S5"),
        ('S6',"S6"),
        ('S7',"S7"),
        ('S8',"S8"),
    )

class BookForm(forms.ModelForm):
    LANGS=(
        ('English',"English"),
        ('Malayalam',"Malayalam"),
        ('Hindi',"Hindi"),
    )
    Code=forms.ModelChoiceField(queryset=BarCode.objects.all(),widget=forms.Select(attrs={"class":"btn btn-secondary dropdown-toggle"}))
    title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title of the Book",
    "class":"form-control"}))
    author=forms.ModelChoiceField(queryset=Author.objects.all(),widget=forms.Select(attrs={"placeholder":"Author of the Book",
    "class":"btn btn-danger dropdown-toggle"}))
    language=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-danger dropdown-toggle"}),choices=LANGS)
    class Meta:
        model=Book
        fields='__all__'

class BarcodeForm(forms.ModelForm):
    number_code=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"",
    "class":"form-control"}
    ), max_length=15, required=True)
    class Meta:
        model = BarCode
        fields = ("__all__")
class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = ("__all__")

