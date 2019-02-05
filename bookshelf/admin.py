from django.contrib import admin

# Register your models here.
from .models import Author,Log,Book, Language

admin.site.register(Log)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Language)

