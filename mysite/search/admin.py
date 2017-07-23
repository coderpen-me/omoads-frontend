from django.contrib import admin
from .models import Book, Author, Publisher, Banner,Agency,Profile,Order,Order_Info,Customer,Cart

# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Banner)
admin.site.register(Agency)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Order_Info)
admin.site.register(Cart)