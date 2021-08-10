# Двойные скобки означают: print.
# Register your models here.
from django.contrib import admin
from products.models import Category, ConfirmCode
from products.models import Tag
from products.models import Product


class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product
    search_fields = ['title', 'description']
    list_display = 'id title category price'.split()
    list_filter = 'category'.split()
    list_per_page = 3


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
admin.site.register(ConfirmCode)
