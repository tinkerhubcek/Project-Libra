from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    Language=models.ForeignKey('Language',on_delete=models.SET_NULL,null=True)
    Edition=models.IntegerField()
    def __str__(self):
        return self.title



class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '{0},{1}'.format(self.first_name , self.last_name)

class Language(models.Model):
    English="English"
    Malayalam="Malayalam"
    Hindi="Hindi"
    langs=(
        ('English',"English"),
        ('Malayalam',"Malayalam"),
        ('Hindi',"Hindi"),
    )
    language=models.CharField(
        max_length=10,
        choices=langs,
        default=English,
    )
    def is_upperclass(self):
        return self.language in (self.English, self.Malayalam)
        
from datetime import date
from django.contrib.auth.models import User        
class Log(models.Model):
    book=models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('Lo', 'On loan'),
        ('Av', 'Available'),
        ('Re', 'Reserved'),
    )

    status = models.CharField(
        max_length=3,
        choices=LOAN_STATUS,
        blank=True,
        default='Av',
        help_text='Book availability')

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0}({1})'.format(self.borrower,self.book.title)        