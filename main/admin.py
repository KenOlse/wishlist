from django.contrib import admin


from .models import Product, WishListUser


class ProductAdmin(admin.ModelAdmin):
    '''
        Admin View for Product
    '''
    list_display = ('title', 'link', 'price', 'added',)
    list_filter = ('price',)
    search_fields = ('title',)


admin.site.register(Product, ProductAdmin)

class WishListUserAdmin(admin.ModelAdmin):
    '''
        Admin View for WishlistUser
    '''
    list_display = ('title', 'owner', 'is_hidden',)

admin.site.register(WishListUser, WishListUserAdmin)

