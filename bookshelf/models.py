from django.db import models


# Create your models here.
class Book(models.Model):
    Code=models.ForeignKey('BarCode',on_delete=models.CASCADE,null=False)
    title=models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author=models.ForeignKey('Author',on_delete=models.CASCADE,null=True)
    awards = models.CharField(max_length=400)
    langs=(
        ('English',"English"),
        ('Malayalam',"Malayalam"),
        ('Hindi',"Hindi"),
    )
    language=models.CharField(
        max_length=10,
        choices=langs,
        default='English',
    )
    def is_upperclass(self):
        return '{0}'.format(self.language)
    Edition=models.IntegerField()
    def __str__(self):
        return self.title



class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{0} {1}'.format(self.first_name , self.last_name)


class A_Logger(models.Model):
    bar_code_no=models.ForeignKey('BarCode',on_delete=models.CASCADE,null=True)
    book=models.ForeignKey('Book',on_delete=models.CASCADE,null=True)
    #due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey('Log_user' , on_delete=models.CASCADE, null=True, blank=True)
    
    LOAN_STATUS = (
        ('On loan', 'On loan'),
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
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
