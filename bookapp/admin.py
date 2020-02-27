from django.contrib import admin
from .models import Bookwriter,Author,Publisher

# Register your models here.

admin.site.register(Bookwriter)
admin.site.register(Author)
admin.site.register(Publisher)