from django.contrib import admin

# Register your models here.
from .models import Product , Brand , Review , ProductImages

class ProductImagesInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','flag','price']
    list_filter = ['flag','price','quantity']
    search_fields = ['name','subtitle','description']
    inlines = [ProductImagesInline]


class ReviewAdmin(admin.ModelAdmin):
    list_display=['user','product','rate','create_at']
    list_filter = ['create_at','rate']

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review,ReviewAdmin)
