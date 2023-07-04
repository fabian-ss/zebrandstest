from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','sku','name','price','is_active','brand','counter','created_at')
    list_display_links = ('id','sku','name')
    search_fields = ('sku','name')
    list_per_page = 25


admin.site.register(Product, ProductAdmin)
