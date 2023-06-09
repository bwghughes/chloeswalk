from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, Price


class PriceInlineAdmin(admin.TabularInline):
    model = Price
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PriceInlineAdmin]


admin.site.register(Product, ProductAdmin)