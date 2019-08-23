from django import forms
from .models import Book,Log_user,A_Logger,Author,BarCode
class BookForm(forms.ModelForm):
    LANGS=(
        ('English',"English"),
        ('Malayalam',"Malayalam"),
        ('Hindi',"Hindi"),
    )
    Code=forms.ModelChoiceField(queryset=BarCode.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}))
    title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title of the Book",
    "class":"form-control"}))
    author=forms.ModelChoiceField(queryset=Author.objects.all(),widget=forms.Select(attrs={"placeholder":"Author of the Book",
    "class":"btn btn-primary dropdown-toggle"}))
    language=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}),choices=LANGS)
    class Meta:
        model=Book
        fields='__all__'

class BarcodeForm(forms.ModelForm):
    number_code=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the Barcode",
    "class":"form-control"}
    ), max_length=15, required=True)
    class Meta:
        model = BarCode
        fields = ("__all__")
class AuthorForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the First Name",
    "class":"form-control"}), required=True)
    last_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the Last Name",
    "class":"form-control"}), required=True)
    class Meta:
        model = Author
        fields = ("__all__")
class Log_userForm(forms.ModelForm):
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
    Name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the User's Name",
    "class":"form-control"}), required=True)
    Department=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}),choices=depts)
    Branch=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}),choices=bch)
    Semester=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}),choices=sem)
    class Meta:
        model = Log_user
        fields = ("__all__")
class LogForm(forms.ModelForm):
    STATUS = (
        ('On loan', 'On loan'),
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
    )
    bar_code_no=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the BarCode","class":"form-control"}))
    book=forms.ModelChoiceField(queryset=Book.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}), required=True)
    borrower=forms.ModelChoiceField(queryset=Log_user.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}))
    status=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}),choices=STATUS)
    class Meta:
        model = A_Logger
        fields = ("__all__")


