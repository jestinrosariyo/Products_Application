from django.contrib import admin
from .models import Product

# Register your models here.
# admin.site.register(Product)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display=('name','price','description','type')
    list_filter=('name','price','description','type')
    search_fields=('name','price','description','type')
    