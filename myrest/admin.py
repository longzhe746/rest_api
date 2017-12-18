from django.contrib import admin
from myrest.models import *

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('name',  'title','author')
    class Meta:
        model = Book

admin.site.register(Book,BookAdmin)