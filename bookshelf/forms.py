from django import forms
from .models import *
class BookForm(forms.ModelForm):
    LANGS=(
        ('English',"English"),
        ('Malayalam',"Malayalam"),
        ('Hindi',"Hindi"),
    )
    CATEGORIES =[
        ("Theology", "Theology"),
        ("Philosophy", "Philosophy"),
        ("Novel", "Novel"),
        ("Short Story", "Short Story"),
        ("Self Help ", "Self Help "),
        ("Yathra Vivaranm", "Yathra Vivaranm"),
        ("Travel", "Travel"),
        ("Poetry", "Poetry"),
        ("Samburna Crithikal", "Samburna Crithikal"),
        ("Classic Series", "Classic Series"),
        ("Geology", "Geology"),
        ("Culture and Society", "Culture and Society"),
        ("History", "History"),
        ("Others", "Others"),
    ]
    YEARS= [x for x in range(1980,2030)]
    Code=forms.ModelChoiceField(queryset=BarCode.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}))
    author=forms.ModelChoiceField(queryset=Author.objects.all(),widget=forms.Select(attrs={"placeholder":"Author of the Book",
    "class":"btn btn-primary dropdown-toggle"}))
    title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title of the Book",
    "class":"form-control"}))
    description=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Description of the Book",
    "class":"form-control"}))
    awards=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Awards Received",
    "class":"form-control"}))
    category=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}),choices=CATEGORIES)
    date_of_purchase = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    MRP = forms.FloatField(widget=forms.TextInput(attrs={"placeholder":"Price of the Book",
    "class":"form-control"}))

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
    full_name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the Name of the Author",
    "class":"form-control"}), required=True)
    class Meta:
        model = Author
        fields = ("__all__")
class Log_userForm(forms.ModelForm):
    Name=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the User's Name",
    "class":"form-control"}), required=True)
    Address = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the User's Address",
    "class":"form-control"}), required=True)
    class Meta:
        model = Log_user
        fields = ("__all__")
class LogForm(forms.ModelForm):
    STATUS = (
        ('On loan', 'On loan'),
        ('Reserved', 'Reserved'),
    )
    bar_code_no=forms.ModelChoiceField(queryset=BarCode.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}))
    book=forms.ModelChoiceField(queryset=Book.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}), required=True)
    borrower=forms.ModelChoiceField(queryset=Log_user.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}))
    status=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}),choices=STATUS)
    class Meta:
        model = A_Logger
        fields = ("__all__")
class logdelform(forms.ModelForm):
    STATUS = (
        ('On loan', 'On loan'),
        ('Reserved', 'Reserved'),
    )
    bar_code_no=forms.ModelChoiceField(queryset=BarCode.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}))
    borrower=forms.ModelChoiceField(queryset=Log_user.objects.all(),widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}))
    status=forms.ChoiceField(widget=forms.Select(attrs={"class":"btn btn-primary dropdown-toggle"}),choices=STATUS)
    class Meta:
        model = A_Logger
        fields = ("bar_code_no",'status','borrower')


