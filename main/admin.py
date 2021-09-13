from django.contrib import admin


from .models import Product


class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    list_display = ('title', 'link', 'price', 'added',)
    list_filter = ('price',)
    search_fields = ('title',)


admin.site.register(Product, ProductAdmin)
