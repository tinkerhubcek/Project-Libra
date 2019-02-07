from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
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
        return '{0},{1}'.format(self.first_name , self.last_name)

# class Language(models.Model):
#    English="English"
#   Malayalam="Malayalam"
#    Hindi="Hindi"
#   langs=(
#      ('English',"English"),
#     ('Malayalam',"Malayalam"),
#    ('Hindi',"Hindi"),
#    )
#    language=models.CharField(
#        max_length=10,
#        choices=langs,
#        default=English,
#    )
#   def is_upperclass(self):
#        return '{0}'.format(self.language) 
        
from datetime import date
class A_Logger(models.Model):
    book=models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    bar_code_no=models.ForeignKey('ISBN',on_delete=models.SET_NULL,null=True)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey('Log_user' , on_delete=models.SET_NULL, null=True, blank=True)
    
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

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

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        """String for representing the Model object."""
        return '{0}({1}) and {2}'.format(self.borrower,self.book.title,self.status)        
class Log_user(models.Model):
    Name=models.CharField(max_length=100)
    depts=(
     ('CS',"Computer Science"),
     ('IT',"Information Technology"),
     ('EI',"Electronics and Instrumentation"),
     ('EC',"Electronics and Communication"),
     ('CE',"Civil"),
     ('EEE',"Electrical & Electronics")
    )
    Department=models.CharField(
        max_length=2,
        choices=depts,
        default='CS',
    )
    def is_upperclass(self):
        return '{0}'.format(self.department)
    
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
    Semester=models.CharField(
        max_length=2,
        choices=sem,
        default='S5',
    )
    def is_upperclass(self):
        return '{0}'.format(self.Semester)
    def __str__(self):
        """String for representing the Model object."""
        return '{0}({1},{2})'.format(self.Name,self.Department,self.Semester) 
  class ISBN(models):
    
    
