from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'added_date', 'photo')
    search_fields = ['name', 'description']
    list_filter = ('added_date',)
    readonly_fields = ('added_date',)
    

admin.site.register(Product, ProductAdmin)