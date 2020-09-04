from django.db import models


# Create your models here.
class Book(models.Model):
    Code=models.ForeignKey('BarCode',on_delete=models.CASCADE,null=False)
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author=models.ForeignKey('Author',on_delete=models.CASCADE,null=True)
    awards = models.CharField(max_length=400)
    date_of_purchase = models.DateField()
    MRP = models.FloatField()
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
    category=models.CharField(
        max_length=150,
        choices=CATEGORIES,
        default="Novel",
        help_text="Book Type"
    )
    def __str__(self):
        return self.title



class Author(models.Model):
    """Model representing an author."""
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return '{0}'.format(self.full_name)


class A_Logger(models.Model):
    bar_code_no=models.ForeignKey('BarCode',on_delete=models.CASCADE,null=True)
    book=models.ForeignKey('Book',on_delete=models.CASCADE,null=True)
    #due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey('Log_user' , on_delete=models.CASCADE, null=True, blank=True)
    
    LOAN_STATUS = (
        ('On loan', 'On loan'),
        ('Available', 'Available')
    )

    status = models.CharField(
        max_length=10,
        choices=LOAN_STATUS,
        blank=True,
        default='Available',
        help_text='Book availability')
    def __str__(self):
        """String for representing the Model object."""
        return '({0}) and {1}'.format(self.borrower,self.status)

class Log_user(models.Model):
    Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    def __str__(self):
        """String for representing the Model object."""
        return '{0}({1})'.format(self.Name,self.Address) 
        
class BarCode(models.Model):
    number_code=models.CharField(max_length=12)
    #number_code=models.IntegerField()
    def __str__(self):
        return self.number_code
