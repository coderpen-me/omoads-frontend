from django.contrib import admin
from .models import Book, Author, Publisher, Banner

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Banner)