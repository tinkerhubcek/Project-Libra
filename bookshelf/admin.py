from django.contrib import admin

# Register your models here.
from .models import A_Logger,Book,Log_user,Author,BarCode

admin.site.register(A_Logger)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Log_user)
admin.site.register(BarCode)

